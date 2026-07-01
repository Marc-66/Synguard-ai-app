"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten..."
[---SPLIT-DOSSIER---]
**Customer Requirements Document (CRD)**

---

**Samenvatting**

Dit document beschrijft de vereisten voor de integratie van iLOQ RF draadloze sloten met het Synguard systeem. Momenteel werken klanten met twee aparte systemen, namelijk iLOQ Manager en Synguard. De klant vraagt om een volledige integratie die de werking van beide systemen naadloos combineert. De belangrijkste functionaliteiten die gewenst zijn, omvatten bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus van de sloten in de SynApp.

---

**Customer Needs**

- **CN-001**: De klant wil een bidirectionele synchronisatie tussen iLOQ Manager en Synguard om gegevensconsistentie te waarborgen.
- **CN-002**: De klant heeft behoefte aan realtime logging van gebeurtenissen om de beveiliging en het beheer te verbeteren.
- **CN-003**: De klant wil de batterijstatus van de iLOQ RF draadloze sloten kunnen bekijken binnen de SynApp voor efficiënt onderhoud en beheer.

---

**Functionele Eisen**

- **FE-001**: Het systeem moet een bidirectionele synchronisatie ondersteunen tussen iLOQ Manager en Synguard, zodat wijzigingen in één systeem automatisch worden doorgevoerd in het andere.
- **FE-002**: Het systeem moet in staat zijn om realtime logging van alle relevante gebeurtenissen te bieden, inclusief toegangspogingen en systeemwijzigingen.
- **FE-003**: De batterijstatus van de iLOQ RF draadloze sloten moet zichtbaar zijn in de SynApp, met duidelijke indicaties van de batterijlevensduur.

---

**Niet-functionele Eisen**

- **NFE-001**: De integratie moet voldoen aan de hoogste beveiligingsstandaarden om de gegevensintegriteit en privacy te waarborgen.
- **NFE-002**: De synchronisatie en logging moeten minimale vertraging hebben om realtime functionaliteit te garanderen.
- **NFE-003**: De gebruikersinterface van de SynApp moet intuïtief en gebruiksvriendelijk zijn, met duidelijke weergave van de batterijstatus en loggegevens.
- **NFE-004**: Het systeem moet schaalbaar zijn om toekomstige uitbreidingen en integraties met andere systemen te ondersteunen.

---

Dit document dient als basis voor de ontwikkeling en implementatie van de integratie tussen iLOQ RF draadloze sloten en het Synguard systeem, met als doel een efficiëntere en gebruiksvriendelijkere ervaring voor de klant te creëren.
[---SPLIT-DOSSIER---]
## Technische Specificaties

### Overzicht

De integratie tussen iLOQ RF draadloze sloten en het Synguard systeem vereist een cloud-to-cloud verbinding via de iLOQ Gateway API. Er is geen lokale server-installatie nodig. De integratie moet zorgen voor bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus van de sloten in de SynApp.

### Systeemarchitectuur

1. **Integratieplatform**: 
   - **Cloud Gateway API**: Gebruik de iLOQ Cloud Gateway API voor communicatie tussen iLOQ Manager en Synguard.
   - **SynApp**: Zorg voor de weergave van iLOQ iconen in de boomstructuur van de SynApp.

2. **Data Synchronisatie**:
   - **Bidirectionele Synchronisatie**: Implementeer een mechanisme dat wijzigingen in iLOQ Manager automatisch synchroniseert met Synguard en vice versa.

3. **Logging en Monitoring**:
   - **Realtime Logging**: Ontwikkel een logging-systeem dat gebeurtenissen zoals toegangspogingen en systeemwijzigingen in realtime registreert.

4. **Batterijstatus Monitoring**:
   - **Batterijstatus Weergave**: Integreer een functie in de SynApp die de batterijstatus van de iLOQ RF draadloze sloten toont.

### Beveiliging

- **Gegevensintegriteit en Privacy**: Zorg ervoor dat de integratie voldoet aan de hoogste beveiligingsstandaarden om de integriteit en privacy van gegevens te waarborgen.

### Prestaties

- **Minimale Vertraging**: Optimaliseer de synchronisatie en logging om minimale vertraging te garanderen voor realtime functionaliteit.

### UI/UX

- **Gebruiksvriendelijke Interface**: Ontwerp een intuïtieve gebruikersinterface voor de SynApp die duidelijke weergave biedt van de batterijstatus en loggegevens.

### Schaalbaarheid

- **Toekomstige Uitbreidingen**: Zorg ervoor dat het systeem schaalbaar is voor toekomstige uitbreidingen en integraties met andere systemen.

## Traceability Matrix

```markdown
| FR/NFR ID | Traces To CN | Description | Technische Architectuur Component | QA / Test Scenario |
|-----------|--------------|-------------|-----------------------------------|--------------------|
| FE-001    | CN-001       | Bidirectionele synchronisatie tussen iLOQ Manager en Synguard | Cloud Gateway API, Data Synchronisatie | Test bidirectionele gegevensoverdracht tussen iLOQ Manager en Synguard |
| FE-002    | CN-002       | Realtime logging van gebeurtenissen | Logging en Monitoring | Verifieer realtime logging van toegangspogingen en systeemwijzigingen |
| FE-003    | CN-003       | Weergave van batterijstatus in SynApp | Batterijstatus Monitoring | Controleer de zichtbaarheid en nauwkeurigheid van de batterijstatus in SynApp |
| NFE-001   | CN-001, CN-002, CN-003 | Voldoen aan beveiligingsstandaarden | Beveiliging | Voer penetratietests uit om de beveiliging van de integratie te evalueren |
| NFE-002   | CN-002       | Minimale vertraging in synchronisatie en logging | Prestaties | Meet de vertragingstijd van synchronisatie en logging |
| NFE-003   | CN-003       | Intuïtieve en gebruiksvriendelijke UI | UI/UX | Beoordeel de gebruiksvriendelijkheid van de SynApp interface |
| NFE-004   | CN-001, CN-002, CN-003 | Schaalbaarheid voor toekomstige uitbreidingen | Schaalbaarheid | Test de prestaties van het systeem onder verhoogde belasting |
```

Deze technische specificaties en traceability matrix bieden een gedetailleerd overzicht van de vereisten en de architectuurcomponenten die nodig zijn voor de succesvolle integratie van iLOQ RF draadloze sloten met het Synguard systeem.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten...\"",
    "cust_req": "**Customer Requirements Document (CRD)**\n\n---\n\n**Samenvatting**\n\nDit document beschrijft de vereisten voor de integratie van iLOQ RF draadloze sloten met het Synguard systeem. Momenteel werken klanten met twee aparte systemen, namelijk iLOQ Manager en Synguard. De klant vraagt om een volledige integratie die de werking van beide systemen naadloos combineert. De belangrijkste functionaliteiten die gewenst zijn, omvatten bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus van de sloten in de SynApp.\n\n---\n\n**Customer Needs**\n\n- **CN-001**: De klant wil een bidirectionele synchronisatie tussen iLOQ Manager en Synguard om gegevensconsistentie te waarborgen.\n- **CN-002**: De klant heeft behoefte aan realtime logging van gebeurtenissen om de beveiliging en het beheer te verbeteren.\n- **CN-003**: De klant wil de batterijstatus van de iLOQ RF draadloze sloten kunnen bekijken binnen de SynApp voor effici\u00ebnt onderhoud en beheer.\n\n---\n\n**Functionele Eisen**\n\n- **FE-001**: Het systeem moet een bidirectionele synchronisatie ondersteunen tussen iLOQ Manager en Synguard, zodat wijzigingen in \u00e9\u00e9n systeem automatisch worden doorgevoerd in het andere.\n- **FE-002**: Het systeem moet in staat zijn om realtime logging van alle relevante gebeurtenissen te bieden, inclusief toegangspogingen en systeemwijzigingen.\n- **FE-003**: De batterijstatus van de iLOQ RF draadloze sloten moet zichtbaar zijn in de SynApp, met duidelijke indicaties van de batterijlevensduur.\n\n---\n\n**Niet-functionele Eisen**\n\n- **NFE-001**: De integratie moet voldoen aan de hoogste beveiligingsstandaarden om de gegevensintegriteit en privacy te waarborgen.\n- **NFE-002**: De synchronisatie en logging moeten minimale vertraging hebben om realtime functionaliteit te garanderen.\n- **NFE-003**: De gebruikersinterface van de SynApp moet intu\u00eftief en gebruiksvriendelijk zijn, met duidelijke weergave van de batterijstatus en loggegevens.\n- **NFE-004**: Het systeem moet schaalbaar zijn om toekomstige uitbreidingen en integraties met andere systemen te ondersteunen.\n\n---\n\nDit document dient als basis voor de ontwikkeling en implementatie van de integratie tussen iLOQ RF draadloze sloten en het Synguard systeem, met als doel een effici\u00ebntere en gebruiksvriendelijkere ervaring voor de klant te cre\u00ebren.",
    "tech_req": "## Technische Specificaties\n\n### Overzicht\n\nDe integratie tussen iLOQ RF draadloze sloten en het Synguard systeem vereist een cloud-to-cloud verbinding via de iLOQ Gateway API. Er is geen lokale server-installatie nodig. De integratie moet zorgen voor bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus van de sloten in de SynApp.\n\n### Systeemarchitectuur\n\n1. **Integratieplatform**: \n   - **Cloud Gateway API**: Gebruik de iLOQ Cloud Gateway API voor communicatie tussen iLOQ Manager en Synguard.\n   - **SynApp**: Zorg voor de weergave van iLOQ iconen in de boomstructuur van de SynApp.\n\n2. **Data Synchronisatie**:\n   - **Bidirectionele Synchronisatie**: Implementeer een mechanisme dat wijzigingen in iLOQ Manager automatisch synchroniseert met Synguard en vice versa.\n\n3. **Logging en Monitoring**:\n   - **Realtime Logging**: Ontwikkel een logging-systeem dat gebeurtenissen zoals toegangspogingen en systeemwijzigingen in realtime registreert.\n\n4. **Batterijstatus Monitoring**:\n   - **Batterijstatus Weergave**: Integreer een functie in de SynApp die de batterijstatus van de iLOQ RF draadloze sloten toont.\n\n### Beveiliging\n\n- **Gegevensintegriteit en Privacy**: Zorg ervoor dat de integratie voldoet aan de hoogste beveiligingsstandaarden om de integriteit en privacy van gegevens te waarborgen.\n\n### Prestaties\n\n- **Minimale Vertraging**: Optimaliseer de synchronisatie en logging om minimale vertraging te garanderen voor realtime functionaliteit.\n\n### UI/UX\n\n- **Gebruiksvriendelijke Interface**: Ontwerp een intu\u00eftieve gebruikersinterface voor de SynApp die duidelijke weergave biedt van de batterijstatus en loggegevens.\n\n### Schaalbaarheid\n\n- **Toekomstige Uitbreidingen**: Zorg ervoor dat het systeem schaalbaar is voor toekomstige uitbreidingen en integraties met andere systemen.\n\n## Traceability Matrix\n\n```markdown\n| FR/NFR ID | Traces To CN | Description | Technische Architectuur Component | QA / Test Scenario |\n|-----------|--------------|-------------|-----------------------------------|--------------------|\n| FE-001    | CN-001       | Bidirectionele synchronisatie tussen iLOQ Manager en Synguard | Cloud Gateway API, Data Synchronisatie | Test bidirectionele gegevensoverdracht tussen iLOQ Manager en Synguard |\n| FE-002    | CN-002       | Realtime logging van gebeurtenissen | Logging en Monitoring | Verifieer realtime logging van toegangspogingen en systeemwijzigingen |\n| FE-003    | CN-003       | Weergave van batterijstatus in SynApp | Batterijstatus Monitoring | Controleer de zichtbaarheid en nauwkeurigheid van de batterijstatus in SynApp |\n| NFE-001   | CN-001, CN-002, CN-003 | Voldoen aan beveiligingsstandaarden | Beveiliging | Voer penetratietests uit om de beveiliging van de integratie te evalueren |\n| NFE-002   | CN-002       | Minimale vertraging in synchronisatie en logging | Prestaties | Meet de vertragingstijd van synchronisatie en logging |\n| NFE-003   | CN-003       | Intu\u00eftieve en gebruiksvriendelijke UI | UI/UX | Beoordeel de gebruiksvriendelijkheid van de SynApp interface |\n| NFE-004   | CN-001, CN-002, CN-003 | Schaalbaarheid voor toekomstige uitbreidingen | Schaalbaarheid | Test de prestaties van het systeem onder verhoogde belasting |\n```\n\nDeze technische specificaties en traceability matrix bieden een gedetailleerd overzicht van de vereisten en de architectuurcomponenten die nodig zijn voor de succesvolle integratie van iLOQ RF draadloze sloten met het Synguard systeem.",
    "sow_body": "# Statement of Work (SoW)\n**Datum:** 01-07-2026  \n**Status:** Draft / For Review\n\n## 1. Projectdoel\nHet doel van dit project is om een naadloze integratie te realiseren tussen de iLOQ RF draadloze sloten en het Synguard systeem. Deze integratie zal een cloud-to-cloud verbinding via de iLOQ Gateway API omvatten, zonder de noodzaak van een lokale server-installatie. Het project streeft naar bidirectionele synchronisatie, realtime logging, en het weergeven van de batterijstatus van de sloten in de SynApp.\n\n## 2. Project Scope\n### Functionele Vereisten (FR) en Acceptatiecriteria\n- **FR-001: Bidirectionele Synchronisatie**\n  - **Beschrijving:** Synchronisatie van wijzigingen tussen iLOQ Manager en Synguard.\n  - **Acceptatiecriteria:** Wijzigingen in iLOQ Manager worden automatisch gesynchroniseerd met Synguard en vice versa.\n  \n- **FR-002: Realtime Logging**\n  - **Beschrijving:** Registratie van gebeurtenissen zoals toegangspogingen en systeemwijzigingen.\n  - **Acceptatiecriteria:** Alle gebeurtenissen worden in realtime geregistreerd en zijn toegankelijk via de SynApp.\n\n- **FR-003: Batterijstatus Weergave**\n  - **Beschrijving:** Toon de batterijstatus van de iLOQ RF draadloze sloten in de SynApp.\n  - **Acceptatiecriteria:** De batterijstatus is zichtbaar en accuraat in de SynApp.\n\n## 3. Technische Scope & Integratiearchitectuur\n- **Integratieplatform:** Gebruik van de iLOQ Cloud Gateway API voor communicatie tussen iLOQ Manager en Synguard.\n- **Data Synchronisatie:** Implementatie van bidirectionele synchronisatie.\n- **Logging en Monitoring:** Ontwikkeling van een realtime logging-systeem.\n- **Batterijstatus Monitoring:** Integratie van batterijstatusweergave in de SynApp.\n- **Beveiliging:** Voldoen aan de hoogste beveiligingsstandaarden voor gegevensintegriteit en privacy.\n- **Prestaties:** Optimalisatie voor minimale vertraging.\n- **UI/UX:** Ontwerp van een gebruiksvriendelijke interface.\n- **Schaalbaarheid:** Voorbereiding voor toekomstige uitbreidingen.\n\n## 4. Deliverables\n- **D-001:** Voltooide integratie van iLOQ en Synguard systemen.\n- **D-002:** Werkend bidirectioneel synchronisatiemechanisme.\n- **D-003:** Functionerend realtime logging-systeem.\n- **D-004:** Ge\u00efntegreerde batterijstatusweergave in SynApp.\n- **D-005:** Beveiligingsrapport met resultaten van penetratietests.\n- **D-006:** UI/UX ontwerpdocumentatie en gebruikerstests.\n\n## 5. Out of Scope\n- Lokale server-installaties.\n- Integratie met andere systemen buiten iLOQ en Synguard.\n- Ondersteuning voor niet-iLOQ sloten.\n\n## 6. Rollen & Verantwoordelijkheden\n- **Projectmanager:** Verantwoordelijk voor de algehele projectco\u00f6rdinatie.\n- **Technisch Lead:** Verantwoordelijk voor de technische architectuur en implementatie.\n- **Ontwikkelaar:** Implementatie van de integratie en functionaliteiten.\n- **Tester:** Uitvoeren van QA en testen van de integratie.\n- **Beveiligingsspecialist:** Uitvoeren van beveiligingsaudits en penetratietests.\n\n## 7. Planning & Mijlpalen\n```markdown\n| Mijlpaal                | Datum       |\n|-------------------------|-------------|\n| Start van het project   | 01-07-2026  |\n| Voltooiing ontwerp      | 15-08-2026  |\n| Voltooiing ontwikkeling | 30-09-2026  |\n| Testfase                | 15-10-2026  |\n| Implementatie           | 01-11-2026  |\n| Projectafsluiting       | 15-11-2026  |\n```\n\n## 8. Afhankelijkheden & Risico's\n- **Afhankelijkheden:**\n  - Beschikbaarheid van iLOQ Gateway API.\n  - Toegang tot Synguard systeem voor integratie.\n  \n- **Risico's:**\n  - Vertraging in API-levering.\n  - Onverwachte technische complicaties.\n  - Beveiligingslekken tijdens de integratie.\n\n## 9. Change Request Procedure\nAlle wijzigingen in de projectscope of specificaties moeten formeel worden aangevraagd via een Change Request formulier. Deze worden beoordeeld door het projectteam en goedgekeurd door de projectmanager voordat implementatie plaatsvindt.\n\n## 10. Acceptatie & Sign-Off\nBij voltooiing van het project worden alle deliverables beoordeeld door de klant. Na goedkeuring wordt een formele sign-off verkregen, waarmee het project officieel wordt afgesloten.",
    "current_filepath": "outputs/generated_srs\\20260701_1523_klant_vraagt_om_een_volledige.md",
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
            "Description": "Bidirectionele synchronisatie tussen iLOQ Manager en Synguard",
            "Technische Architectuur Component": "Cloud Gateway API, Data Synchronisatie",
            "QA / Test Scenario (Acceptatiecriterium)": "Test bidirectionele gegevensoverdracht tussen iLOQ Manager en Synguard"
        },
        {
            "FR/NFR ID": "FE-002",
            "Traces To CN": "CN-002",
            "Description": "Realtime logging van gebeurtenissen",
            "Technische Architectuur Component": "Logging en Monitoring",
            "QA / Test Scenario (Acceptatiecriterium)": "Verifieer realtime logging van toegangspogingen en systeemwijzigingen"
        },
        {
            "FR/NFR ID": "FE-003",
            "Traces To CN": "CN-003",
            "Description": "Weergave van batterijstatus in SynApp",
            "Technische Architectuur Component": "Batterijstatus Monitoring",
            "QA / Test Scenario (Acceptatiecriterium)": "Controleer de zichtbaarheid en nauwkeurigheid van de batterijstatus in SynApp"
        },
        {
            "FR/NFR ID": "NFE-001",
            "Traces To CN": "CN-001, CN-002, CN-003",
            "Description": "Voldoen aan beveiligingsstandaarden",
            "Technische Architectuur Component": "Beveiliging",
            "QA / Test Scenario (Acceptatiecriterium)": "Voer penetratietests uit om de beveiliging van de integratie te evalueren"
        },
        {
            "FR/NFR ID": "NFE-002",
            "Traces To CN": "CN-002",
            "Description": "Minimale vertraging in synchronisatie en logging",
            "Technische Architectuur Component": "Prestaties",
            "QA / Test Scenario (Acceptatiecriterium)": "Meet de vertragingstijd van synchronisatie en logging"
        },
        {
            "FR/NFR ID": "NFE-003",
            "Traces To CN": "CN-003",
            "Description": "Intu\u00eftieve en gebruiksvriendelijke UI",
            "Technische Architectuur Component": "UI/UX",
            "QA / Test Scenario (Acceptatiecriterium)": "Beoordeel de gebruiksvriendelijkheid van de SynApp interface"
        },
        {
            "FR/NFR ID": "NFE-004",
            "Traces To CN": "CN-001, CN-002, CN-003",
            "Description": "Schaalbaarheid voor toekomstige uitbreidingen",
            "Technische Architectuur Component": "Schaalbaarheid",
            "QA / Test Scenario (Acceptatiecriterium)": "Test de prestaties van het systeem onder verhoogde belasting"
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