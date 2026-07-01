# iLOQ CLOUD GATEWAY INTEGRATION - SOW EXAMPLE

This is a **reference example** of the standardized SOW structure used for all generated Statement of Work documents in the Synguard AI platform.

## 📋 Standard Structure

All SOW documents follow this 11-section structure (based on Eurofiber template):

1. **Project Overzicht** - Project metadata, objective, duration, short description
2. **Integratieflow** - Visual diagrams of system flows (sync, logging, monitoring)
3. **Scope** - In-scope features (detailed) + Out-of-scope items
4. **Systeemvereisten** - Platform, external system, network, dependency requirements
5. **Aannames** - Project assumptions with clear, testable statements
6. **Wijzigingsbeheer** - Change management process and templates
7. **Op te leveren resultaten** - 8+ specific deliverables with descriptions
8. **Acceptatiecriteria** - Multiple sections with ✓ checkmark criteria
9. **Inschatting** - Budget breakdown by discipline + phase timeline
10. **Roles & Responsibilities** - RACI matrix with clear assignments
11. **Aanvaarding** - Sign-off section for stakeholder approval

## 🔄 Pipeline Usage

### When SOWs Are Generated:

1. **User provides customer input** → Pipeline receives problem statement
2. **LangGraph nodes process input** → Creates CRD, technical requirements, matrix
3. **SOW generation node runs** → Uses `SOWTemplate.build_complete_sow()` 
4. **Document is formatted** → Automatically applies Eurofiber structure
5. **File is saved** → Stored in `/outputs/generated_srs/` with metadata

### When Examples Are Saved:

- All saved SOW files automatically follow the standardized structure
- Metadata is embedded in the file using `[---SPLIT-DOSSIER---]` separator
- Examples can be loaded back into the pipeline for review/modification

## 📁 File Locations

- **Template module**: `sow_template.py` (provides formatting functions)
- **Generated SOWs**: `outputs/generated_srs/` (timestamped filenames)
- **Example reference**: This file

## 🚀 Implementation in Pipeline

The template is integrated via:

```python
# In app.py or Customer_Req_doc_LangGraph.py
from sow_template import SOWTemplate

# When node_sow generates the document:
sow_document = SOWTemplate.build_complete_sow(metadata_dict)

# Save with metadata:
with open(filepath, 'w') as f:
    f.write(sow_document)
    f.write('\n[---SPLIT-DOSSIER---]\n')
    f.write(json.dumps(metadata))
```

## ✅ Quality Checks

Every generated SOW should pass:

- ✓ All 11 sections present
- ✓ Project metadata correctly populated  
- ✓ Clear in-scope vs out-of-scope distinction
- ✓ Testable acceptance criteria with checkmarks
- ✓ Budget totals calculated correctly
- ✓ All roles assigned (no blanks)
- ✓ Flows/diagrams match content

## 📊 Metadata Fields Required

The template requires these fields in the metadata dictionary:

```json
{
  "project_name": "string",
  "version": "string (e.g., '1.0')",
  "sow_date": "string (DD/MM/YYYY)",
  "customer": "string",
  "project_duration": "string",
  "objective": "string",
  "short_description": "string",
  "work_description": ["item1", "item2"],
  "in_scope": ["section with description"],
  "out_of_scope": ["item1", "item2"],
  "system_requirements": {
    "category": ["requirement1", "requirement2"]
  },
  "assumptions": ["assumption1", "assumption2"],
  "flows": {
    "Flow Name": "ASCII diagram or description"
  },
  "deliverables": [
    {"title": "...", "description": "...", "items": []}
  ],
  "acceptance_criteria": {
    "Section Name": ["✓ criterion1", "✓ criterion2"]
  },
  "budget_data": [
    {"Discipline / Jira Component": "...", "Geschatte Uren": 8, "Uurtarief (€)": 125}
  ],
  "phases": [
    {"name": "Phase 1", "duration": "2 dagen", "deliverables": "..."}
  ],
  "roles": [
    {"title": "...", "organization": "...", "responsibilities": "..."}
  ]
}
```

---

**Last Updated**: 01/07/2026  
**Status**: Reference Template v1.0  
**Compatibility**: Synguard AI Platform v1.0+
