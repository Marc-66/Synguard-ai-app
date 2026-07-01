# System Requirements Reference Guide

## Overview

This guide provides practical examples and templates for using the System Requirements skill (Phase 2a).

---

## Example 1: Eurofiber Project System Requirements

### Input: Eurofiber NFRs + SOW Section 4

**NFRs from Step 5:**
- NFR-001: Response time < 5 seconds (enrollment process)
- NFR-002: Support 50 concurrent kiosk users
- NFR-003: 99.9% uptime during business hours
- NFR-004: Encrypt all personal data at rest and in transit

**SOW Section 4 System Requirements:**
```
NUC für SynReg:
- Windows 11
- Intel Core i5 (or higher)
- 4 GB RAM
- 128 GB SSD

Kompatibilität:
- Biostation with 8x8 SIP
- Adaptive Recognition Osmond scanner
- Same network connectivity
```

### Output: Eurofiber System Requirements Specification

```markdown
# Eurofiber System Requirements

## Infrastructure Layers

### Layer 1: Compute

| Component | Requirement | Priority | Rationale |
|-----------|------------|----------|-----------|
| **Local NUC (SynReg)** | | | |
| OS | Windows 11 Pro | MUST | SOW Section 4 |
| Processor | Intel Core i5 (6-core, 2.4GHz+) | MUST | SOW Section 4 + NFR-002 (50 concurrent) |
| RAM | 8 GB (minimum 4GB to app) | MUST | Local enrollment + document processing |
| Storage | 256 GB SSD | MUST | OS + app + document cache (10-min retention) |
| | | | |
| **SynApp PC (BioStation Controller)** | | | |
| OS | Windows 11 | MUST | Synguard SynAppWindows requirement |
| Processor | Intel i5 (4-core minimum) | SHOULD | Each PC controls ~10 BioStations |
| RAM | 4 GB minimum | SHOULD | Window management for 10 instances |

### Layer 2: Storage & Database

| Component | Requirement | Priority | Rationale |
|-----------|------------|----------|-----------|
| **Local Database** | | | |
| Engine | SQL Server 2019 (or Express) | MUST | Synguard standard |
| Edition | Standard or Express | SHOULD | Local operational use |
| Backup | Daily automated (7-day retention) | SHOULD | Visitor/access data recovery |
| Storage | Local SSD (part of NUC 256GB) | MUST | Fast document query access |

### Layer 3: Network & Connectivity

| Component | Requirement | Priority | Rationale |
|-----------|------------|----------|-----------|
| Bandwidth | 100 Mbps minimum (local LAN) | MUST | SOW Section 5: "All devices on same network" |
| Latency | < 100ms (kiosk ↔ BioStation) | MUST | From NFR-001 (enrollment response time) |
| Latency | < 50ms (NUC ↔ Scanner) | MUST | Document scanning responsiveness |
| Connectivity | Wired Ethernet preferred | SHOULD | Stability for continuous operation |
| Redundancy | Single network (no failover specified) | COULD | Future enhancement per SOW change mgmt |

### Layer 4: Software Stack

| Component | Version/Edition | Priority | Notes |
|-----------|-----------------|----------|-------|
| **.NET Runtime** | | | |
| Framework | .NET 6 or higher | MUST | Synguard modern standard |
| C# | C# 10+ | MUST | Language compatibility |
| | | | |
| **Synguard Components** | | | |
| SynReg | Current version | MUST | Document scanning UI |
| SynAppWindows | Current version | MUST | BioStation enrollment orchestration |
| | | | |
| **External Integrations** | | | |
| Adaptive Recognition SDK | v5.0+ | MUST | SOW Section 5: "firmware stable" |
| BioStation API | v2.0+ | MUST | REST API for enrollment commands |
| 8x8 SIP | SIP protocol | MUST | SIP calling from BioStation |
| | | | |
| **Security** | | | |
| TLS | 1.3 minimum | MUST | Encrypted communication (NFR-004) |
| Encryption | AES-256 data at rest | MUST | Personal data protection |
| | | | |
| **Monitoring** | | | |
| Event Logging | Windows Event Log | SHOULD | System diagnostics |
| Application Logging | Synguard log files | SHOULD | Troubleshooting |

### Layer 5: Development Environment

| Component | Requirement | Priority | Notes |
|-----------|------------|----------|-------|
| IDE | Visual Studio 2022 | MUST | Synguard C# development |
| SCM | Git + Azure Repos | MUST | Version control |
| Test DB | SQL Server Express (local) | SHOULD | Integration testing |
| Containerization | Docker Desktop | COULD | Consistency with CI/CD |

### Layer 6: Deployment Environments

#### Development
```
Purpose: Feature development, local testing
├── Developer NUC
│   ├── Windows 11 Pro
│   ├── Visual Studio 2022
│   ├── SQL Server Express (local database)
│   └── Synguard SynReg (local instance)
├── Scanner: USB-connected Adaptive Recognition Osmond R
└── Network: Local development network (no external dependencies)
```

#### Test/Staging
```
Purpose: System integration testing, UAT, acceptance testing
├── Client-provided NUC (separate from production)
│   ├── Windows 11
│   ├── SQL Server 2019 (test database, separate schema)
│   └── Synguard SynReg + SynAppWindows
├── Scanner: Connected to NUC for testing
├── BioStation: In lab for enrollment flow testing
└── Network: Isolated or client test network (same LAN as production)
```

#### Production
```
Purpose: Live end-user operation, visitor enrollment
├── Client-provided NUC
│   ├── Windows 11
│   ├── SQL Server 2019 (production database)
│   ├── Synguard SynReg (kiosk UI)
│   └── Synguard SynAppWindows (BioStation controller on separate PC)
├── Scanner: Persistent USB connection to NUC
├── BioStation: Operational units (up to 10 per SynAppWindows PC)
├── Kiosk: Touch screen connected to NUC
└── Network: Client's secure, monitored network
```

---

## Performance Baselines (Testable)

### From NFRs

| NFR | Metric | Target | Test Method | Acceptance |
|-----|--------|--------|------------|-----------|
| NFR-001 | Enrollment flow time | < 5 sec (p95) | Stopwatch + logging | Time from start to "Enrollment complete" |
| | Document scan time | < 2 sec | Scanner timing | From "scan" button to validation |
| | Visitor lookup | < 1 sec | Database profiler | Query < 1 sec on 10k visitors |
| | | | | |
| NFR-002 | Concurrent users | 50 simultaneous | Synthetic load test | 50 kiosk sessions, no errors |
| | Response time under load | < 5 sec (p95) | Load test dashboard | Latency stable at 50 concurrent |
| | | | | |
| NFR-003 | Uptime | 99.9% business hours | Monitoring | Log file analysis of downtime |
| | Recovery time | < 30 minutes | Incident simulation | From failure detection to restored service |
| | | | | |
| NFR-004 | TLS version | 1.3+ | SSL Labs scan | Certificate audit |
| | Encryption | AES-256 | Database audit | Personal data encrypted |

### Validation Testing Plan

#### Unit 1: Enrollment Response Time (NFR-001)
```
Objective: Verify enrollment completes in < 5 seconds

Test Scenario:
1. User taps "Start Enrollment" button
2. System displays document scan UI
3. User scans ID document
4. System validates document (EID/passport/license)
5. System matches visitor (last name + DOB)
6. System initiates BioStation enrollment
7. System displays "Enrollment Complete" or error message

Success Criteria:
- Steps 1-7 complete in < 5 seconds (p95)
- Document validation: < 2 seconds
- Visitor lookup: < 1 second
- No timeout errors

Test Data:
- 100 test visitors in database
- Valid and invalid documents

Execution:
- Manual stopwatch (initial validation)
- Automated timing via logging (ongoing monitoring)
```

#### Unit 2: Concurrency Test (NFR-002)
```
Objective: Verify system handles 50 concurrent kiosk users

Test Scenario:
1. Simulate 50 concurrent user sessions
2. Each session performs enrollment flow
3. Measure response times, errors, resource usage
4. Hold load for 10 minutes
5. Measure database connection usage
6. Measure memory and CPU utilization

Success Criteria:
- 0 HTTP errors (no timeouts, 5xx errors)
- Response time p95 < 5 seconds maintained
- Database connections < 80% of pool
- CPU < 80%, Memory < 85%
- No race conditions or data corruption

Tool: JMeter or Azure Load Testing
Load Profile:
- Ramp: 5 new users/second until 50 reached
- Hold: 50 concurrent × 10 minutes
- Ramp down: Linear

Success Threshold: 95% of requests succeed
```

#### Unit 3: Uptime/Recovery (NFR-003)
```
Objective: Verify 99.9% uptime and < 30 min recovery

Test Scenarios:

Scenario A: Component Restart
- Stop SynReg application
- Measure time to restart and resume operation
- Success: < 2 minutes

Scenario B: Database Connection Loss
- Simulate network interruption (30 seconds)
- Measure application behavior
- Success: Auto-reconnect within 30 sec

Scenario C: Extended Outage
- Stop all services for 1 hour
- Restore and verify data integrity
- Success: All data intact, < 30 min recovery

Monitoring:
- Event log for error/restart events
- Application logging for recovery timestamps
- Monthly uptime calculation

Acceptance: 99.9% uptime = < 43 minutes downtime/month
```

#### Unit 4: Security (NFR-004)
```
Objective: Verify data encryption and secure communication

Test Scenarios:

Scenario A: TLS Certificate
- Verify TLS 1.3+ on all endpoints
- Check certificate chain validity
- Use SSL Labs for audit

Success: Grade A or higher

Scenario B: Data Encryption
- Verify personal data encrypted in database
- Check encryption algorithm: AES-256
- Verify encryption keys stored in Key Vault

Scenario C: Access Control
- Verify unauthorized users cannot access API
- Test authentication (OAuth 2.0)
- Test invalid token rejection

Success: All unauthorized requests rejected (HTTP 403)
```

---

## External Dependencies & Risks

### Eurofiber Specific

| Dependency | Status | Risk Level | Mitigation |
|-----------|--------|-----------|-----------|
| **BioStation v8x8 SIP Compatibility** | Assumed compatible | HIGH | Pre-project compatibility test by Eurofiber |
| **Adaptive Recognition Firmware** | Must be v5.0+ | MEDIUM | Version lock in configuration |
| **Network Connectivity (Same LAN)** | Assumption | MEDIUM | Network topology documentation before go-live |
| **Windows 11 NUC Stability** | New hardware | LOW | 48-hour stability test before production |
| **SQL Server 2019 License** | Client responsibility | MEDIUM | Verify licensing before deployment |
| **Scanner USB Connection** | Physical hardware | MEDIUM | Redundant cable + frequent testing |

---

## Developer Setup Checklist

### For Local Development

```
□ Install Windows 11 Pro on development machine
□ Install Visual Studio 2022 (Community or higher)
□ Install .NET 6 SDK
□ Install SQL Server Express or LocalDB
□ Install Git
□ Clone Synguard repository
□ Create local database from schema
□ Verify compilation: dotnet build ✓
□ Run unit tests: dotnet test ✓
□ Start local SynReg: dotnet run ✓
□ Test database connectivity ✓
□ Test with sample visitors (10+) ✓
□ Ready for feature development
```

### For Integration Testing

```
□ Deploy to staging NUC
□ Install Windows 11 on NUC
□ Install SQL Server 2019
□ Configure database backup
□ Connect Adaptive Recognition scanner via USB
□ Connect BioStation to same network
□ Verify network latency < 100ms: ping BioStation
□ Run performance baseline tests
□ Load test with 50 concurrent users
□ Verify uptime monitoring
□ Document any issues for change management
```

---

## Deployment Checklist (Operations)

### Pre-Deployment

```
□ Infrastructure specs reviewed by client IT
□ NUC hardware received and verified
□ Windows 11 installed and updated
□ SQL Server 2019 installed with security hardening
□ Network connectivity tested (100 Mbps, <100ms latency)
□ Scanner hardware connected and driver installed
□ BioStation connectivity confirmed
□ TLS certificates installed and verified
□ Database backup strategy configured
□ Monitoring and alerting set up
□ Incident response procedures documented
```

### Production Deployment

```
□ Backup production data (if migrating)
□ Deploy application code to production NUC
□ Configure production database connection
□ Run acceptance tests (full enrollment flow)
□ Performance test: Verify response times
□ Concurrency test: 50 simultaneous users
□ User training completed
□ Go-live support team briefed
□ Monitoring dashboards active
□ Incident escalation procedures ready
□ Sign-off: Client acceptance of infrastructure
```

---

## Quick Reference: Tech Stack Summary

### Eurofiber Tech Stack

```
FRONTEND
└── Windows Kiosk UI (SynReg)
    ├── Platform: Windows Forms / WPF
    ├── Scanner Integration: Adaptive Recognition SDK
    └── BioStation Integration: REST API calls

BACKEND
├── Runtime: .NET 6 (C#)
├── API Framework: ASP.NET Core
├── Web Server: IIS 10 / Kestrel
└── ORM: Entity Framework Core

DATABASE
├── Engine: SQL Server 2019
├── Local Storage: NUC SSD
└── Backup: Daily automated

INTEGRATIONS
├── BioStation API: REST (v2.0+)
├── Scanner SDK: Adaptive Recognition v5.0+
├── SIP: 8x8 SIP protocol
└── Authentication: OAuth 2.0 (future)

INFRASTRUCTURE
├── Compute: Windows 11 NUC (Intel i5, 4GB RAM, 128GB SSD)
├── Network: Local LAN (100 Mbps, <100ms latency)
├── Monitoring: Windows Event Log + app logs
└── Security: TLS 1.3, AES-256 encryption
```

---

## Next Phase: What Feeds Into Estimation

System Requirements outputs feed into **Phase 2b (Assumptions & Constraints)** and **Phase 2c (Estimation)**:

### Estimation Considerations

```
Infrastructure Setup Effort (from System Requirements):
├── NUC configuration & hardening: 1 day
├── SQL Server installation & backup setup: 0.5 days
├── Network validation & testing: 0.5 days
├── Security setup (TLS, encryption keys): 1 day
└── Monitoring/logging configuration: 0.5 days
TOTAL INFRASTRUCTURE SETUP: ~3.5 days

Development Environment Setup:
├── Developer machine configuration: 0.5 day per dev
├── Build tool / IDE setup: 0.25 day per dev
├── Local database setup: 0.25 day per dev
└── Git/CI-CD configuration: 0.5 day team effort
TOTAL: ~1.5 days overhead for 3-person team

Performance & Load Testing:
├── Test environment setup: 1 day
├── Load test execution: 1 day
├── Results analysis & tuning: 1 day
└── Acceptance testing: 1 day
TOTAL TESTING: ~4 days

GRAND TOTAL: Infrastructure + Setup + Testing = ~9 days
(Plus 24 days development + 10 days overhead from SOW = 34 days total)
```
