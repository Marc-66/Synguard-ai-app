"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten..."
[---SPLIT-DOSSIER---]
### 📑 1. EXECUTIVE SUMMARY & BUSINESS CASE

The integration of iLOQ RF wireless locks into the Synguard platform is driven by the need to remain competitive with industry benchmarks like Nedap AEOS Locker Management. This project aims to enhance the user experience by eliminating the need for dual system management (iLOQ Manager and Synguard) and enabling real-time synchronization of access rights between SynApp and iLOQ Cloud. The integration promises significant business value by increasing the licensable value per door without requiring additional physical hardware, thereby offering a streamlined solution for both end customers and partners. The financial projections include a total project value of €50, direct loadable value of €7, and an expected annual recurring revenue of €12.

### ⚖️ 2. STRATEGIC DIRECTOR EVALUATION MATRIX (WORKING METHOD)

- **Strategic Vision fit (Yes):** This integration aligns with Synguard's strategic vision of expanding its ecosystem through partnerships and enhancing its access management solutions. It supports the roadmap by leveraging cloud-based technologies and increasing the platform's competitive edge.

- **Technical Feasibility (High):** The integration is technically feasible given the existing SynCon Evo and SynApp architecture, which supports cloud-to-cloud communication. The availability of the iLOQ Cloud Gateway API further facilitates seamless integration.

- **Functional Sufficiency (Sufficient):** The functional requirements are clearly defined, including bidirectional sync, real-time logging, and battery status monitoring. These specifications provide a comprehensive understanding of the desired outcomes and minimize the risk of misinterpretation.

- **Genericity & Multi-tenant Value (Generic):** The solution is designed to be multi-tenant, offering value to various customers across different verticals such as healthcare and education. It is not limited to a single customer, thereby enhancing its market appeal.

### 🔧 3. FUNCTIONAL SPECIFICATIONS (BASE FOR STATEMENT OF WORK)

1. **The system shall** enable bidirectional synchronization of access rights between SynApp and iLOQ Cloud, ensuring real-time updates and consistency across platforms.

2. **The system shall** provide real-time logging of access events, allowing operators to monitor and audit access activities efficiently.

3. **The system shall** display the battery status of iLOQ locks within the SynApp interface, providing operators with critical information for maintenance and operational planning.

4. **The system shall** integrate iLOQ icons into the SynApp tree structure, ensuring a seamless user experience and intuitive navigation.

5. **The system shall** process synchronization requests within 5 seconds, maintaining operational efficiency and user satisfaction.

6. **The system shall** ensure offline functionality of locks, allowing them to operate independently of the network connection in case of outages.

These specifications will serve as the foundation for the development team to conduct a technical analysis and implement the integration effectively.
[---SPLIT-DOSSIER---]
## Functional Requirements

### FR-001: Bidirectional Synchronization of Access Rights
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall enable bidirectional synchronization of access rights between SynApp and iLOQ Cloud, ensuring real-time updates and consistency across platforms.

**Acceptance Criteria:**
- [ ] Access rights changes in SynApp are reflected in iLOQ Cloud within 5 seconds.
- [ ] Access rights changes in iLOQ Cloud are reflected in SynApp within 5 seconds.

### FR-002: Real-Time Logging of Access Events
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall provide real-time logging of access events, allowing operators to monitor and audit access activities efficiently.

**Acceptance Criteria:**
- [ ] Access events are logged within 2 seconds of occurrence.
- [ ] Logs include timestamp, user ID, and access point details.

### FR-003: Display of Battery Status
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall display the battery status of iLOQ locks within the SynApp interface, providing operators with critical information for maintenance and operational planning.

**Acceptance Criteria:**
- [ ] Battery status is updated in real-time and displayed in the SynApp dashboard.
- [ ] Alerts are generated when battery levels fall below 20%.

### FR-004: Integration of iLOQ Icons
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall integrate iLOQ icons into the SynApp tree structure, ensuring a seamless user experience and intuitive navigation.

**Acceptance Criteria:**
- [ ] iLOQ icons are displayed correctly in the SynApp interface.
- [ ] Users can navigate to iLOQ-specific settings through the icons.

### FR-005: Synchronization Request Processing Time
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall process synchronization requests within 5 seconds, maintaining operational efficiency and user satisfaction.

**Acceptance Criteria:**
- [ ] 95% of synchronization requests are completed within 5 seconds.
- [ ] System logs processing time for each synchronization request.

### FR-006: Offline Functionality of Locks
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall ensure offline functionality of locks, allowing them to operate independently of the network connection in case of outages.

**Acceptance Criteria:**
- [ ] Locks continue to function with stored access rights during network outages.
- [ ] System logs offline access events for later synchronization.

## Non-Functional Requirements

### NFR-001: Performance
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall maintain a response time of less than 2 seconds for user interface interactions under normal load conditions.

**Measurement Criteria:**
- **Target:** < 2 seconds for 95th percentile
- **Minimum Acceptable:** < 3 seconds for 99th percentile
- **Measurement Method:** Application performance monitoring (APM)

### NFR-002: Security
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall ensure secure data transmission between SynApp and iLOQ Cloud using end-to-end encryption.

**Measurement Criteria:**
- **Target:** 256-bit encryption for all data transmissions
- **Minimum Acceptable:** 128-bit encryption
- **Measurement Method:** Security audits and penetration testing

### NFR-003: Usability
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall provide an intuitive user interface for managing iLOQ locks, ensuring ease of use for operators.

**Measurement Criteria:**
- **Target:** User satisfaction score of 4.5/5 in usability testing
- **Minimum Acceptable:** 4.0/5
- **Measurement Method:** User surveys and usability testing

### NFR-004: Reliability
**Traces to:** CN-001 — Integration of iLOQ RF wireless locks

The system shall achieve 99.9% uptime for the synchronization service, ensuring high availability.

**Measurement Criteria:**
- **Target:** < 1 hour of downtime per year
- **Minimum Acceptable:** < 8 hours of downtime per year
- **Measurement Method:** System monitoring and uptime reports

---

These requirements will be saved as individual files in the appropriate folders for functional and non-functional requirements, ensuring traceability and ease of implementation by the engineering team.