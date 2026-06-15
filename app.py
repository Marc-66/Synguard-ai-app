import streamlit as st
import os
from openai import OpenAI
from openai.lib.azure import AzureOpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
import pandas as pd

# --- CONFIGURATIE VAN DE PAGINA ---
st.set_page_config(page_title="Synguard AI Requirements Agent", layout="wide")

# --- INITIALISEER STANDAARD VALUES IN SESSION STATE ---
DEFAULT_STATES = {
    "cust_input": "", "cust_req": "", "tech_req": "", "sow_body": "", "current_filepath": "",
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
        {"Discipline / Jira Component": "Solution Architecture & Design", "Geschatte Uren": 8, "Uurtarief (€)": 125},
        {"Discipline / Jira Component": "SynApp Front-end Development (UI)", "Geschatte Uren": 24, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "SynCon Firmware Integration", "Geschatte Uren": 16, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "Database & Security Engineering", "Geschatte Uren": 12, "Uurtarief (€)": 110},
        {"Discipline / Jira Component": "QA / Test Automation & Validation", "Geschatte Uren": 16, "Uurtarief (€)": 95},
        {"Discipline / Jira Component": "Project Management & Documentation", "Geschatte Uren": 8, "Uurtarief (€)": 125}
    ]
}

for key, val in DEFAULT_STATES.items():
    if key not in st.session_state:
        st.session_state[key] = val

# --- HISTORISCHE DOCUMENTEN OPROEPEN VIA SIDEBAR ---
st.sidebar.title("📚 Archief & Historie")
history_dir = "outputs/generated_srs"

if os.path.exists(history_dir):
    saved_files = [f for f in os.listdir(history_dir) if f.endswith('.md')]
    if saved_files:
        selected_file = st.sidebar.selectbox("Kies een eerdere aanvraag:", sorted(saved_files, reverse=True))
        
        if st.sidebar.button("📂 Open Dossier"):
            filepath = os.path.join(history_dir, selected_file)
            st.session_state.current_filepath = filepath
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                raw_dossier = f.read()
            
            parts = raw_dossier.split("[---SPLIT-DOSSIER---]")
            
            if len(parts) >= 3:
                st.session_state.cust_input = parts[0].strip()
                st.session_state.cust_req = parts[1].strip()
                st.session_state.tech_req = parts[2].strip()
                
                if len(parts) >= 4:
                    try:
                        meta = json.loads(parts[3].strip())
                        for key, val in meta.items():
                            if key == "matrix_data" and isinstance(val, list):
                                updated_list = []
                                for row in val:
                                    new_row = {}
                                    new_row["FR/NFR ID"] = row.get("FR/NFR ID", row.get("Requirement ID", ""))
                                    new_row["Traces To CN"] = row.get("Traces To CN", row.get("Bron / Customer Need (CN)", ""))
                                    new_row["Description"] = row.get("Description", row.get("Functionele Omschrijving (FR)", ""))
                                    new_row["Technische Architectuur Component"] = row.get("Technische Architectuur Component", "[In te vullen door Engineering]")
                                    new_row["QA / Test Scenario (Acceptatiecriterium)"] = row.get("QA / Test Scenario (Acceptatiecriterium)", "")
                                    updated_list.append(new_row)
                                st.session_state.matrix_data = updated_list
                            else:
                                st.session_state[key] = val
                    except Exception:
                        pass
                st.sidebar.success("Dossier succesvol herladen!")
                st.rerun()

# API-key configuratie
load_dotenv()
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

if azure_api_key or azure_endpoint:
    client = AzureOpenAI(azure_endpoint=azure_endpoint, azure_deployment=azure_deployment, api_version=azure_api_version, api_key=azure_api_key)
else:
    client = OpenAI(api_key=openai_api_key)

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f: return f.read()
    return ""

synguard_products = read_file("knowledge/synguard_products.md")
tech_partners = read_file("knowledge/technology_partners.md")
product_catalogue = read_file("knowledge/product_catalogue.md")

# --- UI INTERFACE ---
st.subheader("Vertaal ongestructureerde klantvragen automatisch naar technische specificaties & SoW")
st.title("🚀 Synguard AI Requirements & SoW Architect")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### 📥 Klant Input")
    st.text_area("Plak hier de e-mail of ruwe aanvraag van de klant/integrator:", height=180, key="cust_input")
    
    dev_types = [
        "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
        "2. Back-end Software integrations with 3rd party solution",
        "3. New Software functionality impacting flow/operation/logic/UI",
        "4. New functionality related to Mobile app or Cloud"
    ]
    st.selectbox("Wat voor type ontwikkelingsverzoek is dit?", dev_types, key="development_type")

    with st.expander("💼 Commerciële Impact & Business Value"):
        st.text_input("Link naar Eindklant / Project / Tender:", key="link_project")
        st.number_input("Wat kunnen we hiervoor rekenen (Licentie, Maatwerk in €):", min_value=0, step=500, key="chargeable_value")

    with st.expander("📝 Functional Description (Technisch)"):
        st.text_area("Huidige situatie & Pijnpunten:", key="current_situation")
        st.text_area("Lijst van Gewenste Functionaliteiten:", key="desired_functionality")
        
    st.markdown("---")
    generate_button = st.button("🚀 Genereer Volledige Pijplijn (CRD -> Tech -> SoW)", type="primary", use_container_width=True)

    if generate_button:
        if not st.session_state.cust_input:
            st.warning("Vul eerst een klantvraag in.")
        else:
            with st.spinner("AI doorloopt de stappen en genereert de documenten..."):
                
                # --- STAP 1: Customer Requirements Document ---
                prompt_step1 = "Je bent de Synguard AI Requirements Agent. Synthetiseer de input tot een Customer Requirements rapport. Input: {raw}".format(raw=st.session_state.cust_input)
                response_step1 = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_step1}], temperature=0.2)
                st.session_state.cust_req = response_step1.choices[0].message.content

                # --- STAP 2: Technical Document ---
                prompt_step2 = "Je bent de Synguard AI Technical Agent. Maak de harde technische specificaties inclusief een duidelijke Traceability Matrix tabel in markdown op basis van: {cust}".format(cust=st.session_state.cust_req)
                response_step2 = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_step2}], temperature=0.2)
                st.session_state.tech_req = response_step2.choices[0].message.content

                # --- STAP 3: Matrix Extractie naar Data Editor (OPGELOST MET F-STRING & ESCAPING) ---
                tech_document_content = st.session_state.tech_req
                prompt_matrix = f"""Je bent een data-extractie expert. Lees de zojuist gegenereerde Tech Specs en extraheer de Traceability Matrix tabel naar een valide JSON array.

                Tech Specs:
                {tech_document_content}

                Formaat van de JSON output moet exact voldoen aan deze structuur:
                [{{ "FR/NFR ID": "FR-001", "Traces To CN": "CN-001", "Description": "...", "Technische Architectuur Component": "[In te vullen door Engineering]", "QA / Test Scenario (Acceptatiecriterium)": "..." }}]
                
                Genereer ALTIJD en UITSLUITEND de valide JSON array. Geen markdown codeblocks (geen backticks), geen inleidende tekst of afsluiting."""
                
                response_matrix = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_matrix}], temperature=0.1)
                
                try:
                    clean_json = response_matrix.choices[0].message.content.strip().replace("```json", "").replace("```", "").strip()
                    st.session_state.matrix_data = json.loads(clean_json)
                except Exception as e:
                    st.session_state.matrix_data = []

                # --- STAP 4: Statement of Work (SoW) Generatie ---
                prompt_sow = """
                Je bent de Synguard Commercial & Delivery Agent. Schrijf een formeel en professioneel 'Statement of Work' (SoW) document gericht aan de partner/klant.
                Gebruik hiervoor de details uit het Technical Requirements Document:
                {tech_doc}

                Structureer het document strak volgens de Synguard SoW indeling:
                1. Executive Summary & Project Purpose
                2. Detailed Scope of Work (Verwijs expliciet naar de unieke functionele requirements zoals FR-001)
                3. Out of Scope (Wat levert Synguard expliciet NIET, bijv. lokale IT-infrastructuur, bekabeling)
                4. Deliverables & Jira Component Mapping
                5. High-Level Timeline & Milestones
                6. Acceptance Criteria & Sign-off Procedure
                """.format(tech_doc=st.session_state.tech_req)
                
                response_sow = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt_sow}], temperature=0.3)
                st.session_state.sow_body = response_sow.choices[0].message.content

                # --- Sla tussentijds dossier op in het archief ---
                output_dir = "outputs/generated_srs"
                os.makedirs(output_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                safe_title = "".join([c if c.isalnum() else "_" for c in st.session_state.cust_input[:30]]).strip("_").lower()
                st.session_state.current_filepath = os.path.join(output_dir, f"{timestamp}_{safe_title}.md")
                
                ui_state_dict = {k: st.session_state[k] for k in DEFAULT_STATES.keys() if k not in ["cust_input", "cust_req", "tech_req", "current_filepath"]}
                with open(st.session_state.current_filepath, "w", encoding="utf-8") as f:
                    f.write(st.session_state.cust_input + "\n[---SPLIT-DOSSIER---]\n" + st.session_state.cust_req + "\n[---SPLIT-DOSSIER---]\n" + st.session_state.tech_req + "\n[---SPLIT-DOSSIER---]\n" + json.dumps(ui_state_dict))

                st.rerun()

with col2:
    st.markdown("### 📤 AI Agent Output")
    tab1, tab2, tab3, tab4 = st.tabs(["📥 Customer Input", "👥 Customer Requirements Doc", "🛠️ Technical Doc & Matrix", "📄 Statement of Work"])
    
    with tab1:
        st.code(st.session_state.cust_input if st.session_state.cust_input else "Nog geen input.", language="text")
            
    with tab2:
        st.markdown(st.session_state.cust_req if st.session_state.cust_req else "Nog geen document gegenereerd.")
            
    with tab3:
        if st.session_state.tech_req:
            st.markdown(st.session_state.tech_req)
            st.markdown("---")
            st.markdown("### 📊 Requirements Traceability Matrix (Editable)")
            
            if st.session_state.matrix_data:
                df_matrix = pd.DataFrame(st.session_state.matrix_data)
                # Zorg dat oude of wisselende kolomnamen netjes uniform getoond worden
                df_matrix = df_matrix.rename(columns={"Requirement ID": "FR/NFR ID", "Bron / Customer Need (CN)": "Traces To CN", "Functionele Omschrijving (FR)": "Description"})
                edited_df = st.data_editor(df_matrix, use_container_width=True, num_rows="dynamic")
                st.session_state.matrix_data = edited_df.to_dict(orient="records")
            else:
                st.warning("De interactieve tabel kon niet automatisch worden geparsed. Voeg hieronder handmatig rijen toe:")
                empty_df = pd.DataFrame(columns=["FR/NFR ID", "Traces To CN", "Description", "Technische Architectuur Component", "QA / Test Scenario (Acceptatiecriterium)"])
                edited_df = st.data_editor(empty_df, use_container_width=True, num_rows="dynamic")
                st.session_state.matrix_data = edited_df.to_dict(orient="records")
        else:
            st.info("Nog geen Technical Requirements geladen.")
            
    with tab4:
        if st.session_state.sow_body:
            st.subheader("📄 Draft: Statement of Work (SoW)")
            st.caption("Dit contract-ready document combineert de technische requirements, Jira disciplines en kostenbepalingen.")
            
            # Dynamische budget editor (Brug naar Jira & Ureninschatting)
            st.markdown("#### 💰 Project Budget & Jira Component Ureninschatting")
            df_budget = pd.DataFrame(st.session_state.sow_budget_data)
            edited_budget_df = st.data_editor(df_budget, use_container_width=True, num_rows="dynamic")
            st.session_state.sow_budget_data = edited_budget_df.to_dict(orient="records")
            
            # Bereken totalen live door op het scherm
            edited_budget_df["Geschatte Uren"] = pd.to_numeric(edited_budget_df["Geschatte Uren"], errors="coerce").fillna(0)
            edited_budget_df["Uurtarief (€)"] = pd.to_numeric(edited_budget_df["Uurtarief (€)"], errors="coerce").fillna(0)
            edited_budget_df["Totaal (€)"] = edited_budget_df["Geschatte Uren"] * edited_budget_df["Uurtarief (€)"]
            
            total_hours = edited_budget_df["Geschatte Uren"].sum()
            total_cost = edited_budget_df["Totaal (€)"].sum()
            
            st.markdown(f"**🔢 Totaal uren (Jira componenten):** `{total_hours} uur` | **💶 Totale projectprijs (Excl. BTW):** `€ {total_cost:,.2f}`")
            
            st.markdown("---")
            st.markdown("#### 🖋️ SoW Contract Inhoud")
            
            # De SoW tekst zelf is bewerkbaar in een grote textarea
            edited_sow_body = st.text_area("Bewerk de officiële SoW tekst hieronder indien nodig:", value=st.session_state.sow_body, height=400)
            st.session_state.sow_body = edited_sow_body
            
            st.markdown("---")
            if st.button("💾 Sla Officiële Deliverables op naar VS Code (`output/`)"):
                budget_markdown = edited_budget_df.to_markdown(index=False)
                matrix_markdown = pd.DataFrame(st.session_state.matrix_data).to_markdown(index=False)
                
                os.makedirs("output", exist_ok=True)
                with open("output/statement-of-work.md", "w", encoding="utf-8") as f:
                    f.write(f"# STATEMENT OF WORK (SoW) - SYNGUARD\n\n")
                    f.write(f"**Generatiedatum:** {datetime.now().strftime('%d-%m-%Y')}\n\n")
                    f.write(st.session_state.sow_body)
                    f.write(f"\n\n## 7. Commercial Terms & Resource Budget (Jira Components)\n\n")
                    f.write(budget_markdown)
                    f.write(f"\n\n**Gecalculeerde Totale Investering:** € {total_cost:,.2f} (Excl. BTW)\n\n")
                    f.write(f"## 8. Appendix: Requirements Traceability Matrix\n\n")
                    f.write(matrix_markdown)
                
                st.success("🎉 De Statement of Work (SoW) is succesvol weggeschreven naar `output/statement-of-work.md`!")
        else:
            st.info("Genereer eerst de pijplijn om de Statement of Work (SoW) in te zien.")