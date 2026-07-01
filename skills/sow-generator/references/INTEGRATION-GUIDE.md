# SOW-Problem-Based SRS Integration Guide

## Overview

The Problem-Based SRS methodology has been **extended with Statement of Work (SOW) support** to enable project-driven requirements engineering. This guide explains how the components work together.

---

## What Changed

### Phase 1 Implementation (Current)

| Component | Version | Change |
|-----------|---------|--------|
| **Problem-Based SRS Agent** | 1.4 (↑ from 1.3) | Added SOW workflow documentation and component integration |
| **Functional Requirements Skill** | 1.3 (↑ from 1.2) | Added SOW acceptance criteria format, component tagging, component-aware index |
| **NEW: SOW Generator Skill** | 1.0 | Parse SOW documents or generate SOW from requirements |
| **NEW: SOW Scope Mapper Skill** | 1.0 | Map CNs to scope, validate FR scope compliance, formalize assumptions |

### Backward Compatible

✅ **ALL existing workflows still work** — SOW integration is optional
- Original Problem-Based SRS Steps 0-5 unchanged
- Existing FR generation works as before
- New SOW capabilities are additive

---

## Three Workflows

### Workflow 1: Pure Problem-Based SRS (Original)
**Use when:** No SOW exists or requirements-only approach

```
Problem → Business Context → Customer Problems → Customer Needs 
                                                      ↓
                            Software Glance → Software Vision → FRs/NFRs
```

**Output:** Flat requirement list with full traceability  
**Tools:** Steps 0-5 + zigzag-validator

---

### Workflow 2: SOW → Requirements (NEW)
**Use when:** You have an existing SOW document

```
SOW Document
     ↓
sow-generator: Parse & extract metadata, components, scope
     ↓
Business Context + Customer Problems + Customer Needs
     ↓
sow-scope-mapper: Validate scope boundaries
     ↓
Functional Requirements (component-organized)
     ↓
zigzag-validator: Full traceability + scope validation
```

**Input:** SOW document (e.g., Eurofiber)  
**Output:** Requirements organized by delivery component  
**Tools:** sow-generator + traditional steps + sow-scope-mapper + zigzag-validator  
**Benefit:** Requirements automatically aligned with project scope and components

---

### Workflow 3: Requirements → SOW (NEW)
**Use when:** You have CNs/Software Vision and need to generate SOW

```
Steps 0-4 Complete (BC + CPs + CNs + SV)
     ↓
sow-generator: Group CNs into components, generate SOW sections 7-9
     ↓
functional-requirements: Generate FRs with component tags and effort estimates
     ↓
sow-scope-mapper: Validate component assignments and scope
     ↓
sow-generator: Produce complete SOW document
```

**Input:** Complete Problem-Based SRS artifact set  
**Output:** Professional SOW document  
**Tools:** sow-generator + functional-requirements (v1.3+) + sow-scope-mapper  
**Benefit:** Generate formal project SOW from structured requirements

---

## Key Concepts

### Delivery Component
**Definition:** A logically-related group of requirements delivered as a unit

**Example (Eurofiber):**
- C01: Webservice (11 endpoints)
- C02: Document Scanner Integration
- C03: Auto-Remove Mechanism
- C04: Visitor Select Rule
- C05: BioStation Integration
- C06: SIP Call Integration

**In Requirements:** Each FR tagged with component ID (C01, C02, etc.)

### Component-Organized Index
**New artifact in Step 5 output:**

```
functional-requirements/_index.md

Organized by component instead of flat list:

## Component C01: Webservice (5.5 days)
- FR-001: Create Visitor endpoint
- FR-002: Update Visitor endpoint
- FR-003: Get All Visitors endpoint
- ...
Total: 3 FRs, 5.5 days

## Component C02: Document Scanner (5 days)
- FR-004: Scan document
- FR-005: Validate document type
- ...
```

### SOW-Style Acceptance Criteria
**New format in Step 5 FR files:**

Instead of just unit-level criteria:
```
- [ ] System accepts valid input
- [ ] System rejects invalid input
```

Now includes end-to-end scenarios matching SOW Section 8:
```
- [ ] User can initiate document scan via kiosk UI without errors
- [ ] System validates document type (eID / paspoort / rijbewijs)
- [ ] When enrollment fails, fallback screen appears with dispatch instructions
- [ ] System handles 100 concurrent visitors without performance degradation
```

### Scope Mapping
**New validation step:**

Each CN/FR must map to:
- SOW Section 3.1 (In Scope) ✅ or 3.2 (Out of Scope) ❌
- A delivery component (C01-C06)
- SOW Section 5 assumptions (dependencies)
- SOW Section 9 effort estimate

**Violations flagged as:**
- ⚠️ OUT OF SCOPE — Requires scope change request
- ⚠️ MISSING EFFORT — Cannot complete project budget
- ⚠️ ASSUMPTION RISK — Requirement depends on unconfirmed assumption

---

## New Skills: Quick Reference

### sow-generator Skill

**Purpose:** Parse SOW documents or generate SOW from requirements

**Input Options:**
- Existing SOW document (e.g., Eurofiber)
- Customer Needs + Software Vision (generate new SOW)

**Output:**
- SOW metadata (project name, duration, components)
- Component inventory with effort estimates
- Scope summary (in/out of scope)
- Assumptions and constraints
- Role assignments
- OR: Complete SOW document (v1.0)

**Key Operations:**
1. **Parse SOW:** Extract 6-10 structured sections
2. **Identify Components:** Find all delivery units
3. **Map to SRS:** Link SOW sections to Problem-Based SRS steps
4. **Extract Assumptions:** Formalize SOW Section 5 as constraints
5. **Estimate Effort:** Calculate total from component estimates

---

### sow-scope-mapper Skill

**Purpose:** Ensure requirements stay within SOW scope boundaries

**Input:**
- SOW metadata (from sow-generator)
- Customer Needs (Step 3)
- Functional Requirements (Step 5)

**Validation Checks:**
1. **In-Scope Mapping:** Does each CN map to SOW 3.1?
2. **Out-of-Scope Detection:** Are any FRs in SOW 3.2?
3. **Assumption Compliance:** Does each FR meet SOW 5 assumptions?
4. **Effort Estimation:** Is every FR estimated in SOW 9?
5. **Component Assignment:** Does every FR belong to a component?

**Output:**
- Scope compliance matrix
- Violation report with recommendations
- Scope change request template (if violations found)
- Assumption-to-constraint mapping
- Verification checklist

**Key Operations:**
1. **Map CNs to Scope:** Create CN → SOW section mapping
2. **Validate FRs:** Check each FR against scope boundaries
3. **Flag Violations:** Generate issue list with severity
4. **Generate SCRs:** Create scope change request templates for out-of-scope items
5. **Formalize Constraints:** Convert assumptions to requirement constraints

---

## Integration Points

### 1. Business Context (Step 0)
**SOW input:** Project Overview (SOW Section 1)
- Project name, duration, objective
- Key stakeholders
- Success metrics

### 2. Customer Problems (Step 1)
**SOW input:** Description of Work (SOW Section 2)
- Extract pain points from work description
- Identify customer gaps

### 3. Software Glance (Step 2)
**SOW input:** Flow diagrams (SOW Section 2)
- Use SOW flow diagrams as visual reference
- Identify main components

### 4. Customer Needs (Step 3)
**SOW input:** In Scope items (SOW Section 3.1)
- Map each in-scope item to a CN
- Exclude out-of-scope items (Section 3.2)
- Incorporate constraints from Section 5

### 5. Software Vision (Step 4)
**SOW input:** Component structure (SOW Section 7)
- Organize architecture around delivery components
- Define component boundaries from SOW

### 6. Functional Requirements (Step 5)
**SOW input:** Deliverables + Acceptance Criteria (SOW Sections 7-8)
- Generate FRs per component
- Map to SOW deliverables (Section 7)
- Use SOW acceptance criteria format (Section 8)
- Tag with component and effort estimate (Section 9)

### 7. Validation (Ongoing)
**SOW input:** Scope boundaries (SOW Sections 3.1, 3.2, 5)
- sow-scope-mapper validates scope compliance
- Flags violations for scope change management

---

## Artifact Structure (SOW-Aware)

### Standard Problem-Based SRS
```
.spec/
├── 00-business-context.md
├── 01-customer-problems.md
├── 02-software-glance.md
├── 03-customer-needs.md
├── 04-software-vision.md
├── functional-requirements/
│   ├── _index.md
│   ├── FR-001.md
│   └── ...
├── non-functional-requirements/
│   └── ...
└── traceability-matrix.md
```

### SOW-Integrated (Extended)
```
.spec/
├── sow-metadata.md                    # Extracted/generated SOW context
├── 00-business-context.md
├── 01-customer-problems.md
├── 02-software-glance.md
├── 03-customer-needs.md
├── 04-software-vision.md
├── functional-requirements/
│   ├── _index.md                      # Organized by component!
│   ├── FR-001-component-c01.md        # Tagged with component
│   ├── FR-002-component-c01.md
│   └── ...
├── non-functional-requirements/
│   └── ...
├── project-planning/                  # NEW: SOW artifacts
│   ├── scope-in.md                    # In-scope items (SOW 3.1)
│   ├── scope-out.md                   # Out-of-scope items (SOW 3.2)
│   ├── assumptions.md                 # Constraints from SOW 5
│   ├── system-requirements.md         # Infrastructure (SOW 4)
│   ├── roles-responsibilities.md      # Ownership (SOW 10)
│   └── estimation-summary.md          # Effort breakdown (SOW 9)
├── traceability-matrix.md             # Includes component column
└── scope-compliance.md                # Validation report from sow-scope-mapper
```

---

## Usage: By Role

### Product Manager
**Workflow:** SOW → Requirements (Workflow 2)

1. Provide existing SOW document to AI agent
2. Agent parses SOW using `sow-generator`
3. Reviews extracted components, scope, assumptions
4. Agent generates CNs aligned with scope
5. Result: Requirements organized by project component, ready for dev team

**Benefit:** Your SOW scope automatically enforced in requirements

---

### Requirements Engineer
**Workflow:** Requirements → SOW (Workflow 3)

1. Complete Steps 0-4 (BC, CPs, CNs, SV)
2. Use `functional-requirements` (v1.3+) to generate component-organized FRs
3. Use `sow-scope-mapper` to validate scope boundaries
4. Use `sow-generator` to create formal SOW document
5. Result: Professional SOW with full requirement traceability

**Benefit:** SOW auto-generated from validated requirements

---

### Project Manager
**Use:** Scope Compliance Monitoring

1. Use `sow-scope-mapper` to validate FRs against project scope
2. Tool flags scope creep and out-of-scope requests
3. Generate scope change requests (SCRs) for scope violations
4. Monitor effort estimates via component-organized index
5. Track component completion against SOW estimates

**Benefit:** Real-time scope and effort tracking

---

### Development Team
**Use:** Component-Organized Requirements

1. Receive FRs organized by delivery component (from Step 5 _index.md)
2. Each component shows: effort estimate, acceptance criteria, dependencies
3. Pick individual component to implement
4. Acceptance criteria match SOW format (Section 8) for validation

**Benefit:** Work on focused components with clear effort/success metrics

---

## Example: Eurofiber Integration

### Original Challenge
- Eurofiber SOW: 34 days, 6 components, complex scope
- Traditional approach: Translate SOW to generic requirements manually
- Problem: Requirements disconnected from project context; scope creep risk

### SOW-Integrated Solution

**Step 1: Parse Eurofiber SOW**
```
sow-generator: Parse Eurofiber SOW v3.03
→ Extract 6 components (Webservice, Document Scanner, etc.)
→ Extract 34-day estimate
→ Extract 3 assumptions (8x8 SIP, firmware stability, network connectivity)
```

**Step 2: Generate Problem-Based SRS**
```
business-context: Extract from SOW Section 1
→ Project: "Eurofiber Visitor & Card Holder Flow"
→ Objective: "Implement SelfRegistration kiosk with biometric enrollment"
→ Timeline: 34 days

customer-needs: Extract from SOW Section 3.1
→ 6 CNs (one per component)
→ Exclude items in SOW 3.2 (PowerApp, hardware, network)

functional-requirements (v1.3+):
→ Generate 10-15 FRs organized by component
→ C01: 3 FRs (5.5 days) → Webservice endpoints
→ C02: 2 FRs (5 days) → Document Scanner
→ C03: 1 FR (0.5 days) → Auto-Remove
→ C04: 1 FR (3 days) → Visitor Select Rule
→ C05: 2 FRs (10 days) → BioStation Integration
→ C06: [FRs] → SIP Call Integration
```

**Step 3: Validate Scope Compliance**
```
sow-scope-mapper:
→ Check: All FRs in SOW Section 3.1 (In Scope)? ✅ YES
→ Check: All assumptions documented (SOW Section 5)? ✅ YES
→ Check: All FRs have effort estimates? ✅ YES
→ Check: Total effort = 34 days? ✅ CONFIRMED

Result: 0 violations, scope validated
```

**Step 4: Dev Team Receives**
```
functional-requirements/_index.md:

Component C01: Webservice (5.5 days)
├── FR-001: Create Visitor endpoint
├── FR-002: Update Visitor endpoint
└── ... (3 FRs total)

Component C02: Document Scanner (5 days)
├── FR-004: Scan and validate document
└── ... (2 FRs total)

[Each FR file includes:]
- Acceptance criteria in SOW format (Section 8 style)
- Links to deliverables (SOW Section 7)
- Effort estimate (SOW Section 9)
- Component assignment (C01-C06)
```

**Result:** 
✅ Requirements match SOW structure  
✅ Scope boundaries enforced automatically  
✅ Dev team gets component-organized work packages  
✅ Effort tracking built-in  

---

## Migration Path: Adding SOW to Existing Projects

### If You Have Existing FRs (Pre-v1.3)

1. **Get your SOW document** (or existing project definition)
2. **Run sow-scope-mapper** against existing FRs
3. **Tool outputs:** Scope violations, missing estimates, component assignments
4. **Manually update FR files** to add:
   - Component tag (C01, C02, etc.)
   - Scope status (✅ In / ❌ Out)
   - Effort estimate (days)
5. **Regenerate _index.md** with component organization
6. **Run zigzag-validator** to confirm traceability

---

## What's NOT Changing

✅ **Steps 0-5 core methodology** — 100% compatible  
✅ **Traceability (CP → CN → FR)** — Enhanced, not replaced  
✅ **Acceptance criteria quality** — Higher with end-to-end scenarios  
✅ **Problem-first approach** — Still enforced  
✅ **Individual FR files** — Still created separately  
✅ **Team collaboration** — Now organized by component  

---

## Quick Decision Tree

**Do you have a SOW document?**

→ **YES:** Use Workflow 2 (SOW → Requirements)  
   1. Run sow-generator to parse
   2. Follow traditional Steps 0-5
   3. Use sow-scope-mapper for validation
   4. Result: Component-organized FRs

→ **NO:** Do you need to create one?

   → **YES:** Use Workflow 3 (Requirements → SOW)
      1. Complete Steps 0-4
      2. Run functional-requirements (v1.3+)
      3. Run sow-generator to create SOW
      4. Result: Professional SOW document

   → **NO:** Use traditional Workflow 1 (Pure Problem-Based SRS)
      1. Run Steps 0-5 as normal
      2. Result: Requirements with full traceability
      3. (SOW features available if you decide to use them later)

---

## Phase 2: Project Planning (Extended)

**After completing Phase 1 (Requirements), Phase 2 extends with project planning skills:**

| Phase 2 Skill | Purpose | When to Use |
|---|---|---|
| **System Requirements (2a)** | Extract infrastructure & software stack from NFRs + SOW Section 4 | After Step 5, before estimation |
| **Assumptions & Constraints (2b)** | Identify risks from SOW Section 5 + dependencies | After system requirements |
| **Estimation (2c)** | Calculate effort, timeline, resources | After dependencies identified |
| **Roles & Responsibilities (2d)** | Assign team members and responsibilities | Before project kickoff |

### Phase 2a: System Requirements (NOW AVAILABLE)

**Skill:** `system-requirements` (`/skills/system-requirements/SKILL.md`)

**Input:** Non-Functional Requirements (NFRs) + Software Vision + SOW Section 4

**Output:**
- Infrastructure specification (compute, storage, network, software stack)
- Performance baselines (testable metrics from NFRs)
- Deployment environment specs (dev, staging, production)
- External dependencies & risks

**Example:** [Eurofiber System Requirements](../../system-requirements/references/EUROFIBER-EXAMPLE.md)

**Feeds Into:**
- Estimation (Phase 2c): Infrastructure setup effort
- Development: Dev environment configuration
- Operations: Provisioning and deployment

---

## Support & References

- **SOW Generator Skill:** `/skills/sow-generator/SKILL.md`
- **SOW Scope Mapper Skill:** `/skills/sow-scope-mapper/SKILL.md`
- **Functional Requirements (v1.3+):** `/skills/functional-requirements/SKILL.md` — See "SOW Integration" section
- **Problem-Based SRS Agent (v1.4):** `/agents/problem-based-srs/AGENT.md` — See "SOW-Based Workflow" section
- **System Requirements (Phase 2a):** `/skills/system-requirements/SKILL.md` — Infrastructure & software stack
- **System Requirements Example:** `/skills/system-requirements/references/EUROFIBER-EXAMPLE.md`
