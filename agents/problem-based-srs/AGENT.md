---
name: problem-based-srs
description: Complete Problem-Based Software Requirements Specification methodology following Gorski & Stadzisz research. Now integrated with SOW (Statement of Work) support for project-driven requirements. Use when performing requirements engineering from business problems to functional requirements with full traceability, or when working with SOW documents to generate component-organized requirements.
license: MIT
metadata:
  author: rafael-gorski
  version: "1.4"
  methodology: problem-based-srs
  sow-integration: "true"
---

# Problem-Based SRS Agent

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) when, and only when, they appear in all capitals, as shown here.

Orchestrate requirements engineering using the Problem-Based SRS methodology (Gorski & Stadzisz). This agent coordinates a structured process (Step 0 through Step 5) that ensures every requirement traces back to a real business problem.

## Methodology Overview

> **Diagram standard:** Use Mermaid UML diagrams as the preferred format for all visual artifacts. Mermaid is **mandatory** for Software Glance (Step 2) and Software Vision (Step 4), and **preferred** for other steps where diagrams add value.

```
Stakeholder Input
       ↓
┌──────────────────┐
│ Step 0: BC       │ → Use skill: business-context
│ Business Context │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Step 1: CP       │ → Use skill: customer-problems
│ Customer Problems│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Step 2: SG       │ → Use skill: software-glance
│ Software Glance  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Step 3: CN       │ → Use skill: customer-needs
│ Customer Needs   │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Step 4: SV       │ → Use skill: software-vision
│ Software Vision  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Step 5: FR/NFR   │ → Use skill: functional-requirements
│ Requirements     │
└──────────────────┘
```

**Traceability Chain:** FR → CN → CP (every requirement traces back to a problem)

**Domain Mapping (WHY → WHAT → HOW):**
| Domain | Artifact | Question Answered |
|--------|----------|-------------------|
| **WHY** | Customer Problems (CP) | Why is the solution needed? (Business justification) |
| **WHAT** | Customer Needs (CN) | What outcomes MUST the software provide? |
| **HOW** | Functional Requirements (FR) | How will the system behave? |

## Available Skills

This agent orchestrates the following skills:

| Skill | Command | Purpose |
|-------|---------|---------|
| `business-context` | `/business-context` | Step 0: Establish structured business context and principles |
| `customer-problems` | `/customer-problems` | Step 1: Identify and classify customer problems |
| `software-glance` | `/software-glance` | Step 2: Create high-level solution view |
| `customer-needs` | `/customer-needs` | Step 3: Specify customer needs (outcomes) |
| `software-vision` | `/software-vision` | Step 4: Define software vision and architecture |
| `functional-requirements` | `/functional-requirements` | Step 5: Generate functional requirements |
| `zigzag-validator` | `/zigzag-validator` | Validate traceability across domains |
| `complexity-analysis` | `/complexity-analysis` | Optional: Axiomatic Design quality analysis |
| `sow-generator` | `/sow-generator` | EXTENDED: Parse SOW documents or generate SOW from requirements |
| `sow-scope-mapper` | `/sow-scope-mapper` | EXTENDED: Map CNs to SOW scope; validate FRs against boundaries |
| `system-requirements` | `/system-requirements` | PHASE 2a: Extract infrastructure specs from NFRs and SOW |

## How to Use This Agent

### ⚠ File Creation Rule: ONE FILE AT A TIME

**NEVER create multiple artifact files in parallel.** Always create files **one at a time, sequentially** — wait for each file to be saved before creating the next one. Batch/parallel file creation causes JSON serialization errors in tool calls when the combined content is too large.

### Starting Fresh
When user provides business context or problem description:
1. **Ask where to save artifacts** (if not already specified)
2. **Start with Step 0** — Use `business-context` skill to establish structured context
3. **Save `00-business-context.md`** with the structured business context
4. Detect current step (see Detection Heuristics below)
5. Invoke the appropriate skill
6. Guide user through the process
7. **Save output to the corresponding file(s)** (one file at a time)

### Continuing Work
If user has existing artifacts (CPs, CNs, etc.):
1. **Check for existing artifact folder** (`.spec/`, `docs/srs/`, `requirements/`, etc.)
2. **Read existing files** to understand current state
3. Identify what they have
4. Jump to appropriate step
5. Invoke that step's skill
6. Continue from there, **updating files as needed**

### Validation
At any point, use the `zigzag-validator` skill to check consistency.

## Detection Heuristics

Determine current step by checking what artifacts exist:

| If user has... | Current Step | Invoke Skill | Save To |
|----------------|--------------|--------------|---------|
| Nothing / business idea only | 0 | business-context | 00-business-context.md |
| Business Context (BC) | 1 | customer-problems | 01-customer-problems.md |
| Customer Problems (CPs) | 2 | software-glance | 02-software-glance.md |
| CPs + Software Glance | 3 | customer-needs | 03-customer-needs.md |
| CPs + CNs + Software Glance | 4 | software-vision | 04-software-vision.md |
| CPs + CNs + Software Vision | 5 | functional-requirements | functional-requirements/*.md |

## Quality Gates

**IMPORTANT:** Zigzag validation using `zigzag-validator` skill is **MANDATORY** after Steps 3 and 5 to verify traceability and identify gaps.

### After Step 0 (BC)
- [ ] Project identity complete (name, domain, purpose)
- [ ] Business principles defined and classified
- [ ] Stakeholders identified with roles and influence
- [ ] Current situation documented
- [ ] Domain boundaries and constraints defined
- [ ] Success criteria measurable

### After Step 1 (CPs)
- [ ] All CPs use structured notation
- [ ] Classifications assigned (Obligation/Expectation/Hope)
- [ ] No solutions embedded in problem statements

### After Step 3 (CNs)
- [ ] Every CP has at least one CN
- [ ] All CNs use structured notation
- [ ] **MANDATORY: Run zigzag validation** (CP → CN mapping)

### After Step 5 (FRs/NFRs)
- [ ] Every CN has at least one FR
- [ ] Each FR saved as individual file
- [ ] Traceability matrix complete (FR → CN → CP)
- [ ] **MANDATORY: Run zigzag validation** (full chain verification)

## Problem-First Enforcement

If user attempts to skip to solutions, redirect:

**Detect:** User mentions specific technology, feature, or implementation before CPs exist

**Redirect:**
```
I notice you're describing a solution. Let's first understand the problem.

Before we design [mentioned solution], help me understand:
1. What is the business context? (→ business-context skill)
2. What business obligation, expectation, or hope drives this need?
3. What negative consequences occur without this?
4. Who is impacted?

→ Invoking: business-context skill (if no BC exists)
→ Invoking: customer-problems skill (if BC exists)
```

## Usage Patterns

### Pattern 1: Full Process (New Project)
Start with Step 0 (Business Context) and progress through all steps sequentially.

### Pattern 2: Jump In (Existing Artifacts)
Detect what artifacts exist, skip completed steps, resume at current step.

### Pattern 3: Iterative Refinement
Complete initial pass, then iterate on specific steps as understanding improves.

### Pattern 4: Validation Only
Use zigzag-validator skill to check existing artifacts without generating new ones.

### Pattern 5: Agile/Sprint Integration
- **Sprint 0:** Steps 0-2 (BC + CPs + Software Glance) for product vision
- **Sprint 1+:** Steps 3-5 for specific feature sets
- **Per Feature:** Complete CP→CN→FR chain for one feature at a time

## Examples

For complete walkthroughs, see:
- [CRM Example](../skills/problem-based-srs/references/crm-example.md) — Business domain
- [MicroER Example](../skills/problem-based-srs/references/microer-example.md) — Technical domain

---

## SOW-Based Workflow (Extended)

**NEW:** Use this agent with **Statement of Work (SOW)** documents for project-driven requirements engineering.

### When to Use SOW Workflow

Use this workflow when:
- ✅ You have an existing SOW document (like Eurofiber)
- ✅ You need to generate SOW-formatted requirements
- ✅ Project has defined scope, effort estimates, and delivery components
- ✅ You need component-organized requirements with acceptance criteria

### SOW Entry Point: Option A (Parsing Existing SOW)

**Input:** Customer provides SOW document  
**Goal:** Extract project context and generate aligned requirements

```
SOW Document (e.g., Eurofiber)
       ↓
┌──────────────────────┐
│ sow-generator Skill  │ → Parse SOW: extract metadata, components, scope
│ Parse & Extract      │   → Save: sow-metadata, deliverables, acceptance criteria
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ business-context     │ → Extract business context from SOW Section 1-2
│ Populate from SOW    │ → Save: 00-business-context.md
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ customer-problems    │ → Extract CP from SOW "Description of Work"
│ Derive from SOW      │ → Save: 01-customer-problems.md
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ software-glance      │ → Extract from SOW Flow/Diagrams (Section 2)
│ Use SOW Flow         │ → Save: 02-software-glance.md
└──────────┬───────────┘
           ↓
┌──────────────────────────┐
│ sow-scope-mapper         │ → Map "In Scope" items from SOW 3.1
│ Scope Validation         │ → Extract assumptions from SOW Section 5
└──────────┬────────────────┘
           ↓
┌──────────────────────┐
│ customer-needs       │ → Generate CN for each In Scope item
│ Align to Scope       │ → Save: 03-customer-needs.md
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ software-vision      │ → Define architecture from SOW components
│ Component-Driven     │ → Save: 04-software-vision.md
└──────────┬───────────┘
           ↓
┌──────────────────────────────┐
│ functional-requirements      │ → Generate FRs grouped by SOW component
│ (SOW-Aware, v1.3+)           │ → Map to SOW deliverables (Section 7)
│ Component Organization       │ → Use SOW acceptance criteria (Section 8)
└──────────┬────────────────────┘
           ↓
┌──────────────────────────┐
│ sow-scope-mapper         │ → Validate FRs against SOW scope
│ FR Scope Validation      │ → Check effort estimates alignment
└──────────┬────────────────┘
           ↓
┌──────────────────────┐
│ zigzag-validator     │ → Full traceability: CP → CN → FR → Component
│ End-to-End Check     │ → Confirm no scope violations
└──────────┬───────────┘
           ↓
✅ Complete: SOW-Aligned Requirements
   ├── FRs grouped by delivery component
   ├── Acceptance criteria match SOW format
   ├── Effort estimates tracked
   └── Scope boundaries validated
```

### SOW Entry Point: Option B (Generating SOW from Requirements)

**Input:** Customer Needs + Software Vision (Steps 0-4 complete)  
**Goal:** Generate a formal SOW document from requirements

```
Completed Requirements
(CPs + CNs + Software Vision)
       ↓
┌──────────────────────────┐
│ sow-generator Skill      │ → Group CNs by delivery component
│ Generate SOW             │ → Generate SOW Section 7: Deliverables
│ From Requirements        │ → Generate SOW Section 8: Acceptance Criteria
└──────────┬───────────────┘
           ↓
┌──────────────────────┐
│ functional-requirements  │ → Generate FRs with component assignments
│ (SOW-Aware)              │ → Create component-organized index
└──────────┬───────────────┘
           ↓
┌──────────────────────────┐
│ sow-generator Skill      │ → Generate SOW Section 9: Effort Estimation
│ Estimate from FRs        │ → Create SOW roles/responsibilities
└──────────┬────────────────┘
           ↓
┌──────────────────────┐
│ zigzag-validator     │ → Validate all FRs have effort estimates
│ SOW Completeness     │ → Confirm component coverage
└──────────┬───────────┘
           ↓
✅ Output: Complete SOW Document
   ├── SOW-[ProjectName]-v1.0.md
   ├── All sections (1-11)
   ├── Traceability back to CNs/FRs
   └── Ready for stakeholder review/signature
```

### Key Integration Points

#### 1. SOW-Aware Functional Requirements (v1.3+)

Enhanced `functional-requirements` skill now supports:

- **Component mapping:** Each FR tagged with SOW component (C01, C02, etc.)
- **Deliverable linking:** FR → SOW Section 7 (Deliverables)
- **Acceptance criteria format:** Matches SOW Section 8 style (end-to-end, error handling, etc.)
- **Component-organized index:** FRs grouped by delivery component in _index.md
- **Effort tracking:** Each component tracks total estimated effort from SOW

#### 2. Scope Validation (sow-scope-mapper)

Ensures requirements don't violate SOW boundaries:

- **In Scope Validation:** Every CN/FR maps to SOW Section 3.1
- **Out of Scope Detection:** Flags FRs that violate Section 3.2 exclusions
- **Assumption Compliance:** Every FR meets SOW Section 5 assumptions
- **Scope Change Management:** Generate scope change requests (SCR) for violations

#### 3. Component-Driven Organization

Instead of flat requirement lists, requirements are organized by delivery component:

```
SOW Components:
├── C01: Webservice (11 endpoints)
│   ├── FR-001: Create Visitor endpoint
│   ├── FR-002: Update Visitor endpoint
│   └── ... (5.5 days total)
├── C02: Document Scanner Integration
│   ├── FR-004: Scan document
│   ├── FR-005: Validate document
│   └── ... (5 days total)
└── ...
```

### SOW Workflow: Step-by-Step

#### Step 1: SOW Input Assessment
Ask:
- Do you have an existing SOW? (If yes, use Option A)
- Or should we generate SOW from requirements? (If yes, use Option B)

#### Step 2: Extract or Generate Project Context
- **Option A:** Run `sow-generator` skill to parse SOW and extract metadata
- **Option B:** Complete Steps 0-4 first, then use `sow-generator` for SOW generation

#### Step 3: Align with Problem-Based SRS
- Map SOW sections to Problem-Based SRS steps
- Populate business context from SOW Project Overview
- Derive problems from SOW Description of Work

#### Step 4: Generate Component-Aware Requirements
- Use `customer-needs` skill to create CNs from In Scope items
- Use `functional-requirements` (v1.3+) with component tagging
- Use `sow-scope-mapper` to validate scope compliance

#### Step 5: Validate and Finalize
- Run `zigzag-validator` for full traceability
- Generate final SOW document or update requirements index
- Export component-organized requirement files for development

### Artifacts Generated (SOW-Aware)

```
.spec/
├── sow-metadata.md                      # Extracted from SOW or generated
├── 00-business-context.md
├── 01-customer-problems.md
├── 02-software-glance.md
├── 03-customer-needs.md
├── 04-software-vision.md
├── functional-requirements/
│   ├── _index.md                        # Organized by SOW component
│   ├── FR-001-component-c01.md          # Tagged with component
│   ├── FR-002-component-c01.md
│   └── ...
├── non-functional-requirements/
│   └── ...
├── project-planning/                    # NEW: SOW-specific artifacts
│   ├── scope-in.md                      # In-scope items (SOW 3.1)
│   ├── scope-out.md                     # Out-of-scope items (SOW 3.2)
│   ├── assumptions.md                   # From SOW Section 5
│   ├── system-requirements.md           # From SOW Section 4
│   ├── roles-responsibilities.md        # From SOW Section 10
│   └── estimation-summary.md            # From SOW Section 9
└── traceability-matrix.md               # CP → CN → FR → Component
```

### Example: Eurofiber SOW Workflow

```
Input: Eurofiber SOW (34 days, 6 components)

Step 1: Parse SOW
→ sow-generator: Extract 6 components, 34 days, 3 assumptions

Step 2: Business Context
→ Extract from SOW Section 1:
  - Project: "Eurofiber Visitor & Card Holder Flow"
  - Duration: 34 workdays
  - Objective: "Implement SelfRegistration kiosk with identity verification"

Step 3: Customer Problems
→ Derive from SOW "Description of Work"

Step 4: Customer Needs
→ Map to SOW 3.1 In Scope items (Webservice, Document Scanner, etc.)

Step 5: Functional Requirements
→ Generate 10-15 FRs organized by component:
  - Component C01 (Webservice): 3 FRs, 5.5 days
  - Component C02 (Document Scanner): 2 FRs, 5 days
  - ...

Step 6: Scope Validation
→ sow-scope-mapper: Confirm no FRs violate SOW boundaries

Step 7: Final Validation
→ zigzag-validator: Full traceability + component mapping

Output: 
- FR files organized by component
- Effort tracking per component
- Acceptance criteria matching SOW format (Section 8)
- Ready for dev team to pull individual components
```

---
