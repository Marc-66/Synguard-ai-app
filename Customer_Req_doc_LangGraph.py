"""
Synguard AI Requirements Agent — LangGraph Refactor
====================================================
Original: sequential OpenAI calls inside a single Streamlit button handler.
Refactored: typed StateGraph with one node per agent, explicit edges, and a
compiled graph that Streamlit invokes as a single unit.

Key LangGraph concepts used
────────────────────────────
  StateGraph      — the graph itself; holds all nodes + edges
  AgentState      — a TypedDict that is the single shared memory object
                    passed from node to node (replaces ad-hoc session_state strings)
  Nodes           — plain Python functions that receive state and return a partial update
  Edges           — declare which node runs after which (add_edge / add_conditional_edges)
  compile()       — turns the graph definition into a runnable object
  .invoke()       — runs the full graph synchronously; returns the final state
"""

import os, json
import streamlit as st
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from typing import TypedDict, List, Dict, Any, Optional

# ── LangGraph imports ──────────────────────────────────────────────────────────
from langgraph.graph import StateGraph, END

# ── LLM client (same as original — Azure or plain OpenAI) ─────────────────────
from openai import OpenAI
from openai.lib.azure import AzureOpenAI

load_dotenv()
azure_api_key      = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint     = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_version  = os.getenv("AZURE_OPENAI_API_VERSION")
azure_deployment   = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
openai_api_key     = os.getenv("OPENAI_API_KEY")

if azure_api_key or azure_endpoint:
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        azure_deployment=azure_deployment,
        api_version=azure_api_version,
        api_key=azure_api_key,
    )
else:
    client = OpenAI(api_key=openai_api_key)

MODEL = "gpt-4o"

# ══════════════════════════════════════════════════════════════════════════════
# 1. SHARED STATE  ← THE CORE LANGGRAPH CONCEPT
#    Every node receives this dict and returns a *partial* update to it.
#    Nothing is passed as function arguments between agents — the graph
#    handles routing and state merging automatically.
# ══════════════════════════════════════════════════════════════════════════════

class AgentState(TypedDict):
    # ── inputs collected from the UI ──
    cust_input:          str
    resolved_problem:    str
    current_situation:   str
    desired_functionality: str
    integration_details: str
    ui_ux_expectations:  str
    constraints_conditions: str

    # ── outputs written by each node ──
    cust_req:            str          # written by node_crd
    tech_req:            str          # written by node_tech
    matrix_data:         List[Dict]   # written by node_matrix
    sow_body:            str          # written by node_sow

    # ── pipeline control ──
    error:               Optional[str]


# ══════════════════════════════════════════════════════════════════════════════
# 2. HELPER — thin LLM wrapper
# ══════════════════════════════════════════════════════════════════════════════

def llm(prompt: str, temperature: float = 0.2) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return resp.choices[0].message.content


# ══════════════════════════════════════════════════════════════════════════════
# 3. NODES  ← each is a pure function(state) -> dict
#    They read from state, call the LLM, and return only the keys they update.
#    LangGraph merges the returned dict into the running state automatically.
# ══════════════════════════════════════════════════════════════════════════════

def node_crd(state: AgentState) -> dict:
    """Agent 1 — Customer Requirements Document."""
    prompt = f"""Je bent de Synguard AI Requirements Agent.
Synthetiseer de input tot een gestructureerd Customer Requirements Document (CRD).

Probleem dat opgelost wordt : {state['resolved_problem']}
Huidige situatie            : {state['current_situation']}
Gewenste functionaliteit    : {state['desired_functionality']}

Ruwe klantvraag:
{state['cust_input']}

Schrijf een CRD met secties: Samenvatting, Customer Needs (CN-001…), Functionele Eisen, Niet-functionele Eisen."""
    try:
        return {"cust_req": llm(prompt)}
    except Exception as e:
        return {"error": f"node_crd failed: {e}"}


def node_tech(state: AgentState) -> dict:
    """Agent 2 — Technical Specifications + Traceability Matrix."""
    prompt = f"""Je bent de Synguard AI Technical Agent.
Maak volledige technische specificaties op basis van het CRD hieronder.
Voeg een Traceability Matrix toe als markdown tabel met kolommen:
FR/NFR ID | Traces To CN | Description | Technische Architectuur Component | QA / Test Scenario

Integratie details : {state['integration_details']}
UI/UX verwachtingen: {state['ui_ux_expectations']}
Constraints        : {state['constraints_conditions']}

CRD:
{state['cust_req']}"""
    try:
        return {"tech_req": llm(prompt)}
    except Exception as e:
        return {"error": f"node_tech failed: {e}"}


def node_matrix(state: AgentState) -> dict:
    """Agent 3 — Extract Traceability Matrix from tech doc into structured JSON."""
    prompt = f"""Je bent een data-extractie expert.
Lees de Tech Specs en extraheer de Traceability Matrix naar een valide JSON array.

Verplicht formaat (exact deze keys):
[{{"FR/NFR ID": "FR-001", "Traces To CN": "CN-001", "Description": "...",
   "Technische Architectuur Component": "...", "QA / Test Scenario (Acceptatiecriterium)": "..."}}]

Geef UITSLUITEND de JSON array terug. Geen markdown, geen backticks, geen uitleg.

Tech Specs:
{state['tech_req']}"""
    try:
        raw = llm(prompt, temperature=0.1)
        clean = raw.strip().replace("```json", "").replace("```", "").strip()
        matrix = json.loads(clean)
        return {"matrix_data": matrix}
    except Exception as e:
        return {"matrix_data": [], "error": f"node_matrix parse error: {e}"}


def node_sow(state: AgentState) -> dict:
    """Agent 4 — Statement of Work (SoW)."""
    prompt = f"""Je bent de Synguard Commercial & Delivery Agent.
Schrijf een formele Statement of Work (SoW) op basis van de Tech Specs.

# Statement of Work (SoW)
**Datum:** {datetime.now().strftime('%d-%m-%Y')}
**Status:** Draft / For Review

Gebruik EXACT deze secties:
1. Projectdoel
2. Project Scope (met FR-codes en acceptatiecriteria per item)
3. Technische Scope & Integratiearchitectuur
4. Deliverables (D-001 t/m D-006)
5. Out of Scope
6. Rollen & Verantwoordelijkheden
7. Planning & Mijlpalen (markdown tabel)
8. Afhankelijkheden & Risico's
9. Change Request Procedure
10. Acceptatie & Sign-Off

Tech Specs:
{state['tech_req']}"""
    try:
        return {"sow_body": llm(prompt)}
    except Exception as e:
        return {"error": f"node_sow failed: {e}"}


# ══════════════════════════════════════════════════════════════════════════════
# 4. CONDITIONAL EDGE — route to END on error, otherwise continue
# ══════════════════════════════════════════════════════════════════════════════

def route_on_error(state: AgentState) -> str:
    """If any node set an error, stop the pipeline early."""
    return "end" if state.get("error") else "continue"


# ══════════════════════════════════════════════════════════════════════════════
# 5. GRAPH DEFINITION & COMPILATION  ← happens once at module load
#    compile() validates the graph (no dangling nodes, no unreachable nodes)
#    and returns an object with .invoke() / .stream() / .astream()
# ══════════════════════════════════════════════════════════════════════════════

def build_graph():
    graph = StateGraph(AgentState)

    # Register nodes
   
    graph.add_node("crd",    node_crd)
    graph.add_node("tech",   node_tech)
    graph.add_node("matrix", node_matrix)
    graph.add_node("sow",    node_sow)

    # Entry point
    graph.set_entry_point("crd")

    # Edges with error guard after each node
    graph.add_conditional_edges("crd",    route_on_error, {"continue": "tech",   "end": END})
    graph.add_conditional_edges("tech",   route_on_error, {"continue": "matrix", "end": END})
    graph.add_conditional_edges("matrix", route_on_error, {"continue": "sow",    "end": END})
    graph.add_edge("sow", END)

    return graph.compile()


# Compile once; reused on every Streamlit rerun
pipeline = build_graph()


# ══════════════════════════════════════════════════════════════════════════════
# 6. STREAMLIT UI  — identical look/feel to original; only the generate
#    section changes: one pipeline.invoke() call replaces four sequential
#    client.chat.completions.create() calls.
# ══════════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="Synguard AI Requirements Agent (LangGraph)", layout="wide")

DEFAULT_STATES = {
    "cust_input": "", "cust_req": "", "tech_req": "", "sow_body": "",
    "current_filepath": "",
    "development_type": "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
    "business_driver": "Requested in Official Tender",
    "is_customer_specific": "Customer Specific (Unique)",
    "verticals": [], "benchmark_competitor": "", "link_project": "", "link_product": "",
    "total_project_value": 0, "chargeable_value": 0, "potential_yearly_revenue": 0,
    "resolved_problem": "", "value_end_customer": "", "value_partner": "", "value_synguard": "",
    "current_situation": "", "overall_workflow": "", "desired_functionality": "",
    "integration_details": "", "ui_ux_expectations": "", "acceptance_criteria": "",
    "constraints_conditions": "", "tender_text": "",
    "matrix_data": [],
    "sow_budget_data": [
        {"Discipline / Jira Component": "Solution Architecture & Design",         "Geschatte Uren": 8,  "Uurtarief (€)": 125},
        {"Discipline / Jira Component": "SynApp Front-end Development (UI)",      "Geschatte Uren": 24, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "SynCon Firmware Integration",            "Geschatte Uren": 16, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "Database & Security Engineering",        "Geschatte Uren": 12, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "QA / Test Automation & Validation",      "Geschatte Uren": 16, "Uurtarief (€)": 95},
        {"Discipline / Jira Component": "Project Management & Documentation",     "Geschatte Uren": 8,  "Uurtarief (€)": 125},
    ],
}

for k, v in DEFAULT_STATES.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Sidebar archive ────────────────────────────────────────────────────────────
st.sidebar.title("📚 Archief & Historie")
history_dir = "outputs/generated_srs"
if os.path.exists(history_dir):
    saved_files = [f for f in os.listdir(history_dir) if f.endswith(".md")]
    if saved_files:
        selected_file = st.sidebar.selectbox("Kies een eerdere aanvraag:", sorted(saved_files, reverse=True))
        if st.sidebar.button("📂 Open Dossier"):
            filepath = os.path.join(history_dir, selected_file)
            st.session_state.current_filepath = filepath
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                raw = f.read()
            parts = raw.split("[---SPLIT-DOSSIER---]")
            if len(parts) >= 3:
                st.session_state.cust_input = parts[0].strip()
                st.session_state.cust_req   = parts[1].strip()
                st.session_state.tech_req   = parts[2].strip()
                if len(parts) >= 4:
                    try:
                        meta = json.loads(parts[3].strip())
                        for key, val in meta.items():
                            st.session_state[key] = val
                    except Exception as e:
                        st.sidebar.error(f"Metadatafout: {e}")
            st.sidebar.success("Dossier herladen!")
            st.rerun()

# ── Main UI ────────────────────────────────────────────────────────────────────
st.subheader("Vertaal ongestructureerde klantvragen automatisch naar technische specificaties & SoW")
st.title("🚀 Synguard AI Requirements & SoW Architect  —  LangGraph Edition")

col1, col2 = st.columns([1, 1.5])

with col1:
    if st.button("➕ Start Nieuw Dossier", type="secondary", use_container_width=True):
        for k, v in DEFAULT_STATES.items():
            st.session_state[k] = v
        st.toast("Leeggemaakt!", icon="🧹")
        st.rerun()

    st.markdown("### 📥 Klant Input")
    st.text_area("Plak hier de e-mail of ruwe aanvraag:", height=150, key="cust_input")

    dev_types = [
        "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
        "2. Back-end Software integrations with 3rd party solution",
        "3. New Software functionality impacting flow/operation/logic/UI",
        "4. New functionality related to Mobile app or Cloud",
    ]
    st.selectbox("Type ontwikkelingsverzoek:", dev_types, key="development_type")

    with st.expander("💼 Commerciële Impact & Business Value", expanded=False):
        st.selectbox("Business Driver:", ["Requested in Official Tender", "Strategic Feature for Market", "Customer Retention", "Partner Request"], key="business_driver")
        st.selectbox("Is Customer Specific?", ["Customer Specific (Unique)", "Standard Product Enhancement (Reusable)"], key="is_customer_specific")
        st.multiselect("Verticals:", ["Corporate", "Logistics", "Healthcare", "Government", "Education", "Retail"], key="verticals")
        st.text_input("Benchmark Competitor:", key="benchmark_competitor")
        st.text_input("Link to Project/Tender:", key="link_project")
        st.text_input("Link to Product Requirement/Jira:", key="link_product")
        st.number_input("Total Project Value (€):", min_value=0, step=1000, key="total_project_value")
        st.number_input("Chargeable Value (€):", min_value=0, step=500, key="chargeable_value")
        st.number_input("Potential Yearly Revenue (€):", min_value=0, step=500, key="potential_yearly_revenue")

    with st.expander("📝 Functional Description", expanded=False):
        st.text_area("Welk probleem wordt opgelost?", key="resolved_problem")
        st.text_area("Value for end customer:", key="value_end_customer")
        st.text_area("Value for partner/integrator:", key="value_partner")
        st.text_area("Value for Synguard:", key="value_synguard")
        st.markdown("---")
        st.text_area("Current Situation / Pijnpunten:", key="current_situation")
        st.text_area("Overall Workflow:", key="overall_workflow")
        st.text_area("Desired Functionality:", key="desired_functionality")
        st.text_area("Integration Details / API context:", key="integration_details")
        st.text_area("UI/UX Expectations:", key="ui_ux_expectations")
        st.text_area("Acceptance Criteria:", key="acceptance_criteria")
        st.text_area("Constraints / Conditions:", key="constraints_conditions")
        st.text_area("Raw Tender Text:", key="tender_text")

    st.markdown("---")

    # ── GENERATE BUTTON — the only part that changed vs the original ──────────
    generate_button = st.button(
        "🚀 Genereer Volledige Pijplijn (LangGraph)",
        type="primary",
        use_container_width=True,
    )

    if generate_button:
        if not st.session_state.cust_input:
            st.warning("Vul eerst een klantvraag in.")
        else:
            with st.spinner("LangGraph pipeline loopt… (CRD → Tech → Matrix → SoW)"):

                # ── BUILD INITIAL STATE FROM UI ──────────────────────────────
                # This replaces the four sequential client.chat.completions.create() calls.
                # We hand the graph ONE state dict; it runs all nodes and returns
                # the final enriched state.
                initial_state: AgentState = {
                    "cust_input":            st.session_state.cust_input,
                    "resolved_problem":      st.session_state.resolved_problem,
                    "current_situation":     st.session_state.current_situation,
                    "desired_functionality": st.session_state.desired_functionality,
                    "integration_details":   st.session_state.integration_details,
                    "ui_ux_expectations":    st.session_state.ui_ux_expectations,
                    "constraints_conditions":st.session_state.constraints_conditions,
                    # outputs start empty; nodes will fill them
                    "cust_req":   "",
                    "tech_req":   "",
                    "matrix_data": [],
                    "sow_body":   "",
                    "error":      None,
                }

                # ── SINGLE GRAPH INVOCATION ──────────────────────────────────
                result: AgentState = pipeline.invoke(initial_state)

                # ── WRITE RESULTS BACK TO SESSION STATE ──────────────────────
                if result.get("error"):
                    st.error(f"Pipeline fout: {result['error']}")
                else:
                    st.session_state.cust_req    = result["cust_req"]
                    st.session_state.tech_req    = result["tech_req"]
                    st.session_state.matrix_data = result["matrix_data"]
                    st.session_state.sow_body    = result["sow_body"]

                    # Auto-save
                    output_dir = "outputs/generated_srs"
                    os.makedirs(output_dir, exist_ok=True)
                    timestamp  = datetime.now().strftime("%Y%m%d_%H%M")
                    safe_title = "".join(c if c.isalnum() else "_" for c in st.session_state.cust_input[:30]).strip("_").lower()
                    st.session_state.current_filepath = os.path.join(output_dir, f"{timestamp}_{safe_title}.md")
                    ui_dict = {k: st.session_state[k] for k in DEFAULT_STATES if k in st.session_state}
                    with open(st.session_state.current_filepath, "w", encoding="utf-8") as f:
                        f.write(st.session_state.cust_input + "\n[---SPLIT-DOSSIER---]\n" +
                                st.session_state.cust_req   + "\n[---SPLIT-DOSSIER---]\n" +
                                st.session_state.tech_req   + "\n[---SPLIT-DOSSIER---]\n" +
                                json.dumps(ui_dict, indent=4))

                    st.rerun()

# ── Output tabs (identical to original) ───────────────────────────────────────
with col2:
    st.markdown("### 📤 AI Agent Output")
    tab1, tab2, tab3, tab4 = st.tabs(["📥 Customer Input", "👥 CRD", "🛠️ Tech Doc & Matrix", "📄 SoW"])

    with tab1:
        st.code(st.session_state.cust_input or "Nog geen input.", language="text")

    with tab2:
        st.markdown(st.session_state.cust_req or "Nog geen document gegenereerd.")

    with tab3:
        if st.session_state.tech_req:
            st.markdown(st.session_state.tech_req)
            st.markdown("---")
            st.markdown("### 📊 Requirements Traceability Matrix (Editable)")
            if st.session_state.matrix_data:
                df_matrix  = pd.DataFrame(st.session_state.matrix_data)
                edited_df  = st.data_editor(df_matrix, use_container_width=True, num_rows="dynamic")
                st.session_state.matrix_data = edited_df.to_dict(orient="records")
            else:
                st.warning("Matrix kon niet automatisch worden geparsed. Voeg handmatig rijen toe:")
                empty_df  = pd.DataFrame(columns=["FR/NFR ID", "Traces To CN", "Description", "Technische Architectuur Component", "QA / Test Scenario (Acceptatiecriterium)"])
                edited_df = st.data_editor(empty_df, use_container_width=True, num_rows="dynamic")
                st.session_state.matrix_data = edited_df.to_dict(orient="records")
        else:
            st.info("Nog geen Technical Requirements geladen.")

    with tab4:
        if st.session_state.sow_body:
            st.subheader("📄 Draft: Statement of Work")
            st.markdown("#### 💰 Budget & Jira Ureninschatting")
            df_budget = pd.DataFrame(st.session_state.sow_budget_data)
            edited_budget_df = st.data_editor(df_budget, use_container_width=True, num_rows="dynamic")
            st.session_state.sow_budget_data = edited_budget_df.to_dict(orient="records")
            edited_budget_df["Geschatte Uren"]  = pd.to_numeric(edited_budget_df["Geschatte Uren"],  errors="coerce").fillna(0)
            edited_budget_df["Uurtarief (€)"]   = pd.to_numeric(edited_budget_df["Uurtarief (€)"],   errors="coerce").fillna(0)
            edited_budget_df["Totaal (€)"]       = edited_budget_df["Geschatte Uren"] * edited_budget_df["Uurtarief (€)"]
            total_hours = edited_budget_df["Geschatte Uren"].sum()
            total_cost  = edited_budget_df["Totaal (€)"].sum()
            st.markdown(f"**Totaal:** `{total_hours} uur`  |  **Projectprijs:** `€ {total_cost:,.2f}` (excl. BTW)")
            st.markdown("---")
            edited_sow = st.text_area("SoW tekst (bewerkbaar):", value=st.session_state.sow_body, height=400)
            st.session_state.sow_body = edited_sow
            st.markdown("---")
            if st.button("💾 Sla Deliverables op naar `output/`"):
                budget_md = edited_budget_df.to_markdown(index=False)
                matrix_md = pd.DataFrame(st.session_state.matrix_data).to_markdown(index=False)
                os.makedirs("output", exist_ok=True)
                with open("output/statement-of-work.md", "w", encoding="utf-8") as f:
                    f.write(st.session_state.sow_body)
                    f.write(f"\n\n## 11. Budget (Jira Components)\n\n{budget_md}")
                    f.write(f"\n\n**Totale Investering:** € {total_cost:,.2f} (Excl. BTW)\n\n")
                    f.write(f"## 12. Appendix: Requirements Traceability Matrix\n\n{matrix_md}")
                if st.session_state.current_filepath and os.path.exists(st.session_state.current_filepath):
                    ui_dict = {k: st.session_state[k] for k in DEFAULT_STATES if k in st.session_state}
                    with open(st.session_state.current_filepath, "w", encoding="utf-8") as f:
                        f.write(st.session_state.cust_input + "\n[---SPLIT-DOSSIER---]\n" +
                                st.session_state.cust_req   + "\n[---SPLIT-DOSSIER---]\n" +
                                st.session_state.tech_req   + "\n[---SPLIT-DOSSIER---]\n" +
                                json.dumps(ui_dict, indent=4))
                st.success("✅ SoW opgeslagen in `output/statement-of-work.md`!")
        else:
            st.info("Genereer eerst de pijplijn om de SoW te zien.")