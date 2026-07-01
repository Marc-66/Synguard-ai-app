---
name: system-requirements
description: Extract, classify, and formalize system infrastructure requirements from Non-Functional Requirements (NFRs) and project scope. Define compute, storage, network, software stack, performance baselines, and deployment targets. Step 6 of Problem-Based SRS + SOW methodology (Phase 2a: Project Planning).
license: MIT
metadata:
  author: synguard-ai
  version: "1.0"
  methodology: problem-based-srs-extended
  phase: project-planning
  sequence: 1
---

# System Requirements

> Translate Non-Functional Requirements (NFRs) into formal infrastructure, software stack, and deployment specifications.

## Purpose

This skill bridges **Requirements Engineering (Step 5)** and **Project Planning (Phase 2)** by:

1. **Extracting infrastructure needs** from NFRs (performance, availability, security)
2. **Classifying requirements** into layers (compute, network, database, middleware, development)
3. **Defining performance baselines** measurable and testable
4. **Specifying software stack** (languages, frameworks, databases, APIs)
5. **Formalizing deployment targets** (dev, staging, production environments)
6. **Documenting external dependencies** and constraints

## When to Use

Use this skill **after Step 5 (FR/NFR generation)** when:

- ✅ You have completed Non-Functional Requirements (NFRs)
- ✅ You need to communicate infrastructure needs to operations/infrastructure teams
- ✅ You need to inform project estimation (Phase 2b)
- ✅ You have SOW Section 4 (System Requirements) to incorporate
- ✅ You need to set up development environment
- ✅ You need to plan deployment and provisioning

Do NOT use when:

- ❌ You haven't completed Step 5 (NFRs) yet
- ❌ You're only doing requirements (no project planning needed)

---

## Required Inputs

Before running this skill, ensure you have:

- [ ] **Non-Functional Requirements (NFRs)** — from Step 5 (functional-requirements skill)
  - Performance requirements (response time, throughput)
  - Availability requirements (uptime, disaster recovery)
  - Security requirements (encryption, authentication)
  - Scalability requirements (concurrent users, data volume)
  - Quality attributes (reliability, maintainability)

- [ ] **Software Vision (Step 4)** — to understand architecture
  - Technology stack preferences
  - System boundaries
  - Integration points

- [ ] **(Optional) SOW Section 4** — if working with SOW workflow
  - Infrastructure specifications
  - Hardware requirements
  - Environment constraints
  - System assumptions (Section 5)

---

## How This Skill Works

### Task 1: Extract Infrastructure from NFRs

For each NFR, identify the infrastructure implications:

```markdown
## NFR-to-Infrastructure Mapping

### NFR-001: Response Time
**Statement:** The system shall return search results within 2 seconds (p95) under normal load

**Infrastructure Implications:**
- Database performance: Need indexed queries (SQL Server premium tier)
- Network latency: <50ms between app ↔ database
- Caching layer: Consider Redis for frequent queries
- Load testing: Need performance baseline testing

**Specification:**
```
| Component | Requirement | Rationale |
|-----------|------------|-----------|
| Database | Azure SQL Standard (S3+) or SQL Server 2019 w/ SSD | Achieves sub-1sec queries |
| Cache | Redis (optional, if p95 still high) | Reduce database hits |
| Network | Local LAN, <50ms latency | Minimize round-trip time |
| Monitoring | Application Performance Monitoring (APM) | Track and optimize |
```

### NFR-002: Concurrency
**Statement:** The system shall support 100 concurrent users without degradation

**Infrastructure Implications:**
- Connection pooling: Need database connection scaling
- Application server: Need horizontal scalability
- Load testing: Must validate with concurrent load
- Memory footprint: Each user session requires memory

**Specification:**
```
| Component | Requirement | Calculation |
|-----------|------------|-------------|
| App Server | Azure App Service Standard tier (minimum) | 100 concurrent = ~2-4 cores needed |
| Database | Connection pool ≥ 200 connections | 100 users × 2 connections (min overhead) |
| Memory | 8GB RAM minimum | ~50MB per concurrent session + OS overhead |
```

### NFR-003: Availability
**Statement:** The system shall maintain 99.5% uptime

**Infrastructure Implications:**
- Redundancy: Need backup infrastructure
- Disaster recovery: RTO < 4 hours, RPO < 1 hour
- Monitoring: Continuous health checks
- Geographic distribution: Reduce single-point-of-failure risk

**Specification:**
```
Production Deployment:
- Primary: Azure App Service (East US region)
- Backup: Azure App Service (West US region)
- Database: Geo-redundant backup (RA-GRS)
- Traffic routing: Azure Traffic Manager (active-passive)
- Monitoring: Azure Monitor with alerts
```

### NFR-004: Security
**Statement:** System shall encrypt all data at rest and in transit

**Infrastructure Implications:**
- TLS certificates: For HTTPS/TLS 1.3
- Encryption keys: Azure Key Vault
- Database encryption: Transparent Data Encryption (TDE)
- Access control: Network security groups, firewalls

**Specification:**
```
| Requirement | Implementation |
|------------|-----------------|
| Data in transit | TLS 1.3 (minimum) on all endpoints |
| Data at rest | AES-256 encryption (database TDE) |
| Key management | Azure Key Vault with key rotation |
| Network security | NSG rules, private endpoints for database |
| Authentication | OAuth 2.0, Azure AD integration |
```
```

### Task 2: Classify into Infrastructure Layers

Create structured inventory by layer:

```markdown
## Infrastructure Layers

### Layer 1: Compute (Processing Power)

| Component | Requirement | Priority | Notes |
|-----------|------------|----------|-------|
| **Development** | | | |
| OS | Windows 11 Pro or macOS 12+ | MUST | Developer machine |
| CPU | Intel i7 or equivalent (6+ cores) | SHOULD | Local builds/debugging |
| RAM | 16GB minimum | SHOULD | VM containers + dev database |
| | | | |
| **Production** | | | |
| App Server | Azure App Service Premium tier | MUST | High availability |
| CPU Cores | 4 cores minimum (scalable to 8+) | SHOULD | Concurrent request handling |
| Memory | 8GB allocated (scale to 16GB) | MUST | From NFR-002 (concurrency) |

### Layer 2: Storage & Database

| Component | Requirement | Priority | Notes |
|-----------|------------|----------|-------|
| **Database** | | | |
| Engine | SQL Server 2019 or Azure SQL Database | MUST | .NET standard |
| Tier | Standard tier (≥ 50 DTUs) | MUST | From NFR-001 (latency) |
| Backup | Daily automated backups (7-day retention) | MUST | SOW Section 5 (assumptions) |
| Geo-replication | RA-GRS for production | SHOULD | From NFR-003 (99.5% uptime) |
| | | | |
| **File Storage** | | | |
| Document Store | Azure Blob Storage (Hot tier) | SHOULD | Document scanner outputs |
| Cache | Redis (optional, if needed for NFR-001) | COULD | Session/response caching |

### Layer 3: Network & Connectivity

| Component | Requirement | Priority | Notes |
|-----------|------------|----------|-------|
| Network Bandwidth | 100 Mbps minimum (local LAN) | MUST | BioStation ↔ Kiosk sync |
| Latency | < 50ms between app ↔ database | MUST | From NFR-001 (response time) |
| | < 100ms between kiosk ↔ BioStation | MUST | From SOW Section 5 (assumptions) |
| VPN/Connectivity | Site-to-site VPN if hybrid | SHOULD | Multi-location deployment |
| DNS | Azure DNS or equivalent | SHOULD | Service discovery |
| CDN | Azure CDN for static assets | COULD | UI performance optimization |

### Layer 4: Software Stack

| Component | Version | Priority | Notes |
|-----------|---------|----------|-------|
| **.NET Runtime** | | | |
| Language | C# 10+ | MUST | Synguard standard |
| Framework | .NET 6 or higher | MUST | Modern, LTS supported |
| | | | |
| **Web Framework** | | | |
| ASP.NET Core | 6.0+ | MUST | HTTP API development |
| Web Server | IIS 10 (Windows) or Kestrel | MUST | Production hosting |
| | | | |
| **Data Access** | | | |
| ORM | Entity Framework Core 6+ | MUST | Data persistence abstraction |
| Database Driver | SQL Server provider (Microsoft.Data.SqlClient) | MUST | .NET standard driver |
| | | | |
| **Integration & Messaging** | | | |
| API Gateway | Azure API Management | SHOULD | Request routing, rate limiting |
| Message Queue | RabbitMQ or Azure Service Bus | COULD | Async processing (document cleanup) |
| | | | |
| **Security & Authentication** | | | |
| Identity Provider | Azure AD (Entra ID) | MUST | Enterprise authentication |
| Protocol | OAuth 2.0, OpenID Connect | MUST | Modern authentication |
| | | | |
| **Monitoring & Logging** | | | |
| APM | Application Insights | MUST | Performance monitoring (NFR-001) |
| Logging | Azure Monitor + Application Insights | MUST | Diagnostic and audit logs |
| Alerting | Azure Monitor Alerts | MUST | Incident response (NFR-003) |

### Layer 5: Development Environment

| Component | Requirement | Priority | Notes |
|-----------|------------|----------|-------|
| IDE | Visual Studio 2022 (Professional+) | MUST | C# development standard |
| SCM | Git + Azure Repos | MUST | Version control, CI/CD integration |
| Build Tool | MSBuild (Visual Studio) | MUST | .NET standard build tool |
| Testing Framework | xUnit or NUnit | SHOULD | Unit testing |
| Test Database | SQL Server Express or LocalDB | SHOULD | Local development database |
| Containerization | Docker Desktop | SHOULD | Consistent dev/prod parity |
| Container Registry | Azure Container Registry (ACR) | SHOULD | Store built images |

### Layer 6: Deployment Environments

```

#### Development Environment
```
Purpose: Local development, rapid iteration
├── Developer Machine
│   ├── Windows 11 Pro + Visual Studio 2022
│   ├── SQL Server Express / LocalDB
│   └── .NET 6 SDK
├── Source Control: Azure Repos (local branch)
└── Build: Local compilation via Visual Studio
```

#### Staging Environment
```
Purpose: Pre-production testing, UAT
├── App Service: Standard tier (same SKU as prod for parity)
├── Database: Azure SQL (Standard tier, separate database)
├── Configuration: Production-like settings
└── Access: Internal team + stakeholders
```

#### Production Environment
```
Purpose: End-user facing, live data
├── App Service: Premium tier with autoscale (2-4 instances)
├── Database: Azure SQL (Standard S3+ or higher)
├── Backup: Geo-redundant (RA-GRS)
├── Monitoring: Full APM + alerting
├── Access: Restricted to ops team + monitoring
└── CDN: Azure CDN for static assets
```

### Task 3: Define Performance Baselines

Create testable, measurable specifications from NFRs:

```markdown
## Performance Baselines (Testable)

| NFR | Baseline Metric | Target | Measurement | Validation Method |
|-----|-----------------|--------|-------------|-------------------|
| **Response Time** | | | | |
| NFR-001 | API response time (p50) | < 1 second | Application logging | Application Insights |
| | API response time (p95) | < 2 seconds | Percentile histogram | APM dashboard |
| | API response time (p99) | < 5 seconds | Percentile histogram | APM dashboard |
| | Database query time (avg) | < 200ms | Database profiler | SQL Profiler |
| | | | | |
| **Concurrency** | | | | |
| NFR-002 | Max concurrent users | 100 | Active session counter | Load test results |
| | Connection pool utilization | < 80% | Connection monitoring | SQL profiler |
| | Memory per user | < 50MB | Memory profiler | WinDbg / dotMemory |
| | | | | |
| **Availability** | | | | |
| NFR-003 | Uptime during business hours | 99.5% | Infrastructure monitoring | Azure Monitor |
| | RTO (Recovery Time Objective) | < 4 hours | Failover test | Disaster recovery drill |
| | RPO (Recovery Point Objective) | < 1 hour | Backup test | Restore validation |
| | | | | |
| **Security** | | | | |
| NFR-004 | TLS version | 1.3 minimum | SSL Labs scan | SSL certificate audit |
| | Encryption algorithm | AES-256 | Database audit | Compliance check |
| | Auth failures (rate limit) | 5 failed attempts = 15 min lockout | Login logs | Security audit |

## Validation Testing Plan

### Load Testing (NFR-002: 100 concurrent users)
```yaml
Tool: Azure Load Testing or JMeter
Scenario:
  - Ramp up: 10 users/second
  - Hold: 100 concurrent users × 10 minutes
  - Ramp down: Linear
  
Success Criteria:
  - No errors (HTTP 5xx)
  - Response time p95 < 2 seconds
  - Database connection pool < 80% utilized
  - Memory usage stable (no leaks)
```

### Performance Baseline Test (NFR-001: Response time < 2s)
```yaml
Tool: Application Insights custom test
Scenarios:
  - Normal load: 50 concurrent users
  - Peak load: 100 concurrent users
  - Stress test: 150% of peak
  
Success Criteria:
  - p95 response < 2 seconds
  - p99 response < 5 seconds
  - Error rate < 0.1%
```

### Availability/DR Test (NFR-003: 99.5% uptime)
```yaml
Frequency: Monthly
Scenarios:
  - Database failover: Switchover to standby
  - App server failure: Instance termination
  - Regional outage: Traffic Manager failover
  
Success Criteria:
  - RTO < 4 hours
  - RPO < 1 hour
  - No data loss
```
```

### Task 4: Document External Dependencies

From SOW Section 5 + Software Vision:

```markdown
## External Dependencies & Constraints

| Dependency | Requirement | Impact | Verification |
|------------|------------|--------|--------------|
| **BioStation API** | REST API v2.0+ | Enrollment feature (FR-005) | API contract test |
| | 8x8 SIP compatible | SIP calling feature (FR-006) | SIP test call |
| | Network latency <100ms | User experience | Ping test |
| **Adaptive Recognition Scanner** | Firmware v5.0+ | Document scanning (FR-004) | Scanner version check |
| | Windows driver stable | System reliability | Driver test |
| **Network Infrastructure** | All devices on same LAN | Real-time sync requirement | Traceroute/ping test |
| | 100 Mbps bandwidth | Component communication | Speed test |
| **Third-party Services** | 8x8 SIP Central | SIP interop | Account verification |
| | [Other integrations] | [Impact] | [Verification] |

## Assumptions (from SOW Section 5 → Translated to Requirements)

| Assumption | Formalized As | Risk | Mitigation |
|-----------|---------------|----|-----------|
| "Biostation compatible with 8x8 SIP" | System shall support SIP protocol | If incompatible: Scope change | Pre-project compatibility test |
| "Adaptive Recognition firmware stable" | System assumes v5.0+ stability | If unstable: Enrollment fails | Firmware version lock + test |
| "All devices on same network" | System assumes LAN connectivity | If not: Latency issues | Network topology documentation |
```

---

## Response Format (CRITICAL)

Your response MUST include:

1. **Infrastructure Layers Summary** — Compute, storage, network, software stack, development env (table format)
2. **Performance Baselines** — All NFRs mapped to measurable targets
3. **Software Stack Specification** — Languages, frameworks, databases, monitoring tools
4. **Deployment Specifications** — Dev/Staging/Prod environment specs
5. **External Dependencies** — From SOW + Software Vision
6. **Validation & Testing Plan** — Load tests, performance tests, DR tests
7. **Assumptions Formalized** — From SOW Section 5 as requirements

**⚠️ INVALID Response:** Only listing items without detailed specifications.  
**✅ VALID Response:** Complete tables, performance metrics, deployment architecture, testing procedures.

---

## Output Artifacts

Create the following files in `project-planning/` folder:

```
project-planning/
├── system-requirements.md              # Main artifact (tables + specs)
├── infrastructure-specification.md     # Detailed infrastructure layers
├── software-stack.md                   # Tech stack with versions
├── development-environment-setup.md    # How-to for dev team
├── performance-baselines.md            # Testable metrics from NFRs
├── deployment-targets.md               # Dev/Staging/Prod specs
└── external-dependencies.md            # SOW assumptions + integrations
```

---

## Key Principles

1. **NFR-Driven:** Every infrastructure requirement traces back to an NFR
2. **SOW-Aligned:** Incorporate Section 4 requirements and Section 5 assumptions
3. **Testable:** Every specification must be measurable/verifiable
4. **Environment-Specific:** Define dev, staging, and production separately
5. **Dependency-Aware:** Document external systems and constraints
6. **Downstream-Ready:** Outputs inform estimation (Phase 2b), roles (Phase 2d), risk management

---

## Integration with Project Planning Phase

### Feeds Into (Downstream)
- **Assumptions & Constraints Skill (Phase 2b):** External dependencies + risks
- **Estimation Skill (Phase 2c):** Infrastructure setup effort, procurement time
- **Roles & Responsibilities Skill (Phase 2d):** Who manages each infrastructure layer

### Fed By (Upstream)
- **Non-Functional Requirements (Step 5):** Performance, availability, security
- **Software Vision (Step 4):** Technology preferences, architecture
- **SOW (Optional):** Section 4 + Section 5

---

## Example: Eurofiber System Requirements

```markdown
## Eurofiber System Requirements (from SOW v3.03 Section 4)

### Infrastructure Layers

#### Compute
| Component | Requirement | Priority |
|-----------|------------|----------|
| NUC (Local) | Windows 11, Intel i5, 4GB RAM, 128GB SSD | MUST |
| SynApp PC | Windows 11, network connection | MUST |
| BioStation | Compatible with 8x8 SIP | MUST |

#### Network
| Requirement | Value | Priority |
|-----------|-------|----------|
| Bandwidth | 100 Mbps minimum | MUST |
| Latency (kiosk ↔ BioStation) | < 100ms | MUST |

#### Software Stack
| Component | Version | Priority |
|-----------|---------|----------|
| .NET | 6 or higher | MUST |
| SQL Server | 2019 or Azure SQL | MUST |
| BioStation API | v2.0+ | MUST |
| Adaptive Recognition SDK | v5.0+ | MUST |
| 8x8 SIP | SIP protocol support | MUST |

### Performance Baselines (from NFRs)

| NFR | Metric | Target | Validation |
|-----|--------|--------|-----------|
| Enrollment response | < 5 seconds | < 5 sec (p95) | Stopwatch / APM |
| Concurrent kiosk users | 100 | < 2 sec response | Load test |
| Uptime | 99.5% business hours | 99.5% | Monitoring |

### Deployment Environments

**Development:**
- Developer NUC (Windows 11, i5, 4GB RAM)
- Local SQL Server Express

**Production:**
- Client NUC (Windows 11, i5, 4GB RAM)
- Client-hosted SQL Server 2019
- BioStation + Scanner on same LAN
```

---

## Next Steps

After completing System Requirements:

1. **Use Assumptions & Constraints Skill** (Phase 2b)
   - Identify risks from external dependencies
   - Plan mitigation strategies
   - Define change management rules

2. **Use Estimation Skill** (Phase 2c)
   - Calculate infrastructure setup effort
   - Plan procurement lead time
   - Estimate testing/validation effort

3. **Use Roles & Responsibilities Skill** (Phase 2d)
   - Assign infrastructure team members
   - Define ops/infrastructure responsibilities
   - Plan team communication

4. **Project Kickoff**
   - Share infrastructure specs with ops team
   - Provision dev environment for developers
   - Set up monitoring and alerting
   - Execute validation testing plan
