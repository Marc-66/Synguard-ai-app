# STATEMENT OF WORK
## iLOQ CLOUD GATEWAY INTEGRATION

**V. 1.0 - 01/07/2026**  
**SYNGUARD | Always with you**

---

# INHOUDSOPGAVE

1. Project Overzicht
2. Integratieflow
3. Scope
4. Systeemvereisten
5. Aannames
6. Wijzigingsbeheer
7. Op te leveren resultaten
8. Acceptatiecriteria
9. Inschatting
10. Roles & Responsibilities
11. Aanvaarding

---

# 1. PROJECT OVERZICHT

| Item | Beschrijving |
|------|---|
| **Project Naam** | iLOQ Cloud Gateway Integratie |
| **Eindklant** | Synguard Partners (Standaard Product Enhancement) |
| **SOW Datum** | 01/07/2026 |
| **Geschatte project duur** | 12 werkdagen |
| **Doel** | Volledige integratie van iLOQ RF draadloze sloten met het Synguard systeem |
| **Korte omschrijving** | Integratie van iLOQ Cloud Gateway API met Synguard voor bidirectionele synchronisatie van toegangsrechten, realtime logging van eventos en batterijstatusweergave in SynApp. De integratie zal klanten toestaan om hun volledige toegangsbeheer vanuit SynApp te beheren zonder dubbele data-invoer. |

## Omschrijving werk

- Bidirectionele synchronisatie van gebruikersrechten en slotconfiguraties tussen iLOQ Manager en Synguard
- Realtime logging van toegangspogingen, slot opens en configuratiewijzigingen in Synguard
- Batterijstatusweergave van iLOQ RF draadloze sloten in SynApp met waarschuwingen
- Cloud-to-Cloud API integratie via iLOQ Cloud Gateway (geen lokale server-installatie)
- UI/UX integratie: iLOQ iconen in de SynApp boomstructuur
- Versleutelde gegevensoverdracht tussen beide systemen



---

# 2. INTEGRATIEFLOW

## 2.1 Bidirectionele Synchronisatie Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  SynApp (Operator)                   iLOQ Cloud Gateway         │
│  ┌──────────────────────┐            ┌──────────────────────┐  │
│  │ Change Access Rights │──────────>│ Sync to iLOQ Cloud   │  │
│  │                      │            │ (< 5 seconds)        │  │
│  └──────────────────────┘            └──────────────────────┘  │
│           ^                                    │                │
│           │                                    v                │
│  ┌──────────────────────┐            ┌──────────────────────┐  │
│  │ Display Sync Status  │<──────────│ Confirm Changes on   │  │
│  │ & Battery Level      │            │ iLOQ Door Locks      │  │
│  └──────────────────────┘            └──────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 2.2 Realtime Logging Flow

```
Synguard → iLOQ Events → Event Queue → Synguard Logs Database
           (Access attempts, Config changes, Battery updates)
           ↓
      Accessible via SynApp Dashboard
```

## 2.3 Batterijstatus Monitoring Flow

```
iLOQ Door Locks → Battery Status API → Synguard Cache → SynApp Display
     (Polling every 5 min)                              (with alerts)
```

---

# 3. SCOPE

## 3.1 In Scope

### 3.1.1 Bidirectionele Synchronisatie
- Synchronisatie van gebruikersrechten tussen SynApp en iLOQ Cloud
- Synchronisatie van slotconfiguraties en toegangsprofielen
- Automatische detectie van wijzigingen in beide systemen
- Wijzigingen worden verwerkt binnen 5 seconden
- Offline fallback: Systeem blijft functioneren op het slot zelfs als cloud onbereikbaar is

**API Endpoints:**
- `POST /sync/access-rights` - Zugrijven synchroniseren
- `POST /sync/configurations` - Configuraties synchroniseren
- `GET /sync/status` - Sync status opvragen
- `POST /sync/verify` - Wijzigingen verifiëren

### 3.1.2 Realtime Logging
- Loggen van alle toegangspogingen (geslaagd/mislukt)
- Loggen van configuratiewijzigingen
- Loggen van batterijstatusveranderingen
- Loggen van synchronisatiefouten
- Logs zijn doorzoekbaar en filterable in SynApp
- Logs worden opgeslagen in Synguard database

### 3.1.3 Batterijstatusweergave
- Batterijstatus van elk iLOQ RF slot wordt zichtbaar in SynApp
- Automatische waarschuwingen wanneer batterij < 20%
- Kritieke waarschuwing wanneer batterij < 5%
- iLOQ iconen geïntegreerd in de SynApp boomstructuur
- Kleurcodering: Groen (OK), Oranje (Low), Rood (Critical)

### 3.1.4 Cloud-to-Cloud Integratie
- Integratie via iLOQ Cloud Gateway API (geen lokale server-installatie)
- Authentificatie via OAuth 2.0 tokens
- Gegevensversleuteling in transit (TLS 1.3 minimum)
- API rate limits en retry logic geïmplementeerd

### 3.1.5 Beveiliging & Versleuteling
- Alle gegevensoverdracht versleuteld (TLS 1.3)
- iLOQ API credentials secure opgeslagen
- Audit trail van alle API calls
- Compliance met GDPR en locale data protection

### 3.1.6 UI/UX Integratie
- iLOQ iconen in de SynApp boomstructuur
- Batterijstatus indicator in het slot item overzicht
- Real-time sync status in de SynApp toolbar
- Logging dashboard met zoek- en filtermogelijkheden
- Error notifications bij sync fouten

## 3.2 Out of Scope

- iLOQ Manager ontwikkelingen of configuratie
- Fysieke installatie van iLOQ sloten
- Fysieke installatie van iLOQ BioStations (als van toepassing)
- Hardware ondersteuning of maintenance
- SynApp Windows/iOS/Android native app updates buiten scope van deze integratie
- Migratie van bestaande iLOQ data naar Synguard

---

# 4. SYSTEEMVEREISTEN

### Synguard Platform
- Synguard Platform versie 3.0 of hoger
- SQL Server 2019 of hoger (database voor logs)
- .NET Framework 6.0 minimum

### iLOQ Systeem
- iLOQ S5 of S50 slot series
- iLOQ Cloud Gateway API beschikbaar
- Minimaal iLOQ firmware versie 5.0+

### Netwerkverbinding
- Stabiele internetverbinding (minimaal 5 Mbps)
- DNS resolution voor iLOQ Cloud endpoints
- Firewall rules voor HTTPS outbound (port 443)

### Externe Afhankelijkheden
- iLOQ Cloud Gateway API (beschikbaarheid)
- iLOQ API credentials en tenant setup
- OAuth 2.0 provider configuratie

---

# 5. AANNAMES

- iLOQ Cloud Gateway API is stabiel en betrouwbaar (99.9% uptime SLA)
- Internetverbinding is permanent beschikbaar en stabiel
- iLOQ sloten worden correct geconfigureerd in iLOQ Manager voorafgaand aan integratie
- Synguard database server heeft voldoende capaciteit voor event logging
- Geen breaking changes in iLOQ Cloud Gateway API during project
- Synguard admin user heeft voldoende permissies voor integratie setup
- Data synchronisatie mag met max 5 seconden delay

---

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

---

# 7. OP TE LEVEREN RESULTATEN

### 7.1 iLOQ Cloud Gateway Integration Module
- Volledig geïmplementeerde integratie module
- Source code versie-beheerd in Azure DevOps
- Documentatie van alle API endpoints

### 7.2 Bidirectional Sync Engine
- Real-time synchronisatie component
- Conflict resolution logic
- Offline queue management

### 7.3 Event Logging System
- Event capture en storage
- Search en filter capabilities
- Dashboard voor event viewing

### 7.4 Battery Monitoring Service
- Polling service voor batterijstatus
- Alert engine
- Status visualization in SynApp

### 7.5 SynApp UI Enhancements
- iLOQ icon integration in tree structure
- Battery status display
- Real-time sync indicator
- Event logging dashboard

### 7.6 Database Schema Updates
- Event logging tables
- iLOQ sync state tables
- Battery status history tables

### 7.7 Documentation & Deployment
- Technical architecture documentation
- Deployment guide (dev/staging/production)
- API documentation
- User guide for battery monitoring
- Troubleshooting guide

### 7.8 Testing & QA
- Unit test suite (target: 80%+ code coverage)
- Integration test scenarios
- Load testing report
- Security assessment report

---

# 8. ACCEPTATIECRITERIA

## 8.1 Bidirectionale Synchronisatie
- ✓ Wijzigingen in SynApp worden binnen 5 seconden gesynchroniseerd naar iLOQ Cloud
- ✓ Wijzigingen in iLOQ Manager worden binnen 5 seconden gesynchroniseerd naar SynApp
- ✓ Geen data verlies bij synchronisatie
- ✓ Offline mode werkt: sloten blijven functioneren als cloud onbereikbaar

## 8.2 Realtime Logging
- ✓ Alle toegangspogingen worden gelogd (100% capture rate)
- ✓ Logs zijn binnen 3 seconden zichtbaar in SynApp dashboard
- ✓ Logs kunnen gefilterd worden op: timestamp, usuario, slot, actie, status
- ✓ Logs zijn persistent en audit-proof (niet verwijderbaar door gebruiker)

## 8.3 Batterijstatusweergave
- ✓ Batterijstatus wordt correct weergegeven per slot (< 1 minuut vertraging)
- ✓ Waarschuwingen verschijnen wanneer batterij < 20% (oranje) en < 5% (rood)
- ✓ iLOQ iconen zijn duidelijk zichtbaar in SynApp tree structure
- ✓ Batterijstatus updates dagelijks of bij willekeurig moment

## 8.4 Cloud-to-Cloud Integratie
- ✓ Zero lokale server installatie vereist
- ✓ Alle communicatie via iLOQ Cloud Gateway API
- ✓ Geen firewall inbound rules nodig
- ✓ Deployment time < 1 uur

## 8.5 Beveiliging
- ✓ Alle API calls zijn versleuteld (TLS 1.3)
- ✓ Credentials zijn nooit blootgesteld in logs
- ✓ Audit trail beschikbaar van alle API operations
- ✓ GDPR compliance verified

## 8.6 Performance
- ✓ Sync latency: < 5 seconden (p95)
- ✓ Log query response: < 2 seconden
- ✓ Battery polling: < 5 minuten staleness
- ✓ Support 1000+ simultaneous locked doors
- ✓ Support 100+ concurrent SynApp users

---

# 9. INSCHATTING

## Effort per Discipline

| Discipline | Uren | Uurtarief | Totaal |
|---|---:|---:|---:|
| Solution Architecture & Design | 8 | €125 | €1.000 |
| Synguard Backend Development (API) | 32 | €110 | €3.520 |
| SynApp Frontend Development (UI) | 24 | €110 | €2.640 |
| Database Engineering | 12 | €110 | €1.320 |
| QA / Test & Validation | 20 | €95 | €1.900 |
| Security & Compliance Review | 8 | €125 | €1.000 |
| Project Management & Documentation | 8 | €125 | €1.000 |
| **TOTAAL** | **112** | | **€12.380** |

## Fase-indeling

| Fase | Duur | Deliverables |
|---|---|---|
| **Phase 1: Architecture & Design** | 2 dagen | Design doc, API spec, DB schema |
| **Phase 2: Backend Integration** | 4 dagen | API implementation, sync engine |
| **Phase 3: Frontend & UI** | 3 dagen | SynApp enhancements, battery display |
| **Phase 4: QA & Testing** | 2 dagen | Test reports, security assessment |
| **Phase 5: Deployment & Documentation** | 1 dag | Production deployment, user guide |

---

# 10. ROLES & RESPONSIBILITIES

| Rol | Organisatie | Verantwoordelijkheden |
|---|---|---|
| **Project Manager** | Synguard | Projectleiding, status reports, change management |
| **Solution Architect** | Synguard | Architecture design, technical decisions, API spec |
| **Backend Developer (2x)** | Synguard | API implementation, sync engine, logging system |
| **Frontend Developer** | Synguard | SynApp UI integration, battery display, UX |
| **QA Engineer** | Synguard | Test planning, test execution, issue tracking |
| **Security Officer** | Synguard | Security review, encryption, compliance check |
| **Product Owner** | Synguard | Requirements owner, acceptance criteria, go/no-go |
| **iLOQ Technical Contact** | iLOQ (Partner) | API support, technical guidance, credentials provision |

---

# 11. AANVAARDING

Dit Statement of Work beschrijft de scope, deliverables, planning en kosten voor de iLOQ Cloud Gateway integratie project.

**Goedkeuring door:**

| Rol | Naam | Datum | Handtekening |
|---|---|---|---|
| Product Owner | _____________ | _____________ | _____________ |
| Project Manager | _____________ | _____________ | _____________ |
| Customer | _____________ | _____________ | _____________ |

---

## Opmerkingen & Bijlagen

- Verdere vragen over scope: neem contact op met Product Owner
- Bijlagen: iLOQ Cloud Gateway API documentatie, Synguard Integration Guidelines
- Versie history: V1.0 - Initial SOW created - 01/07/2026

---

**Einde Statement of Work**
{
    "cust_input": "\"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten...\"",
    "cust_req": "# Customer Requirements Document (CRD)\n\n## Samenvatting\n\nDit document beschrijft de vereisten voor de integratie van iLOQ RF draadloze sloten met het Synguard systeem. De huidige situatie vereist dat klanten werken met twee aparte systemen: iLOQ Manager en Synguard. De klant vraagt om een volledige integratie die een naadloze werking tussen beide systemen mogelijk maakt. De gewenste functionaliteiten omvatten bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus in de SynApp.\n\n## Customer Needs\n\n- **CN-001**: De klant wil een bidirectionele synchronisatie tussen iLOQ Manager en Synguard om gegevens consistent te houden in beide systemen.\n- **CN-002**: De klant heeft behoefte aan realtime logging van gebeurtenissen om de veiligheid en het beheer van de sloten te verbeteren.\n- **CN-003**: De klant wil de batterijstatus van de iLOQ RF draadloze sloten kunnen bekijken in de SynApp voor effici\u00ebnt onderhoud en beheer.\n\n## Functionele Eisen\n\n1. **Bidirectionele Synchronisatie (FE-001)**\n   - Het systeem moet gegevens automatisch synchroniseren tussen iLOQ Manager en Synguard.\n   - Wijzigingen in gebruikersrechten, slotconfiguraties en andere relevante gegevens moeten in beide systemen worden bijgewerkt zonder handmatige tussenkomst.\n\n2. **Realtime Logging (FE-002)**\n   - Het systeem moet alle gebeurtenissen, zoals toegangspogingen en wijzigingen in slotconfiguraties, in realtime loggen.\n   - Gebruikers moeten toegang hebben tot deze logs via de Synguard interface voor monitoring en analyse.\n\n3. **Batterijstatus Weergave (FE-003)**\n   - De batterijstatus van elk iLOQ RF draadloos slot moet zichtbaar zijn in de SynApp.\n   - Het systeem moet waarschuwingen genereren wanneer de batterijstatus onder een bepaald niveau komt.\n\n## Niet-functionele Eisen\n\n1. **Betrouwbaarheid (NFE-001)**\n   - De synchronisatie en logging moeten met een hoge mate van betrouwbaarheid functioneren, met minimale downtime.\n\n2. **Prestaties (NFE-002)**\n   - De synchronisatie en logging moeten binnen enkele seconden plaatsvinden om realtime functionaliteit te garanderen.\n\n3. **Gebruiksvriendelijkheid (NFE-003)**\n   - De interface voor het bekijken van logs en batterijstatus moet intu\u00eftief en gemakkelijk te navigeren zijn voor gebruikers van alle technische niveaus.\n\n4. **Veiligheid (NFE-004)**\n   - Gegevensoverdracht tussen iLOQ Manager en Synguard moet versleuteld zijn om de veiligheid van gevoelige informatie te waarborgen.\n\n5. **Compatibiliteit (NFE-005)**\n   - De integratie moet compatibel zijn met de bestaande versies van iLOQ Manager en Synguard zonder dat er grote systeemupgrades nodig zijn.",
    "tech_req": "## Technische Specificaties\n\n### Overzicht\n\nDeze technische specificaties beschrijven de integratie van iLOQ RF draadloze sloten met het Synguard systeem via de iLOQ Cloud Gateway API. De integratie zal zorgen voor bidirectionele synchronisatie, realtime logging, en batterijstatusweergave in de SynApp. De integratie zal cloud-to-cloud plaatsvinden zonder lokale server-installatie.\n\n### Architectuur\n\n1. **Integratie Methode**\n   - **Cloud-to-Cloud Integratie**: De integratie zal plaatsvinden via de iLOQ Cloud Gateway API. Er zal geen lokale server-installatie zijn, wat betekent dat alle communicatie en gegevensoverdracht via de cloud zal verlopen.\n\n2. **Gegevens Synchronisatie**\n   - **Bidirectionele Synchronisatie**: Gegevens zoals gebruikersrechten en slotconfiguraties worden automatisch gesynchroniseerd tussen iLOQ Manager en Synguard. Dit wordt bereikt door gebruik te maken van de API's van beide systemen om wijzigingen in realtime te detecteren en door te voeren.\n\n3. **Logging Mechanisme**\n   - **Realtime Logging**: Alle gebeurtenissen, zoals toegangspogingen en configuratiewijzigingen, worden in realtime gelogd. Deze logs zijn toegankelijk via de Synguard interface voor monitoring en analyse.\n\n4. **Batterijstatus Monitoring**\n   - **Batterijstatus Weergave**: De batterijstatus van elk iLOQ RF draadloos slot wordt weergegeven in de SynApp. Er worden waarschuwingen gegenereerd wanneer de batterijstatus onder een bepaald niveau komt.\n\n### UI/UX\n\n- **SynApp Boomstructuur**: iLOQ iconen worden ge\u00efntegreerd in de SynApp boomstructuur om gebruikers een visuele indicatie te geven van de status van de sloten en hun batterijstatus.\n\n### Veiligheid\n\n- **Gegevensversleuteling**: Alle gegevensoverdracht tussen iLOQ Manager en Synguard wordt versleuteld om de veiligheid van gevoelige informatie te waarborgen.\n\n### Compatibiliteit\n\n- **Systeemcompatibiliteit**: De integratie is compatibel met de bestaande versies van iLOQ Manager en Synguard zonder dat er grote systeemupgrades nodig zijn.\n\n## Traceability Matrix\n\n```markdown\n| FR/NFR ID | Traces To CN | Description                                           | Technische Architectuur Component | QA / Test Scenario                                          |\n|-----------|--------------|-------------------------------------------------------|-----------------------------------|-------------------------------------------------------------|\n| FE-001    | CN-001       | Bidirectionele synchronisatie tussen systemen         | Cloud-to-Cloud Integratie         | Test synchronisatie van gebruikersrechten en configuraties  |\n| FE-002    | CN-002       | Realtime logging van gebeurtenissen                   | Logging Mechanisme                | Test realtime logging van toegangspogingen en wijzigingen   |\n| FE-003    | CN-003       | Weergave van batterijstatus in SynApp                 | Batterijstatus Monitoring         | Test batterijstatus weergave en waarschuwingen              |\n| NFE-001   | CN-001, CN-002, CN-003 | Betrouwbare synchronisatie en logging             | Gegevensversleuteling             | Test betrouwbaarheid en uptime van synchronisatie en logging|\n| NFE-002   | CN-001, CN-002 | Prestaties van synchronisatie en logging binnen seconden | Cloud-to-Cloud Integratie         | Test snelheid van synchronisatie en logging                 |\n| NFE-003   | CN-003       | Gebruiksvriendelijke interface voor logs en batterijstatus | UI/UX                             | Test gebruiksvriendelijkheid van de interface               |\n| NFE-004   | CN-001, CN-002, CN-003 | Versleutelde gegevensoverdracht                   | Gegevensversleuteling             | Test versleuteling van gegevensoverdracht                   |\n| NFE-005   | CN-001, CN-002, CN-003 | Compatibiliteit met bestaande systemen            | Systeemcompatibiliteit            | Test compatibiliteit met bestaande versies van systemen     |\n```\n\nDeze specificaties en traceability matrix bieden een gedetailleerd overzicht van de technische vereisten en testscenario's voor de integratie van iLOQ RF draadloze sloten met het Synguard systeem.",
    "sow_body": "# Statement of Work (SoW)\n\n**Datum:** 01-07-2026  \n**Status:** Draft / For Review\n\n## 1. Projectdoel\n\nHet doel van dit project is om een naadloze integratie te realiseren tussen iLOQ RF draadloze sloten en het Synguard systeem. Deze integratie zal zorgen voor bidirectionele synchronisatie van gegevens, realtime logging van gebeurtenissen, en batterijstatusweergave in de SynApp. Dit zal de effici\u00ebntie en veiligheid van toegangsbeheer verbeteren zonder de noodzaak van lokale server-installaties.\n\n## 2. Project Scope\n\n### Functionele Vereisten (FR) en Acceptatiecriteria\n\n- **FR-001: Bidirectionele Synchronisatie**\n  - **Beschrijving:** Synchronisatie van gebruikersrechten en slotconfiguraties tussen iLOQ Manager en Synguard.\n  - **Acceptatiecriteria:** Wijzigingen in gebruikersrechten en configuraties worden binnen 5 seconden in beide systemen weergegeven.\n\n- **FR-002: Realtime Logging**\n  - **Beschrijving:** Loggen van toegangspogingen en configuratiewijzigingen in realtime.\n  - **Acceptatiecriteria:** Alle gebeurtenissen worden binnen 3 seconden na optreden in de Synguard interface weergegeven.\n\n- **FR-003: Batterijstatus Weergave**\n  - **Beschrijving:** Weergave van de batterijstatus van iLOQ RF sloten in de SynApp.\n  - **Acceptatiecriteria:** Batterijstatus wordt correct weergegeven en waarschuwingen worden gegenereerd wanneer de status onder 20% komt.\n\n## 3. Technische Scope & Integratiearchitectuur\n\n- **Integratie Methode:** Cloud-to-Cloud Integratie via de iLOQ Cloud Gateway API.\n- **Gegevens Synchronisatie:** Bidirectionele synchronisatie van gebruikersrechten en slotconfiguraties.\n- **Logging Mechanisme:** Realtime logging van toegangspogingen en configuratiewijzigingen.\n- **Batterijstatus Monitoring:** Weergave van batterijstatus en waarschuwingen in de SynApp.\n- **Veiligheid:** Gegevensversleuteling voor alle gegevensoverdracht.\n- **Compatibiliteit:** Compatibel met bestaande versies van iLOQ Manager en Synguard.\n\n## 4. Deliverables\n\n- **D-001:** Volledige integratie van iLOQ RF sloten met Synguard.\n- **D-002:** Functionerende bidirectionele synchronisatie.\n- **D-003:** Realtime logging functionaliteit.\n- **D-004:** Batterijstatus weergave in SynApp.\n- **D-005:** Gegevensversleuteling voor veilige gegevensoverdracht.\n- **D-006:** Documentatie en handleidingen voor eindgebruikers.\n\n## 5. Out of Scope\n\n- Lokale server-installaties.\n- Hardware-upgrades voor bestaande systemen.\n- Ondersteuning voor niet-iLOQ sloten.\n\n## 6. Rollen & Verantwoordelijkheden\n\n- **Projectmanager:** Verantwoordelijk voor de algehele projectco\u00f6rdinatie en communicatie.\n- **Technisch Lead:** Verantwoordelijk voor de technische implementatie en integratie.\n- **QA Specialist:** Verantwoordelijk voor het testen van de functionaliteiten en het waarborgen van de kwaliteit.\n- **Business Analyst:** Verantwoordelijk voor het verzamelen van vereisten en het opstellen van acceptatiecriteria.\n\n## 7. Planning & Mijlpalen\n\n```markdown\n| Mijlpaal                  | Verwachte Datum |\n|---------------------------|-----------------|\n| Start van het project     | 01-08-2026      |\n| Voltooiing technische ontwerp | 15-09-2026  |\n| Implementatie voltooid    | 01-11-2026      |\n| Testfase afgerond         | 15-12-2026      |\n| Oplevering en training    | 01-01-2027      |\n```\n\n## 8. Afhankelijkheden & Risico's\n\n- **Afhankelijkheden:**\n  - Beschikbaarheid van iLOQ Cloud Gateway API.\n  - Toegang tot Synguard systeem voor integratie.\n\n- **Risico's:**\n  - Vertragingen in API-beschikbaarheid kunnen de projectplanning be\u00efnvloeden.\n  - Onvoorziene compatibiliteitsproblemen met bestaande systemen.\n\n## 9. Change Request Procedure\n\nAlle wijzigingen in de projectscope moeten schriftelijk worden ingediend en goedgekeurd door de projectmanager. Wijzigingen kunnen leiden tot herziening van de planning en kosten.\n\n## 10. Acceptatie & Sign-Off\n\nDe projectresultaten worden als voltooid beschouwd wanneer alle deliverables zijn opgeleverd en goedgekeurd door de belanghebbenden. Formele acceptatie en sign-off worden gedocumenteerd door de projectmanager.",
    "current_filepath": "outputs/generated_srs\\20260701_1506_klant_vraagt_om_een_volledige.md",
    "development_type": "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
    "business_driver": "Strategic Feature for Market",
    "is_customer_specific": "Standard Product Enhancement (Reusable)",
    "verticals": [
        "Healthcare",
        "Education"
    ],
    "benchmark_competitor": "Nedap AEOS Locker Management",
    "link_project": "",
    "link_product": "",
    "total_project_value": 50,
    "chargeable_value": 7,
    "potential_yearly_revenue": 12,
    "resolved_problem": "",
    "value_end_customer": "Geen dubbele data-invoer; direct blokkeren van iLOQ sleutels in SynApp.",
    "value_partner": "Kan totaaloplossing (online + draadloos) aanbieden onder \u00e9\u00e9n SynApp platform.",
    "value_synguard": "Verhoogt licentiewaarde per deur in SynApp zonder noodzaak van fysieke SynCon hardware",
    "current_situation": "Klanten werken in twee aparte systemen (iLOQ Manager + Synguard).",
    "overall_workflow": "\"As an operator, I change access rights in SynApp and expect realtime sync to iLOQ Cloud.\"",
    "desired_functionality": "1. Bidirectionele sync\n2. Realtime logging\n3. Batterijstatus in SynApp\n",
    "integration_details": "Systeem: iLOQ S5/S50.\nAPI: Cloud Gateway API.\nWebsite: iloq.com",
    "ui_ux_expectations": "iLOQ iconen in de SynApp boomstructuur.",
    "acceptance_criteria": "Sync verwerkt binnen 5 seconden. Systeem blijft offline functioneren op het slot.",
    "constraints_conditions": "Cloud-to-cloud via iLOQ Gateway. Geen lokale server-installatie.",
    "tender_text": "\"N.v.t. voor deze generieke validatie.\"",
    "matrix_data": [
        {
            "FR/NFR ID": "FE-001",
            "Traces To CN": "CN-001",
            "Description": "Bidirectionele synchronisatie tussen systemen",
            "Technische Architectuur Component": "Cloud-to-Cloud Integratie",
            "QA / Test Scenario (Acceptatiecriterium)": "Test synchronisatie van gebruikersrechten en configuraties"
        },
        {
            "FR/NFR ID": "FE-002",
            "Traces To CN": "CN-002",
            "Description": "Realtime logging van gebeurtenissen",
            "Technische Architectuur Component": "Logging Mechanisme",
            "QA / Test Scenario (Acceptatiecriterium)": "Test realtime logging van toegangspogingen en wijzigingen"
        },
        {
            "FR/NFR ID": "FE-003",
            "Traces To CN": "CN-003",
            "Description": "Weergave van batterijstatus in SynApp",
            "Technische Architectuur Component": "Batterijstatus Monitoring",
            "QA / Test Scenario (Acceptatiecriterium)": "Test batterijstatus weergave en waarschuwingen"
        },
        {
            "FR/NFR ID": "NFE-001",
            "Traces To CN": "CN-001, CN-002, CN-003",
            "Description": "Betrouwbare synchronisatie en logging",
            "Technische Architectuur Component": "Gegevensversleuteling",
            "QA / Test Scenario (Acceptatiecriterium)": "Test betrouwbaarheid en uptime van synchronisatie en logging"
        },
        {
            "FR/NFR ID": "NFE-002",
            "Traces To CN": "CN-001, CN-002",
            "Description": "Prestaties van synchronisatie en logging binnen seconden",
            "Technische Architectuur Component": "Cloud-to-Cloud Integratie",
            "QA / Test Scenario (Acceptatiecriterium)": "Test snelheid van synchronisatie en logging"
        },
        {
            "FR/NFR ID": "NFE-003",
            "Traces To CN": "CN-003",
            "Description": "Gebruiksvriendelijke interface voor logs en batterijstatus",
            "Technische Architectuur Component": "UI/UX",
            "QA / Test Scenario (Acceptatiecriterium)": "Test gebruiksvriendelijkheid van de interface"
        },
        {
            "FR/NFR ID": "NFE-004",
            "Traces To CN": "CN-001, CN-002, CN-003",
            "Description": "Versleutelde gegevensoverdracht",
            "Technische Architectuur Component": "Gegevensversleuteling",
            "QA / Test Scenario (Acceptatiecriterium)": "Test versleuteling van gegevensoverdracht"
        },
        {
            "FR/NFR ID": "NFE-005",
            "Traces To CN": "CN-001, CN-002, CN-003",
            "Description": "Compatibiliteit met bestaande systemen",
            "Technische Architectuur Component": "Systeemcompatibiliteit",
            "QA / Test Scenario (Acceptatiecriterium)": "Test compatibiliteit met bestaande versies van systemen"
        }
    ],
    "sow_budget_data": [
        {
            "Discipline / Jira Component": "Solution Architecture & Design",
            "Geschatte Uren": 8,
            "Uurtarief (\u20ac)": 125
        },
        {
            "Discipline / Jira Component": "SynApp Front-end Development (UI)",
            "Geschatte Uren": 24,
            "Uurtarief (\u20ac)": 110
        },
        {
            "Discipline / Jira Component": "SynCon Firmware Integration",
            "Geschatte Uren": 16,
            "Uurtarief (\u20ac)": 110
        },
        {
            "Discipline / Jira Component": "Database & Security Engineering",
            "Geschatte Uren": 12,
            "Uurtarief (\u20ac)": 110
        },
        {
            "Discipline / Jira Component": "QA / Test Automation & Validation",
            "Geschatte Uren": 16,
            "Uurtarief (\u20ac)": 95
        },
        {
            "Discipline / Jira Component": "Project Management & Documentation",
            "Geschatte Uren": 8,
            "Uurtarief (\u20ac)": 125
        }
    ]
}