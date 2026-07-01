"""
SOW Template Formatter — Enforces Eurofiber Structure
======================================================

This module provides the standard SOW structure template and formatting functions
to ensure ALL generated and saved SOW documents follow the Eurofiber format.

Structure sections:
  1. Project Overzicht (title, metadata)
  2. Integratieflow (visual flows)
  3. Scope (in-scope and out-of-scope)
  4. Systeemvereisten (system requirements)
  5. Aannames (assumptions)
  6. Wijzigingsbeheer (change management)
  7. Op te leveren resultaten (deliverables)
  8. Acceptatiecriteria (acceptance criteria)
  9. Inschatting (estimation/budget)
  10. Roles & Responsibilities (RACI matrix)
  11. Aanvaarding (sign-off)
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
import json


class SOWTemplate:
    """Standard Eurofiber-based SOW template for consistent document generation."""
    
    # --- TEMPLATE STRUCTURE CONSTANTS ---
    SECTIONS = [
        "1. Project Overzicht",
        "2. Integratieflow",
        "3. Scope",
        "4. Systeemvereisten",
        "5. Aannames",
        "6. Wijzigingsbeheer",
        "7. Op te leveren resultaten",
        "8. Acceptatiecriteria",
        "9. Inschatting",
        "10. Roles & Responsibilities",
        "11. Aanvaarding",
    ]
    
    TABLE_OF_CONTENTS = "\n".join(SECTIONS)
    
    @staticmethod
    def format_header(project_name: str, version: str = "1.0", date: Optional[str] = None) -> str:
        """Format SOW document header."""
        if date is None:
            date = datetime.now().strftime("%d/%m/%Y")
        
        return f"""# STATEMENT OF WORK
## {project_name.upper()}

**V. {version} - {date}**  
**SYNGUARD | Always with you**

---

# INHOUDSOPGAVE

{SOWTemplate.TABLE_OF_CONTENTS}

---
"""
    
    @staticmethod
    def format_project_overview(metadata: Dict[str, Any]) -> str:
        """Format Section 1: Project Overzicht."""
        lines = [
            "# 1. PROJECT OVERZICHT",
            "",
            "| Item | Beschrijving |",
            "|------|---|",
        ]
        
        # Standard project metadata fields
        fields = [
            ("Project Naam", metadata.get("project_name", "N/A")),
            ("Eindklant", metadata.get("customer", "N/A")),
            ("SOW Datum", metadata.get("sow_date", datetime.now().strftime("%d/%m/%Y"))),
            ("Geschatte project duur", metadata.get("project_duration", "N/A")),
            ("Doel", metadata.get("objective", "N/A")),
            ("Korte omschrijving", metadata.get("short_description", "N/A")),
        ]
        
        for label, value in fields:
            lines.append(f"| **{label}** | {value} |")
        
        lines.extend([
            "",
            "## Omschrijving werk",
            "",
        ])
        
        work_items = metadata.get("work_description", [])
        for item in work_items:
            lines.append(f"- {item}")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_integration_flows(flows: Optional[Dict[str, str]] = None) -> str:
        """Format Section 2: Integratieflow."""
        if flows is None:
            flows = {}
        
        lines = [
            "",
            "---",
            "",
            "# 2. INTEGRATIEFLOW",
        ]
        
        # Add flow diagrams if provided
        for flow_name, flow_description in flows.items():
            lines.append(f"\n## {flow_name}\n")
            lines.append("```")
            lines.append(flow_description)
            lines.append("```\n")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_scope(in_scope: List[str], out_of_scope: List[str]) -> str:
        """Format Section 3: Scope (In Scope & Out of Scope)."""
        lines = [
            "",
            "---",
            "",
            "# 3. SCOPE",
            "",
            "## 3.1 In Scope",
            "",
        ]
        
        for i, item in enumerate(in_scope, 1):
            lines.append(f"### 3.1.{i} {item.split(':')[0].strip() if ':' in item else item}")
            if ':' in item:
                lines.append(item.split(':')[1].strip())
            lines.append("")
        
        lines.extend([
            "## 3.2 Out of Scope",
            "",
        ])
        
        for item in out_of_scope:
            lines.append(f"- {item}")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_system_requirements(requirements: Dict[str, List[str]]) -> str:
        """Format Section 4: Systeemvereisten."""
        lines = [
            "",
            "---",
            "",
            "# 4. SYSTEEMVEREISTEN",
            "",
        ]
        
        for category, items in requirements.items():
            lines.append(f"### {category}")
            for item in items:
                lines.append(f"- {item}")
            lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_assumptions(assumptions: List[str]) -> str:
        """Format Section 5: Aannames."""
        lines = [
            "---",
            "",
            "# 5. AANNAMES",
            "",
        ]
        
        for assumption in assumptions:
            lines.append(f"- {assumption}")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_change_management() -> str:
        """Format Section 6: Wijzigingsbeheer (standard template)."""
        return """---

# 6. WIJZIGINGSBEHEER

Wijzigingen worden beheerd via:
- Change Requests (formeel document)
- Impactanalyse (tijd/kosten/scope impact)
- Goedkeuring door Product Owner
- Geautoriseerde personen: Project Manager, Product Owner

**Scope Change Request Template:**
- Omschrijving wijziging
- Reden/Business Driver
- Estimated impact (uren, risico's)
- Goedkeuring (ja/nee)
"""
    
    @staticmethod
    def format_deliverables(deliverables: List[Dict[str, str]]) -> str:
        """Format Section 7: Op te leveren resultaten."""
        lines = [
            "",
            "---",
            "",
            "# 7. OP TE LEVEREN RESULTATEN",
            "",
        ]
        
        for i, deliverable in enumerate(deliverables, 1):
            title = deliverable.get("title", f"Deliverable {i}")
            description = deliverable.get("description", "")
            items = deliverable.get("items", [])
            
            lines.append(f"### 7.{i} {title}")
            if description:
                lines.append(description)
            for item in items:
                lines.append(f"- {item}")
            lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_acceptance_criteria(criteria: Dict[str, List[str]]) -> str:
        """Format Section 8: Acceptatiecriteria."""
        lines = [
            "---",
            "",
            "# 8. ACCEPTATIECRITERIA",
            "",
        ]
        
        for section, items in criteria.items():
            lines.append(f"## {section}")
            for item in items:
                lines.append(f"- ✓ {item}")
            lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_estimation(budget_data: List[Dict[str, Any]], phases: Optional[List[Dict[str, str]]] = None) -> str:
        """Format Section 9: Inschatting (Budget and Phases)."""
        lines = [
            "---",
            "",
            "# 9. INSCHATTING",
            "",
            "## Effort per Discipline",
            "",
            "| Discipline | Uren | Uurtarief | Totaal |",
            "|---|---:|---:|---:|",
        ]
        
        total_hours = 0
        total_cost = 0
        
        for item in budget_data:
            discipline = item.get("Discipline / Jira Component", "")
            hours = item.get("Geschatte Uren", 0)
            rate = item.get("Uurtarief (€)", 0)
            subtotal = hours * rate
            
            lines.append(f"| {discipline} | {hours} | €{rate} | €{subtotal:,.0f} |")
            total_hours += hours
            total_cost += subtotal
        
        lines.extend([
            f"| **TOTAAL** | **{total_hours}** | | **€{total_cost:,.0f}** |",
            "",
        ])
        
        if phases:
            lines.extend([
                "## Fase-indeling",
                "",
                "| Fase | Duur | Deliverables |",
                "|---|---|---|",
            ])
            
            for phase in phases:
                name = phase.get("name", "")
                duration = phase.get("duration", "")
                deliverables = phase.get("deliverables", "")
                lines.append(f"| **{name}** | {duration} | {deliverables} |")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_roles_responsibilities(roles: List[Dict[str, str]]) -> str:
        """Format Section 10: Roles & Responsibilities."""
        lines = [
            "",
            "---",
            "",
            "# 10. ROLES & RESPONSIBILITIES",
            "",
            "| Rol | Organisatie | Verantwoordelijkheden |",
            "|---|---|---|",
        ]
        
        for role in roles:
            title = role.get("title", "")
            organization = role.get("organization", "")
            responsibilities = role.get("responsibilities", "")
            lines.append(f"| **{title}** | {organization} | {responsibilities} |")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_sign_off() -> str:
        """Format Section 11: Aanvaarding (Sign-off section)."""
        return """

---

# 11. AANVAARDING

Dit Statement of Work beschrijft de scope, deliverables, planning en kosten voor het project.

**Goedkeuring door:**

| Rol | Naam | Datum | Handtekening |
|---|---|---|---|
| Product Owner | _____________ | _____________ | _____________ |
| Project Manager | _____________ | _____________ | _____________ |
| Customer | _____________ | _____________ | _____________ |

---

## Opmerkingen & Bijlagen

- Verdere vragen over scope: neem contact op met Product Owner
- Versie history: V1.0 - Initial SOW created - """ + datetime.now().strftime("%d/%m/%Y") + """

---

**Einde Statement of Work**
"""
    
    @staticmethod
    def build_complete_sow(metadata: Dict[str, Any]) -> str:
        """Build a complete SOW document from metadata."""
        sow = SOWTemplate.format_header(
            metadata.get("project_name", "Project"),
            metadata.get("version", "1.0"),
            metadata.get("sow_date")
        )
        
        sow += SOWTemplate.format_project_overview(metadata)
        sow += SOWTemplate.format_integration_flows(metadata.get("flows", {}))
        sow += SOWTemplate.format_scope(
            metadata.get("in_scope", []),
            metadata.get("out_of_scope", [])
        )
        sow += SOWTemplate.format_system_requirements(
            metadata.get("system_requirements", {})
        )
        sow += SOWTemplate.format_assumptions(
            metadata.get("assumptions", [])
        )
        sow += SOWTemplate.format_change_management()
        sow += SOWTemplate.format_deliverables(
            metadata.get("deliverables", [])
        )
        sow += SOWTemplate.format_acceptance_criteria(
            metadata.get("acceptance_criteria", {})
        )
        sow += SOWTemplate.format_estimation(
            metadata.get("budget_data", []),
            metadata.get("phases", [])
        )
        sow += SOWTemplate.format_roles_responsibilities(
            metadata.get("roles", [])
        )
        sow += SOWTemplate.format_sign_off()
        
        return sow


# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    example_metadata = {
        "project_name": "iLOQ Cloud Gateway Integration",
        "version": "1.0",
        "sow_date": datetime.now().strftime("%d/%m/%Y"),
        "customer": "Synguard Partners",
        "project_duration": "12 werkdagen",
        "objective": "Volledige integratie van iLOQ RF draadloze sloten",
        "short_description": "Integration via iLOQ Cloud Gateway API",
        "work_description": [
            "Bidirectionele synchronisatie",
            "Realtime logging",
            "Battery monitoring"
        ],
        "in_scope": [
            "3.1.1 Bidirectionele Synchronisatie",
            "3.1.2 Realtime Logging",
            "3.1.3 Batterijstatusweergave"
        ],
        "out_of_scope": [
            "iLOQ Manager ontwikkelingen",
            "Fysieke installatie van hardware"
        ],
        "system_requirements": {
            "Synguard Platform": [
                "Synguard Platform versie 3.0 of hoger",
                "SQL Server 2019 of hoger"
            ]
        },
        "assumptions": [
            "iLOQ Cloud Gateway API is stabiel",
            "Internetverbinding is permanent beschikbaar"
        ],
        "budget_data": [
            {"Discipline / Jira Component": "Solution Architecture & Design", "Geschatte Uren": 8, "Uurtarief (€)": 125}
        ]
    }
    
    sow_document = SOWTemplate.build_complete_sow(example_metadata)
    print(sow_document)
