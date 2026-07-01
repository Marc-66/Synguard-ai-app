---
name: sow-scope-mapper
description: Map Customer Needs to SOW scope sections, identify scope violations, and formalize assumptions as constraints. Validates that Functional Requirements stay within project boundaries and don't introduce scope creep. Use when you need to ensure requirements align with SOW In/Out of Scope, assumptions, and system constraints.
license: MIT
metadata:
  author: synguard-ai
  version: "1.0"
  methodology: problem-based-srs-extended
  integration: sow-based-requirements
---

# SOW Scope Mapper

> Align Customer Needs and Functional Requirements with SOW scope boundaries and project constraints.

## Purpose

This skill ensures that requirements stay within agreed scope by:

1. **Mapping each CN to SOW scope section** (Section 3.1 or 3.2)
2. **Validating FRs against scope** — flagging scope creep
3. **Formalizing assumptions** from SOW Section 5 as requirement constraints
4. **Creating scope compliance report** with traceability
5. **Preventing requirement-scope misalignment** early

## When to Use

Use this skill when:
- ✅ You have Customer Needs (CNs) from customer-needs skill
- ✅ You have extracted SOW metadata (from sow-generator skill)
- ✅ You want to validate FRs against scope boundaries
- ✅ You need to document why certain requests are "out of scope"
- ✅ You want to ensure assumptions are captured as constraints

Do NOT use when:
- ❌ You don't have a SOW or scope definition yet
- ❌ Working on greenfield projects with no scope constraints

---

## Task: Map CNs to SOW Scope

### 1. Create Scope Inventory

From SOW Section 3, create structured lists:

```markdown
## Scope Inventory (from SOW Section 3)

### In Scope (3.1)

| Scope Item | SOW Ref | Description |
|------------|---------|-------------|
| [Item name] | 3.1.1 | [What's included] |
| [Item name] | 3.1.2 | [What's included] |
| ... | ... | ... |

**Count:** X items in scope

### Out of Scope (3.2)

| Scope Item | SOW Ref | Description | Reason |
|------------|---------|-------------|--------|
| [Item name] | 3.2 | [What's excluded] | [Why: budget, timeline, external dependency] |
| [Item name] | 3.2 | [What's excluded] | [Why] |
| ... | ... | ... | ... |

**Count:** Y items explicitly out of scope
```

### 2. Map Each CN to Scope

For each Customer Need from customer-needs skill:

```markdown
## CN Scope Mapping

### CN-001: [Brief title]

**Scope Status:** ✅ IN SCOPE (or ❌ OUT OF SCOPE)

**Maps To:**
- SOW Section 3.1.[X] — [Scope section name]
- Delivery Component: [C01, C02, etc.]

**Requirement Statement:**
> [Full CN statement]

**Scope Boundaries:**
- Included: [What this CN covers]
- Not Included: [What related items are out of scope]

**Related Assumptions (SOW Section 5):**
- [If CN depends on specific assumptions, list them]
- [If CN is constrained by system requirements (Section 4), note them]

---

### CN-002: [Brief title]

**Scope Status:** ✅ IN SCOPE

**Maps To:**
- SOW Section 3.1.[X]
- Delivery Component: [C02]

[Continue pattern...]
```

### 3. Create Scope Compliance Matrix

```markdown
## Scope Compliance Matrix

| ID | Customer Need | Status | SOW Section | Component | Assumptions | Conflicts |
|----|-------------------|--------|------------|-----------|------------|-----------|
| CN-001 | [Brief] | ✅ In | 3.1.1 | C01 | None | None |
| CN-002 | [Brief] | ✅ In | 3.1.2 | C01 | A1, A2 | None |
| CN-003 | [Brief] | ❌ Out | N/A | N/A | N/A | Hardware not provided |
| ... | ... | ... | ... | ... | ... | ... |

**Summary:**
- **In Scope CNs:** X  
- **Out of Scope CNs:** Y  
- **Flagged for Review:** Z
```

---

## Task: Validate FRs Against Scope

### 1. Create FR-to-Scope Validation

For each Functional Requirement:

```markdown
## FR Scope Validation

### FR-001: [Brief title]

**Requirement Statement:**
> The system shall [verb] [object] [constraint]

**Scope Check:**

| Check | Result | Details |
|-------|--------|---------|
| In Scope? | ✅ YES | Maps to SOW 3.1.1 |
| Component Assigned? | ✅ YES | Belongs to C01 |
| Assumptions Met? | ✅ YES | Depends on A1 (network connectivity) |
| Conflicts? | ❌ NO | None detected |
| Effort Estimated? | ✅ YES | 2 days in SOW Section 9 |

**Status:** ✅ APPROVED — Requirement is within scope

---

### FR-002: [Brief title]

**Requirement Statement:**
> [Full FR statement]

**Scope Check:**

| Check | Result | Details |
|-------|--------|---------|
| In Scope? | ⚠️ PARTIAL | Item partially in scope (see below) |
| Component Assigned? | ✅ YES | C02 |
| Assumptions Met? | ❌ NO | Depends on A5 (external service unavailable) |
| Conflicts? | ⚠️ YES | Potential overlap with FR-001 |
| Effort Estimated? | ❌ NO | **MISSING** — Not listed in SOW |

**Status:** ⚠️ REVIEW REQUIRED

**Issues:**
- [ ] Assumption A5 not met; may require architecture change
- [ ] Effort not estimated; needs addition to SOW Section 9
- [ ] Potential overlap with FR-001; needs clarification

**Recommendation:**
- Clarify scope boundary with Product Owner
- Add effort estimate (estimated: 3 days)
- Resolve assumption A5 dependency
```

### 2. Create Scope Violation Report

```markdown
## Scope Violation Report

### Violations Found: X

#### ⚠️ Issue 1: Requirement Outside Scope

**FR:** FR-005  
**Title:** [Requirement name]

**Violation Type:** 🚫 OUT OF SCOPE

**Statement:**
> [Full FR statement]

**Problem:**
This requirement is NOT listed in SOW Section 3.1 (In Scope).
- SOW Section 3.2 explicitly excludes: "[Related excluded item]"
- No delivery component assigned
- No effort estimated in SOW

**SOW Reference:**
- SOW Section 3.2: "[Excluded item description]"
- Reason: "[Why it's out of scope]"

**Resolution Options:**
1. **Remove this FR** — It's out of scope by agreement
2. **Change Scope** — Request change via change management (SOW Section 6)
3. **Map to Existing Component** — If it's a misclassification

**Recommendation:** 
⚠️ Clarify with Product Owner if this should be:
- In scope (change request required)
- Out of scope (remove FR)
- Deferred (add to backlog for future phase)

---

#### ⚠️ Issue 2: Missing Effort Estimation

**FR:** FR-006, FR-007

**Violation Type:** ⚠️ MISSING EFFORT

**Problem:**
These FRs are in scope but NOT listed in SOW Section 9 (Estimation).

**FRs Affected:**
- FR-006: [Title] → Component C02 → **0 days estimated**
- FR-007: [Title] → Component C03 → **0 days estimated**

**Impact:**
Cannot accurately estimate total project effort. May exceed 34-day budget.

**Resolution:**
- [ ] Estimate effort for FR-006 (proposed: 1.5 days)
- [ ] Estimate effort for FR-007 (proposed: 2 days)
- [ ] Update SOW Section 9 estimation table
- [ ] Recalculate total effort

---

#### ⚠️ Issue 3: Assumption Not Met

**FR:** FR-003, FR-004, FR-008

**Violation Type:** ⚠️ ASSUMPTION DEPENDENCY

**Problem:**
These FRs depend on SOW Section 5 assumptions that may not be met.

**Assumptions Referenced:**
- **A1:** "Biostation compatible with 8x8 SIP" — **Dependency:** FR-003, FR-008
- **A2:** "Adaptive Recognition firmware stable" — **Dependency:** FR-004
- **A3:** "All devices on same network" — **Dependency:** FR-003, FR-008

**Risk Analysis:**
- If A1 not met → FR-003, FR-008 fail; requires architecture redesign (~5 days)
- If A2 not met → FR-004 fails; requires firmware upgrade/workaround (~3 days)
- If A3 not met → FR-003, FR-008 fail; requires network redesign (external)

**Resolution:**
- [ ] Confirm all assumptions with Eurofiber before development
- [ ] Add contingency effort (proposed: +5 days buffer)
- [ ] Document assumption verification checklist

### Summary

| Violation Type | Count | Severity | Action |
|---|---|---|---|
| Out of Scope | 1 | 🔴 High | Clarify with PO |
| Missing Effort | 2 | 🟡 Medium | Estimate + update |
| Assumption Risk | 3 | 🟡 Medium | Verify assumptions |

**Total FRs Reviewed:** 10  
**FRs With Issues:** 6 (60%)  
**FRs Approved:** 4 (40%)

**Recommendation:** Resolve all violations before development begins.
```

---

## Task: Formalize Assumptions as Constraints

### 1. Extract Assumptions from SOW Section 5

```markdown
## Assumptions & Constraints (from SOW Section 5)

### Assumption A1: Platform Compatibility
**Statement:** "Biostation is compatible with 8x8 SIP centrale"

**Formalized as NFR-Constraint:**
- System shall support 8x8 SIP signaling protocol
- Biostation firmware version: [Verify with client]
- If not compatible: *Scope change required via change management*

**Applied To FRs:** FR-003, FR-008 (SIP call integration)

**Verification Checklist:**
- [ ] 8x8 SIP compatibility confirmed with Eurofiber
- [ ] Biostation firmware version documented
- [ ] SIP endpoint configuration documented

---

### Assumption A2: External Dependencies
**Statement:** "Adaptive Recognition Osmond scanner firmware is stable"

**Formalized as NFR-Constraint:**
- Scanner firmware shall be stable and current (≤1 year old)
- If firmware not stable: *Requires firmware update or alternate scanner*

**Applied To FRs:** FR-004 (document scanner integration)

**Verification Checklist:**
- [ ] Current firmware version confirmed
- [ ] Stability test completed
- [ ] Fallback plan if firmware unstable

---

### Assumption A3: Network Infrastructure
**Statement:** "All devices sit on the same network"

**Formalized as NFR-Constraint:**
- Network latency between kiosk ↔ BioStation: ≤100ms
- Network availability: ≥99.5% uptime (client responsibility)
- If network issues occur: *Client to resolve via IT team*

**Applied To FRs:** FR-003, FR-008

**Verification Checklist:**
- [ ] Network connectivity tested
- [ ] Latency measured and confirmed ≤100ms
- [ ] Network support from Eurofiber IT confirmed

---

### Assumption A4: External Scope (Client Responsibility)
**Statement:** "Computers and virtual machines provided by client"

**Formalized as Out-of-Scope Deliverable:**
- Hardware provisioning: **Eurofiber responsibility**
- OS installation (Windows 11): **Eurofiber responsibility**
- Network setup: **Eurofiber responsibility**
- Software support: **Synguard responsibility**

**Applied To:** All FRs (underlying infrastructure)

**System Requirements (SOW Section 4):**
- [ ] NUC for SynReg: Windows 11, Intel i5+, 4GB RAM, 128GB SSD
- [ ] SynAppWindows PC: Windows 11, network connection
- [ ] BioStation device: [Verified compatible]
- [ ] Document scanner: Adaptive Recognition Osmond R + USB connection
```

### 2. Create Constraint Specification

```markdown
## Formalized Constraints (for Functional Requirements)

| ID | Constraint | Source | Applies To | Impact |
|----|-----------|--------|-----------|--------|
| C1 | Biostation ↔ 8x8 SIP | A1 | FR-003, FR-008 | SIP call must work or scope changes |
| C2 | Scanner firmware stable | A2 | FR-004 | Document scanning must be reliable |
| C3 | Network latency ≤100ms | A3 | FR-003, FR-008, FR-007 | Real-time response required |
| C4 | Client provides hardware | A4 | All FRs | Synguard tests only; hardware failures client's issue |
| C5 | Windows 11 environment | A4 | All FRs | .NET/Windows-only components supported |

**Constraint Verification:**
- [ ] All constraints documented in requirement specification
- [ ] Client acknowledgement obtained for external dependencies
- [ ] Fallback plans documented for high-risk constraints
```

---

## Task: Create Scope Change Request Template

When a requirement violates scope:

```markdown
## Scope Change Request

**ID:** SCR-001  
**Status:** SUBMITTED

**Current Scope Baseline:** 34 days (SOW v3.03, 23/05/2026)

### Change Details

**Requested By:** [Role]  
**Date Submitted:** [Date]  
**Priority:** [Must/Should/Could/Won't]

**Description:**
[Requirement that violates current scope]

**Justification:**
[Why this should be in scope]

### Impact Analysis (SOW Section 6)

**Scope Impact:** 
- New component? Yes/No
- New FR? [Count]
- Affects existing components? [List]

**Timeline Impact (Section 9):**
- Estimated effort: +X days
- New total: 34 + X = Y days
- Revised delivery date: [Date]

**Cost Impact:**
- Additional effort cost: €[Calculation]
- Budget delta: +€[Amount]

**Risk Impact:**
- New dependencies? [List]
- Assumption changes? [List]
- Integration risks? [List]

### Decision

| Option | Recommendation | Trade-off |
|--------|---|---|
| **Approve** | Add to scope | +X days, +€Y cost, revised date |
| **Defer** | Move to Phase 2 | Original scope/timeline, higher priority for Phase 1 |
| **Reject** | Keep as out-of-scope | Maintains current commitments |

**Product Owner Decision:** [TBD]  
**Approval Sign-off:** [Signature required]

**If Approved:**
1. Update SOW Section 3.1 (In Scope) with new items
2. Create FRs for new functionality
3. Update SOW Section 9 (Estimation) with new effort
4. Update SOW version number (e.g., v3.04)
5. All parties re-sign SOW acceptance (Section 11)
```

---

## Response Format (CRITICAL)

Your response MUST include:

1. **Scope Inventory Table** — All in-scope and out-of-scope items
2. **CN-to-Scope Mapping** — Each CN's scope status and SOW reference
3. **Scope Compliance Matrix** — Summary of all CNs/FRs vs. scope
4. **Violation Report** — Any FRs outside scope with resolution
5. **Assumption-to-Constraint Mapping** — Formalized constraints from SOW Section 5
6. **Constraint Verification Checklist** — What needs to be confirmed

**⚠️ INVALID Response:** Only describing mappings without showing actual tables and compliance data.  
**✅ VALID Response:** Includes complete mapping tables, violation analysis, and formatted constraints.

---

## Example: Eurofiber Scope Mapping

```markdown
## Scope Inventory

### In Scope (3.1)
- Webservice endpoints (3.1.1)
- Document scanner integration (3.1.2-3.3)
- Autoremove mechanism (3.4)
- Visitor select rule (3.5)
- Biostation integration (3.6)
- SIP call capability (3.7)

### Out of Scope (3.2)
- PowerApp development
- Hardware and network management
- Adaptive Recognition software installation

---

## Assumptions as Constraints

| A | Assumption | Constraint | FRs |
|---|-----------|-----------|-----|
| A1 | 8x8 SIP compatible | Network protocol ≤100ms latency | FR-008 |
| A2 | Scanner firmware stable | Firmware version must be current | FR-004 |
| A3 | Same network | Network uptime ≥99.5% | FR-003 to FR-008 |
| A4 | Client provides hardware | Synguard supports Windows 11 only | All FRs |

---

## Violations Found: 0
✅ All FRs are within scope and assumptions are met.
```

---

## Next Steps

After scope mapping:

1. **Use Zigzag Validator** to confirm end-to-end traceability (CP → CN → FR → Deliverable → Scope)
2. **If violations found:** Initiate scope change request per template
3. **Proceed to Functional Requirements skill** to generate FRs for all in-scope CNs
4. **Use SOW Generator** to create final SOW-formatted document with all estimates
