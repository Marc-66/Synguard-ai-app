---
name: functional-requirements
description: Generate Functional Requirements (FR) and Non-Functional Requirements (NFR) from Customer Needs and Software Vision. Creates individual requirement files with traceability. Supports SOW integration for component-based project organization. Step 5 of Problem-Based SRS methodology.
license: MIT
metadata:
  author: rafael-gorski
  version: "1.3"
  methodology: problem-based-srs
  step: 5
  sow-integration: "true"
---

# Functional Requirements (FR) & Non-Functional Requirements (NFR)

> **Step 5 of 5** in Problem-Based SRS methodology  
> **Previous:** Customer Needs → Software Vision  
> **Next:** Requirements Validation / Implementation

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) when, and only when, they appear in all capitals, as shown here.

---

## Position in Process

```
Step 1: Customer Problems → Step 2: Software Glance → Step 3: Customer Needs
                                                              ↓
                                                    Step 4: Software Vision
                                                              ↓
                                                    Step 5: FR/NFR (You are here)
```

---

## Required Inputs

Before running this skill, ensure you have completed artifacts from previous steps:

- [ ] **Customer Needs (CNs)** — from customer-needs skill
- [ ] **Software Vision** — from software-vision skill

**⚠ Warning**: Do not proceed without these inputs. FRs cannot be generated independently—they MUST trace to Customer Needs and respect Software Vision boundaries.

---

## Definition

**Functional Requirements (FR):** Define WHAT the software system SHALL DO to fulfill Customer Needs. FRs describe specific capabilities, behaviors, and functions—not how they are implemented.

**Non-Functional Requirements (NFR):** Define quality attributes and constraints on HOW WELL the system performs. NFRs specify performance, security, usability, reliability, and other quality characteristics.

## Your Task

For each CN:
1. Generate FR statements using "shall/should" notation
2. Identify any NFRs needed (quality attributes)
3. Save each FR/NFR as an individual file (see File Output section)
4. Create index files (_index.md) for both folders
5. **If SOW context available:** Map FRs to SOW components and use SOW-style acceptance criteria (see SOW Integration section)
6. **Present ALL FR statements in your response** (see Response Format immediately below)

---

## Response Format (CRITICAL — DO NOT SKIP)

**⚠ MANDATORY:** Your response MUST contain the actual FR requirement statements written out in full. This is NOT optional — a response that only describes file creation actions without showing the actual requirements is INVALID and INCOMPLETE.

**Every FR in the response MUST include:**

1. **The "shall" statement** — written out explicitly using the grammar: `The [System] shall [verb] [object]`
2. **CN traceability** — each FR MUST show which CN it traces to (e.g., `→ CN-001`)
3. **Acceptance criteria** — at least 2 testable criteria per FR

**Example of CORRECT response format:**

```markdown
## Functional Requirements

### FR-001: Client Registration
**Traces to:** CN-001 — Client data management

The CRM system shall allow the Account Manager to register a new client in the database.

**Acceptance Criteria:**
- [ ] System accepts client name, contact info, and company details
- [ ] System assigns unique client ID upon successful registration

### FR-002: Client Data Update
**Traces to:** CN-001 — Client data management

The CRM system shall allow the Account Manager to update existing client records.

**Acceptance Criteria:**
- [ ] System validates modified fields before saving
- [ ] System logs update timestamp
```

**Example of WRONG response (DO NOT do this):**
```
| CN | Functional Requirements |
|----|------------------------|
| CN.1 | FR-001 Registration, FR-002 Update |
```

The wrong format above lacks "shall" statements, acceptance criteria, and proper traceability.

---

## 📁 Output: Individual Requirement Files

**CRITICAL:** Each FR and NFR MUST be saved as an individual file so engineers can work on them as independent development units.

**⚠ ONE FILE AT A TIME:** Always create FR/NFR files **sequentially, one at a time** — never create multiple files in parallel. Batch file creation causes JSON serialization errors when the combined content is too large.

### Folder Structure

```
.spec/
├── functional-requirements/
│   ├── _index.md                    # Summary and traceability matrix
│   ├── FR-001-[short-name].md       # Individual FR file
│   ├── FR-002-[short-name].md
│   └── ...
└── non-functional-requirements/
    ├── _index.md                    # Summary
    ├── NFR-001-[short-name].md      # Individual NFR file
    └── ...
```

### File Naming Convention

```
FR-[NNN]-[short-descriptive-name].md
NFR-[NNN]-[short-descriptive-name].md
```

Examples:
- `FR-001-client-registration.md`
- `FR-002-client-data-modification.md`
- `NFR-001-response-time.md`
- `NFR-002-data-encryption.md`

---

## FR Structured Notation

Each FR MUST follow this grammar:

```
The [Subject] shall [Verb] [Object] [Constraint] [Condition]
```

Where:
- **Subject**: The software system (e.g., "The CRM system", "The Invoice System")
- **Verb**: "shall" (mandatory) or "should" (desirable)
- **Object**: The specific action or capability
- **Constraint**: Limitations or quality attributes (optional)
- **Condition**: When/where this applies (optional)

## NFR Structured Notation

Each NFR MUST follow this grammar:

```
The [Subject] shall [Quality Attribute] [Measurable Target] [Condition]
```

Where:
- **Subject**: The software system
- **Quality Attribute**: Performance, security, usability, etc.
- **Measurable Target**: Specific, quantifiable criteria
- **Condition**: When/where this applies (optional)

---

## Individual FR File Template

Each FR file MUST follow this template:

```markdown
## FR-[NNN]: [Brief Title]

## Requirement

**ID:** FR-[NNN]  
**Title:** [Descriptive title]  
**Priority:** [Must Have | Should Have | Could Have | Won't Have]  
**Status:** [Draft | Review | Approved | In Progress | Implemented | Tested]

### Statement

The [System] shall [verb] [object] [constraint] [condition].

## Traceability

| Traces To | ID | Description |
|-----------|-----|-------------|
| Customer Need | CN-[X] | [CN description] |
| Customer Problem | CP-[Y] | [CP description] |

## Acceptance Criteria

- [ ] Criterion 1 (testable)
- [ ] Criterion 2 (testable)
- [ ] Criterion 3 (testable)

## Implementation Notes

<!-- Engineers add notes here during implementation -->

## Test Cases

<!-- QA adds test case references here -->

---
*Created: [Date]*  
*Last Updated: [Date]*  
*Author: [Name]*
```

---

## Individual NFR File Template

Each NFR file MUST follow this template:

```markdown
## NFR-[NNN]: [Brief Title]

## Requirement

**ID:** NFR-[NNN]  
**Title:** [Descriptive title]  
**Category:** [Performance | Security | Usability | Reliability | Scalability | Maintainability]  
**Priority:** [Must Have | Should Have | Could Have | Won't Have]  
**Status:** [Draft | Review | Approved | In Progress | Implemented | Tested]

### Statement

The [System] shall [quality attribute] [measurable target] [condition].

## Traceability

| Traces To | ID | Description |
|-----------|-----|-------------|
| Customer Need | CN-[X] | [CN description] |
| Applies To FRs | FR-[A], FR-[B] | [Related FRs] |

## Measurement Criteria

- **Target:** [Specific measurable target]
- **Minimum Acceptable:** [Threshold]
- **Measurement Method:** [How to verify]

## Acceptance Criteria

- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)

## Implementation Notes

<!-- Engineers add notes here during implementation -->

---
*Created: [Date]*  
*Last Updated: [Date]*
```

---

## SOW Integration (When SOW Context Available)

If the project has a Statement of Work (SOW) from the `sow-generator` skill, enhance your FR generation with SOW-specific metadata:

### Enhanced FR File Template (SOW-Aware)

Each FR file should include SOW context:

```markdown
## FR-[NNN]: [Brief Title]

## Requirement

**ID:** FR-[NNN]  
**Title:** [Descriptive title]  
**Priority:** [Must Have | Should Have | Could Have | Won't Have]  
**Status:** [Draft | Review | Approved | In Progress | Implemented | Tested]

### Statement

The [System] shall [verb] [object] [constraint] [condition].

## Traceability

| Traces To | ID | Description |
|-----------|-----|-------------|
| Customer Need | CN-[X] | [CN description] |
| Customer Problem | CP-[Y] | [CP description] |
| SOW Component | C[N] | [Component name - from SOW] |
| SOW Section | [N.M] | [Deliverables or Acceptance Criteria section] |

## SOW Context

**Delivery Component:** C[N] - [Component Name]  
**SOW Deliverable Section:** 7.[N]  
**SOW Acceptance Section:** 8.[N]  
**Estimated Effort:** [X days] (from SOW Section 9)  
**Scope Status:** ✅ In Scope / ❌ Out of Scope

## Acceptance Criteria

### Basic Testability
- [ ] Criterion 1 (testable, unit-level)
- [ ] Criterion 2 (testable, unit-level)

### SOW-Style Acceptance (End-to-End)
- [ ] [End-to-end test scenario reflecting actual user/system behavior]
- [ ] [Error handling scenario matching SOW acceptance criteria]
- [ ] [Performance or quality scenario if applicable]

## Implementation Notes

<!-- Engineers add design/implementation notes here -->

## Test Cases

<!-- QA adds test case references here; link to SOW acceptance criteria -->

---
*Created: [Date]*  
*Last Updated: [Date]*  
*Author: [Name]*  
*SOW Version: [Version] — [Date]*
```

### SOW Acceptance Criteria Format

When you have SOW context, format acceptance criteria to match SOW style (Section 8 format from documents like Eurofiber):

**Pattern 1: End-to-End Workflow**
```markdown
- [ ] [Actor] can [action] via [component/interface] [result/validation]

Example:
- [ ] User can initiate document scan via kiosk UI without errors
- [ ] System validates document type (eID / paspoort / rijbewijs)
- [ ] System rejects unchecksum-failing documents with error messaging
```

**Pattern 2: Error Handling**
```markdown
- [ ] When [error condition], [system response] [user impact]

Example:
- [ ] When enrollment fails, fallback screen appears with dispatch instructions
- [ ] When network timeout occurs, system logs error and retries (max 3 times)
```

**Pattern 3: Integration/Communication**
```markdown
- [ ] [Component A] and [Component B] [interaction] [verification]

Example:
- [ ] BioStation and SelfService kiosk communicate within 5 second response time
- [ ] SIP call connects to dispatch system with stable audio quality
```

**Pattern 4: Performance/Scalability**
```markdown
- [ ] System [performs action] [under load/constraint] [measurable result]

Example:
- [ ] System handles 100 concurrent visitors without performance degradation
- [ ] Document cleanup job runs every 10 minutes without blocking user flows
```

### Component Grouping in Index

In the `_index.md` file, organize FRs by SOW component:

```markdown
# Functional Requirements Index

## Summary

Total FRs: X  
Total Components: Y  
In Scope: A, Out of Scope: B

---

## FRs by SOW Component

### Component C01: [Component Name] (SOW 7.1)
**Estimated Effort:** 5.5 days (SOW 9)  
**Status:** In Development

- **FR-001-[name]** → CN-001 | [Brief description]
- **FR-002-[name]** → CN-002 | [Brief description]
- **FR-003-[name]** → CN-003 | [Brief description]

**Sub-total:** 3 FRs

---

### Component C02: [Component Name] (SOW 7.2)
**Estimated Effort:** 5 days (SOW 9)  
**Status:** In Design

- **FR-004-[name]** → CN-004 | [Brief description]
- **FR-005-[name]** → CN-005 | [Brief description]

**Sub-total:** 2 FRs

---

## Traceability Matrix (CP → CN → FR → Component)

| CP | CN | FR | Component | Status |
|----|----|----|-----------|--------|
| CP-01 | CN-001 | FR-001 | C01 | ✅ In Scope |
| CP-01 | CN-002 | FR-002 | C01 | ✅ In Scope |
| ... | ... | ... | ... | ... |

---

## Effort Tracking

| Component | FRs | Est. Days | Actual Days | % Complete |
|-----------|-----|-----------|-------------|------------|
| C01 | 3 | 5.5 | TBD | 0% |
| C02 | 2 | 5.0 | TBD | 0% |
| **TOTAL** | **5** | **10.5** | **TBD** | **0%** |
```

---

## Integration Workflow

When you have SOW context:

1. **Input:** SOW document (parsed by sow-generator skill) + CNs + Software Vision
2. **Process:** For each CN, generate FRs and assign to SOW component
3. **Validate:** Use sow-scope-mapper skill to verify FRs don't violate scope
4. **Output:** FR files with SOW component tags + component-organized index
5. **Handoff:** FRs ready for development grouped by delivery component

**Example Flow:**

```
SOW (Eurofiber)
    ↓
sow-generator: Parse into components (C01-C06)
    ↓
customer-needs: Generate CNs from "In Scope" items
    ↓
functional-requirements: Generate FRs, assign to components (THIS SKILL)
    ↓
sow-scope-mapper: Validate FR vs. scope boundaries
    ↓
zigzag-validator: Confirm full traceability (CP → CN → FR → Component)
    ↓
Output: FR files tagged by component, ready for dev team
```

---



- Every FR MUST trace to at least one Customer Need (FR.X → CN.Y)
- Every NFR SHOULD trace to CNs or indicate which FRs it applies to
- One CN typically requires MULTIPLE FRs
- Every CN MUST be addressed by at least one FR

## Quality Rules (per [ISO/IEC/IEEE 29148:2018](../../docs/references/iso-iec-ieee-29148-2018.md))

- **Complete**: All customer needs MUST be met by requirements
- **Correct**: All requirements MUST meet some customer need
- **Testable**: Each FR MUST have verifiable acceptance criteria
- **Unambiguous**: Use precise language, avoid vague terms
- **Measurable**: NFRs MUST have quantifiable targets

## Content Restrictions (CRITICAL)

**NO CODE SNIPPETS:** FR and NFR files MUST NOT contain:
- Programming code examples
- Code blocks with implementation logic
- Pseudo-code implementations
- SQL queries, API calls, or technical syntax

**NO CONSTRUCTION DETAILS:** FR and NFR files MUST NOT include:
- Database schemas or table definitions
- API endpoint specifications
- Class diagrams or implementation architecture
- Technology stack decisions
- Configuration details

**WHERE TO PUT CONSTRUCTION DETAILS:**
Construction and implementation details belong in separate design documents:
```
.spec/
├── functional-requirements/     # FR files (WHAT - no code)
├── non-functional-requirements/ # NFR files (WHAT - no code)
└── design/                      # Construction details (HOW)
    ├── architecture.md          # System architecture
    ├── data-model.md            # Database schemas
    ├── api-specification.md     # API endpoints
    └── implementation-notes/    # Technical notes per FR
```

---

## Examples

### Example FR File: FR-001-client-registration.md

```markdown
## FR-001: Client Registration

## Requirement

**ID:** FR-001  
**Title:** Client Registration  
**Priority:** Must Have  
**Status:** Draft

### Statement

The CRM system shall allow the Account Manager to register a new client in the database.

## Traceability

| Traces To | ID | Description |
|-----------|-----|-------------|
| Customer Need | CN-001 | Account Manager needs system to maintain client records |
| Customer Problem | CP-001 | Company must maintain accurate client data for compliance |

## Acceptance Criteria

- [ ] System accepts client name, contact info, and company details
- [ ] System validates required fields before submission
- [ ] System assigns unique client ID upon successful registration
- [ ] System displays confirmation message after registration
- [ ] System logs registration timestamp and user

---
*Created: 2024-01-15*  
*Author: Requirements Team*
```

### Example NFR File: NFR-001-response-time.md

```markdown
## NFR-001: Response Time

## Requirement

**ID:** NFR-001  
**Title:** Search Response Time  
**Category:** Performance  
**Priority:** Must Have  
**Status:** Draft

### Statement

The CRM system shall return client search results within 2 seconds under normal load conditions.

## Traceability

| Traces To | ID | Description |
|-----------|-----|-------------|
| Customer Need | CN-002 | Users need quick access to client information |
| Applies To FRs | FR-004, FR-007 | Client search and filtering functions |

## Measurement Criteria

- **Target:** < 2 seconds for 95th percentile
- **Minimum Acceptable:** < 5 seconds for 99th percentile
- **Measurement Method:** Application performance monitoring (APM)

## Acceptance Criteria

- [ ] Search returns results in < 2 seconds with up to 10,000 client records
- [ ] Performance maintained with 100 concurrent users
- [ ] Response time logged for monitoring

---
*Created: 2024-01-15*
```

---

## Quality Checklist

Before finalizing, verify:

- [ ] Every FR uses syntax: The [Subject] shall [Verb] [Object] [Constraint] [Condition]
- [ ] Every FR saved as individual file (FR-NNN-name.md)
- [ ] Every FR traces to at least one CN
- [ ] Every CN from input is addressed by at least one FR
- [ ] All FRs are testable with clear acceptance criteria
- [ ] All FRs stay within Software Vision boundaries
- [ ] Index file (_index.md) created with all FRs listed
- [ ] NFRs have measurable targets (not vague terms)
- [ ] No implementation/design details in requirements (WHAT not HOW)
- [ ] No code snippets or programming examples in FR/NFR files

---

## Common Pitfalls

| ❌ Wrong | ✅ Correct |
|----------|-----------|
| "The system shall use a MySQL database" | "The system shall persist client data between sessions" |
| "The system shall be user-friendly" | "The system shall allow users to complete registration in under 3 minutes" |
| FR with no CN link | Always specify FR → CN traceability in file |
| "The system shall be fast" | "The system shall return search results within 2 seconds" |
| All FRs in one file | Each FR in separate file for independent development |
| Vague NFR: "good performance" | Measurable NFR: "< 2 second response time" |
| Code snippet in FR file | Reference design docs for implementation details |

---

## Handoff to Engineering

After completing this step:

```
✅ Step 5 Complete: Requirements Specified

📁 Created: functional-requirements/
   ├── _index.md (N FRs total)
   ├── FR-001-*.md → CN-001
   ├── FR-002-*.md → CN-001
   └── ...

📁 Created: non-functional-requirements/
   ├── _index.md (N NFRs total)
   └── NFR-001-*.md

📁 Updated: traceability-matrix.md

→ MANDATORY: Run zigzag-validator skill for full chain verification
→ Engineers can now pick individual FR files to implement
```

---

## Reference

Based on Problem-Based SRS methodology (Gorski & Stadzisz, 2016)

**Version:** 1.2  
**Step:** 5 of 5  
**Validation:** zigzag-validator skill
