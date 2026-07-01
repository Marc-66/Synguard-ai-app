---
name: sow-generator
description: Extract, parse, and transform Statement of Work (SOW) documents into structured project artifacts. Converts between customer SOW input and Problem-Based SRS components. Generates SOW-formatted output from requirements. Use when working with SOW documents to enable component-driven project planning with full requirement traceability.
license: MIT
metadata:
  author: synguard-ai
  version: "1.0"
  methodology: problem-based-srs-extended
  integration: sow-based-requirements
---

# SOW Generator

> Generate and parse Statement of Work (SOW) documents with full requirement traceability and project context.

## Purpose

This skill bridges **Problem-Based SRS methodology** with **real-world project management** by:

1. **Parsing SOW documents** into structured components
2. **Extracting project metadata** (scope, assumptions, effort, roles)
3. **Generating SOW-formatted requirements** from Customer Needs and Functional Requirements
4. **Creating bidirectional mapping** between Problem-Based SRS artifacts and SOW sections

## When to Use

Use this skill when:
- ✅ You have an existing SOW document (like Eurofiber)
- ✅ You need to generate a SOW from requirements
- ✅ You want to map requirements to deliverable components
- ✅ You need to structure project effort estimates
- ✅ You need to clarify scope boundaries (in/out of scope)

Do NOT use when:
- ❌ Working only on requirements without project context
- ❌ You haven't completed Customer Problems → Customer Needs yet

---

## Task: Parse an Existing SOW

If user provides an existing SOW document:

### 1. Extract and Organize SOW Metadata

Create a structured summary with these sections:

```markdown
## SOW Metadata

| Field | Value |
|-------|-------|
| **Project Name** | [From SOW Section 1] |
| **Client** | [End client] |
| **SOW Date** | [Creation/version date] |
| **Estimated Duration** | [Workdays/timeline] |
| **Project Objective** | [1-2 sentence summary] |
| **Key Deliverables Count** | [Number of major components] |
```

### 2. Map SOW Sections to Business Context

Extract and structure:

| SOW Section | Maps To | Content |
|-------------|---------|---------|
| Project Overview (1) | Business Context | Objective, scope, key metrics |
| Description of Work | Customer Problems | Pain points, current gaps |
| Flow/Diagrams (2) | Software Glance | High-level system design |
| Scope - In (3.1) | Customer Needs | What system MUST deliver |
| Scope - Out (3.2) | Scope Boundaries | What is explicitly excluded |
| System Requirements (4) | NFRs | Infrastructure, environment |
| Assumptions (5) | CN Constraints | Dependencies, prerequisites |
| Deliverables (7) | Component Groups | Organized by delivery unit |
| Acceptance Criteria (8) | FR Acceptance | How to test each component |
| Estimation (9) | Effort Allocation | Days per component |
| Roles (10) | Stakeholder Map | Responsibilities and ownership |

### 3. Identify Components

List all major delivery components from SOW:

```markdown
## Delivery Components

| ID | Component | SOW Section | Estimated Effort | Status |
|----|-----------|-------------|------------------|--------|
| C01 | [Name] | [Section reference] | [Days] | Not Started |
| C02 | [Name] | [Section reference] | [Days] | Not Started |
| ... | ... | ... | ... | ... |

**Total Estimated Effort:** [Sum] days
```

### 4. Extract Acceptance Criteria by Component

For each component in SOW Section 8:

```markdown
## Component C01: [Name]

### Deliverables (Section 7)
- [Bullet list from SOW Section 7]

### Acceptance Criteria (Section 8)
- [ ] Criterion 1 (SOW 8.X)
- [ ] Criterion 2 (SOW 8.X)
- [ ] ...

### Effort Estimation
- Estimated: [X days] (SOW Section 9)
```

### 5. Identify Out-of-Scope and Assumptions

Extract from SOW Sections 3.2, 5:

```markdown
## Out of Scope

- [Item] (SOW 3.2)
- [Item] (SOW 3.2)

## Assumptions & Constraints

- Assumption: [Description] (SOW 5)
- Constraint: [Description] (SOW 4 or 5)
- Dependency: [Description] (SOW 5)
```

---

## Task: Generate SOW from Requirements

If user has Customer Needs (CNs) and Functional Requirements (FRs):

### 1. Group FRs by Delivery Component

```markdown
## Delivery Components (Generated from FRs)

### Component: [Name]
**Related CNs:** CN-001, CN-003  
**Related FRs:** FR-001, FR-002, FR-005

#### Deliverables
- [Derived from FR descriptions]
- [Derived from FR descriptions]

#### Acceptance Criteria
- [ ] [Criterion from FR acceptance criteria]
- [ ] [Criterion from FR acceptance criteria]

#### Estimated Effort
- Analysis: [X days]
- Development: [X days]
- Testing: [X days]
- **Total: [X] days**
```

### 2. Generate SOW Section 7: Deliverables

Create section modeled on Eurofiber format:

```markdown
# 7. OP TE LEVEREN RESULTATEN / DELIVERABLES

## 7.1 Component Name
- Implementation of [technical details from FRs]
- API documentation (Swagger if applicable)
- Configuration & setup
- Testing & validation
- Error handling & logging

## 7.2 Component Name
- [Deliverables specific to this component]

## [Continue for each component]
```

### 3. Generate SOW Section 8: Acceptance Criteria

```markdown
# 8. ACCEPTATIECRITERIA / ACCEPTANCE CRITERIA

## 8.1 Component Name
- [ ] Acceptance criterion 1 (end-to-end test)
- [ ] Acceptance criterion 2 (error handling)
- [ ] Acceptance criterion 3 (performance/quality)
- [ ] Acceptance criterion 4 (security/compliance if applicable)

## 8.2 Component Name
- [ ] [Component-specific criteria]

## [Continue for each component]
```

### 4. Create Effort Estimation Table

```markdown
# 9. INSCHATTING / ESTIMATION

| Category | Item | Estimation (days) |
|----------|------|-------------------|
| Component 1 | Subtask 1 | 0.5 |
| | Subtask 2 | 1.5 |
| | Subtask 3 | 2.0 |
| Component 2 | Subtask 1 | 3.0 |
| | ... | ... |
| Overhead | Analysis, testing, coordination | 2.0 |
| **TOTAL** | | **X days** |
```

### 5. Generate Roles & Responsibilities

```markdown
# 10. ROLES & RESPONSIBILITIES

| Role | Responsibility |
|------|-----------------|
| Product Owner | Backlog prioritization, stakeholder liaison |
| Chief Technology Officer | Technical decisions, process support |
| Development Team | Design, implementation, testing |
| QA Team | Acceptance testing, compliance validation |
| Stakeholders | Feedback, acceptance sign-off |
| External Partners | [If applicable - hardware, integration, etc.] |
```

---

## Response Format (CRITICAL)

Your response MUST include:

1. **SOW Metadata Table** — Project name, client, duration, objective
2. **Section Mapping** — How SOW maps to Problem-Based SRS
3. **Delivery Components** — List with estimated effort
4. **Full Acceptance Criteria** — Per component, written explicitly
5. **Effort Breakdown** — By component and category
6. **Out-of-Scope Items** — Explicit list
7. **Assumptions & Constraints** — From SOW
8. **Roles & Responsibilities** — Clear ownership

**⚠️ INVALID Response:** Only describing what will be created without showing actual structured content.  
**✅ VALID Response:** Includes actual tables, criteria, effort breakdown written out in full.

---

## Artifacts Created

When parsing an existing SOW:

```
outputs/sow-artifacts/
├── 00-sow-metadata.md              # Structured SOW metadata
├── 01-section-mapping.md           # Maps SOW → Problem-Based SRS
├── 02-delivery-components.md       # Component inventory with effort
├── 03-acceptance-criteria.md       # All AC by component
├── 04-out-of-scope.md              # Out of scope + assumptions
└── 05-project-roles.md             # Roles & responsibilities
```

When generating a SOW from requirements:

```
outputs/generated-sow/
├── SOW-[ProjectName]-v1.0.md       # Complete SOW document
└── components/
    ├── component-1.md              # Details for Component 1
    ├── component-2.md              # Details for Component 2
    └── ...
```

---

## Key Principles

1. **Bidirectional:** Support both parsing (SOW → SRS) and generation (SRS → SOW)
2. **Component-Driven:** Organize all outputs around delivery components, not abstract requirements
3. **Effort-Aware:** Always include estimation; no orphaned requirements
4. **Scope-Explicit:** Always clarify in/out of scope with assumptions
5. **Traceability:** Map every generated requirement back to source (original SOW or CN/FR)

---

## Example: Eurofiber Project

When processing the Eurofiber SOW:

```markdown
## SOW Metadata

| Field | Value |
|-------|-------|
| **Project Name** | Eurofiber Visitor & Card Holder Flow |
| **Client** | Eurofiber NV |
| **SOW Date** | 23/05/2026 |
| **Estimated Duration** | 34 workdays |
| **Objective** | Implement SelfRegistration kiosk with identity verification (eID/passport/license), facial enrollment, and dispatch contact capability |

## Delivery Components (6 total)

| ID | Component | Effort | Status |
|----|-----------|--------|--------|
| C01 | Webservice (11 endpoints) | 5.5 days | Not Started |
| C02 | Document Scanner Integration | 5 days | Not Started |
| C03 | Auto-Remove Mechanism | 0.5 days | Not Started |
| C04 | Visitor Select Rule | 3 days | Not Started |
| C05 | BioStation Integration | 10 days | Not Started |
| C06 | SIP Call Integration | Included in C05 | Not Started |

**Total Effort:** 24 days (dev) + 10 days (overhead) = **34 workdays**

## Out of Scope

- PowerApp development (client responsibility)
- Hardware and network management (client responsibility)
- Document scanner software installation (handled by Adaptive Recognition)
```

---

## Next Steps

After parsing/generating SOW:

1. **Use Customer Needs skill** to formalize "In Scope" items as CNs
2. **Use Functional Requirements skill** to generate FRs for each component
3. **Use Zigzag Validator** to confirm CP → CN → FR → Deliverable traceability
4. **Use SOW Scope Mapper** to ensure no requirements violate scope boundaries
