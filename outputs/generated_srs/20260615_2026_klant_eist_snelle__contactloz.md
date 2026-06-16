"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller."
[---SPLIT-DOSSIER---]
**Customer Requirements Rapport**

**Probleem:**
De klant heeft behoefte aan een efficiënte en snelle toegangscontrole bij de hoofdingang van hun faciliteit. De huidige toegangscontrolemethoden zijn niet voldoende snel en vereisen fysieke interactie, wat de doorstroom vertraagt en mogelijk veiligheidsrisico's met zich meebrengt.

**Huidige situatie:**
Momenteel maakt de klant gebruik van traditionele toegangscontrolemethoden die niet voldoen aan de eisen van snelheid en contactloos gebruik. Er is behoefte aan een geavanceerde oplossing die biometrische gezichtsherkenning kan bieden zonder vertraging.

**Gewenste functionaliteit:**

1. **Template opslag op SynCon Evo:**
   - De klant wenst dat gezichtsherkenningsgegevens en templates worden opgeslagen op het SynCon Evo platform. Dit zorgt voor een gecentraliseerde en efficiënte opslag van biometrische data, wat essentieel is voor snelle verwerking en herkenning.

2. **Realtime gezichtsherkenning (<1s):**
   - De gezichtsherkenning moet binnen minder dan één seconde plaatsvinden. Dit vereist een geavanceerd systeem dat snelle en nauwkeurige identificatie kan bieden, zodat de doorstroom bij de ingang niet wordt gehinderd.

3. **Wiegand/OSDP koppeling:**
   - Er is behoefte aan integratie met bestaande toegangscontrole systemen via Wiegand of OSDP protocollen. Dit zorgt voor een naadloze communicatie tussen de gezichtsherkenningsscanners en de centrale controller, waardoor de toegang efficiënt kan worden beheerd.

**Specifieke eisen:**
- De klant eist dat de biometrische gezichtsherkenning contactloos is en plaatsvindt via Suprema scanners die direct gekoppeld zijn aan de controller. Dit benadrukt de noodzaak van een snelle en betrouwbare verbinding tussen de hardwarecomponenten om de gewenste functionaliteit te realiseren.

Dit rapport biedt een overzicht van de klantvereisten en de functionele beschrijving van de gewenste oplossing voor toegangscontrole via biometrische gezichtsherkenning. Het is essentieel dat de implementatie van deze technologie voldoet aan de gestelde eisen om de efficiëntie en veiligheid bij de hoofdingang te verbeteren.
[---SPLIT-DOSSIER---]
Hier zijn de harde technische specificaties en de traceability matrix voor de integratie van Suprema BioStation 3 met SynApp, gebaseerd op de gegeven klantvereisten en randvoorwaarden.

## Technische Specificaties

### Integratie Details
- **Systeem:** Suprema BioStation 3
- **API:** Suprema BioStar 2 API
- **Platform:** SynCon Evo
- **Protocollen:** Wiegand, OSDP

### Functionele Specificaties
1. **Biometrische Template Opslag**
   - **Opslaglocatie:** SynCon Evo
   - **Versleuteling:** AVG/GDPR compliant hashing
   - **Dataformaat:** Gehashte biometrische templates

2. **Realtime Gezichtsherkenning**
   - **Snelheid:** <1 seconde
   - **Nauwkeurigheid:** Hoog (99%+)
   - **Contactloos:** Ja

3. **Integratie met Toegangscontrolesystemen**
   - **Protocollen:** Wiegand, OSDP
   - **Communicatie:** Naadloos tussen Suprema scanners en centrale controller

### UI/UX Verwachtingen
- **Beheer:** Suprema apparaten beheren vanuit het hardware-overzicht in SynApp
- **Gebruikersinterface:** Intuïtief en vertrouwd voor bestaande gebruikers van SynApp

### Veiligheid en Compliance
- **AVG/GDPR Compliance:** Biometrische data moet versleuteld zijn en geen echte foto's opslaan
- **Data Privacy:** Alleen gehashte templates worden opgeslagen

## Traceability Matrix

| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |
|------------------|--------------|---------------------------|-----------------------|
| CR-01            | Template opslag op SynCon Evo | TS-01 | Opslag van gehashte biometrische templates op SynCon Evo |
| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Implementatie van snelle gezichtsherkenning via Suprema BioStation 3 |
| CR-03            | Wiegand/OSDP koppeling | TS-03 | Integratie met bestaande systemen via Wiegand/OSDP protocollen |
| CR-04            | Contactloze biometrische herkenning | TS-04 | Gebruik van contactloze Suprema scanners direct gekoppeld aan de controller |
| CR-05            | AVG/GDPR compliance | TS-05 | Versleuteling van biometrische data met hashing, geen opslag van echte foto's |

Deze matrix en specificaties zorgen ervoor dat alle klantvereisten worden getraceerd naar specifieke technische implementaties, wat helpt bij het waarborgen van een succesvolle en conforme oplossing voor de klant.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller.\"",
    "cust_req": "**Customer Requirements Rapport**\n\n**Probleem:**\nDe klant heeft behoefte aan een effici\u00ebnte en snelle toegangscontrole bij de hoofdingang van hun faciliteit. De huidige toegangscontrolemethoden zijn niet voldoende snel en vereisen fysieke interactie, wat de doorstroom vertraagt en mogelijk veiligheidsrisico's met zich meebrengt.\n\n**Huidige situatie:**\nMomenteel maakt de klant gebruik van traditionele toegangscontrolemethoden die niet voldoen aan de eisen van snelheid en contactloos gebruik. Er is behoefte aan een geavanceerde oplossing die biometrische gezichtsherkenning kan bieden zonder vertraging.\n\n**Gewenste functionaliteit:**\n\n1. **Template opslag op SynCon Evo:**\n   - De klant wenst dat gezichtsherkenningsgegevens en templates worden opgeslagen op het SynCon Evo platform. Dit zorgt voor een gecentraliseerde en effici\u00ebnte opslag van biometrische data, wat essentieel is voor snelle verwerking en herkenning.\n\n2. **Realtime gezichtsherkenning (<1s):**\n   - De gezichtsherkenning moet binnen minder dan \u00e9\u00e9n seconde plaatsvinden. Dit vereist een geavanceerd systeem dat snelle en nauwkeurige identificatie kan bieden, zodat de doorstroom bij de ingang niet wordt gehinderd.\n\n3. **Wiegand/OSDP koppeling:**\n   - Er is behoefte aan integratie met bestaande toegangscontrole systemen via Wiegand of OSDP protocollen. Dit zorgt voor een naadloze communicatie tussen de gezichtsherkenningsscanners en de centrale controller, waardoor de toegang effici\u00ebnt kan worden beheerd.\n\n**Specifieke eisen:**\n- De klant eist dat de biometrische gezichtsherkenning contactloos is en plaatsvindt via Suprema scanners die direct gekoppeld zijn aan de controller. Dit benadrukt de noodzaak van een snelle en betrouwbare verbinding tussen de hardwarecomponenten om de gewenste functionaliteit te realiseren.\n\nDit rapport biedt een overzicht van de klantvereisten en de functionele beschrijving van de gewenste oplossing voor toegangscontrole via biometrische gezichtsherkenning. Het is essentieel dat de implementatie van deze technologie voldoet aan de gestelde eisen om de effici\u00ebntie en veiligheid bij de hoofdingang te verbeteren.",
    "tech_req": "Hier zijn de harde technische specificaties en de traceability matrix voor de integratie van Suprema BioStation 3 met SynApp, gebaseerd op de gegeven klantvereisten en randvoorwaarden.\n\n## Technische Specificaties\n\n### Integratie Details\n- **Systeem:** Suprema BioStation 3\n- **API:** Suprema BioStar 2 API\n- **Platform:** SynCon Evo\n- **Protocollen:** Wiegand, OSDP\n\n### Functionele Specificaties\n1. **Biometrische Template Opslag**\n   - **Opslaglocatie:** SynCon Evo\n   - **Versleuteling:** AVG/GDPR compliant hashing\n   - **Dataformaat:** Gehashte biometrische templates\n\n2. **Realtime Gezichtsherkenning**\n   - **Snelheid:** <1 seconde\n   - **Nauwkeurigheid:** Hoog (99%+)\n   - **Contactloos:** Ja\n\n3. **Integratie met Toegangscontrolesystemen**\n   - **Protocollen:** Wiegand, OSDP\n   - **Communicatie:** Naadloos tussen Suprema scanners en centrale controller\n\n### UI/UX Verwachtingen\n- **Beheer:** Suprema apparaten beheren vanuit het hardware-overzicht in SynApp\n- **Gebruikersinterface:** Intu\u00eftief en vertrouwd voor bestaande gebruikers van SynApp\n\n### Veiligheid en Compliance\n- **AVG/GDPR Compliance:** Biometrische data moet versleuteld zijn en geen echte foto's opslaan\n- **Data Privacy:** Alleen gehashte templates worden opgeslagen\n\n## Traceability Matrix\n\n| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |\n|------------------|--------------|---------------------------|-----------------------|\n| CR-01            | Template opslag op SynCon Evo | TS-01 | Opslag van gehashte biometrische templates op SynCon Evo |\n| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Implementatie van snelle gezichtsherkenning via Suprema BioStation 3 |\n| CR-03            | Wiegand/OSDP koppeling | TS-03 | Integratie met bestaande systemen via Wiegand/OSDP protocollen |\n| CR-04            | Contactloze biometrische herkenning | TS-04 | Gebruik van contactloze Suprema scanners direct gekoppeld aan de controller |\n| CR-05            | AVG/GDPR compliance | TS-05 | Versleuteling van biometrische data met hashing, geen opslag van echte foto's |\n\nDeze matrix en specificaties zorgen ervoor dat alle klantvereisten worden getraceerd naar specifieke technische implementaties, wat helpt bij het waarborgen van een succesvolle en conforme oplossing voor de klant.",
    "sow_body": "# Statement of Work (SoW)\n\n## 1. Executive Summary & Project Purpose\n\nDit Statement of Work (SoW) document is opgesteld om de integratie van Suprema BioStation 3 met SynApp te beschrijven, zoals vereist door onze gewaardeerde partner/klant. Het doel van dit project is om een naadloze en veilige biometrische toegangscontroleoplossing te bieden die voldoet aan de hoogste standaarden van snelheid, nauwkeurigheid en compliance. Door gebruik te maken van de Suprema BioStar 2 API en SynCon Evo platform, streven we naar een oplossing die zowel intu\u00eftief als betrouwbaar is, en die de gebruikerservaring van SynApp verder versterkt.\n\n## 2. Detailed Scope of Work\n\n### Functionele Requirements\n\n- **FR-001: Biometrische Template Opslag**\n  - **Specificatie:** Opslag van gehashte biometrische templates op SynCon Evo.\n  - **Details:** De biometrische data wordt AVG/GDPR-compliant versleuteld opgeslagen, zonder echte foto's.\n\n- **FR-002: Realtime Gezichtsherkenning**\n  - **Specificatie:** Implementatie van snelle gezichtsherkenning via Suprema BioStation 3.\n  - **Details:** De herkenning moet plaatsvinden binnen <1 seconde met een nauwkeurigheid van 99%+.\n\n- **FR-003: Integratie met Toegangscontrolesystemen**\n  - **Specificatie:** Integratie met bestaande systemen via Wiegand/OSDP protocollen.\n  - **Details:** Zorgt voor naadloze communicatie tussen Suprema scanners en de centrale controller.\n\n- **FR-004: Contactloze Biometrische Herkenning**\n  - **Specificatie:** Gebruik van contactloze Suprema scanners direct gekoppeld aan de controller.\n  - **Details:** Verhoogt de gebruiksvriendelijkheid en hygi\u00ebne van het systeem.\n\n- **FR-005: AVG/GDPR Compliance**\n  - **Specificatie:** Versleuteling van biometrische data met hashing, geen opslag van echte foto's.\n  - **Details:** Waarborgt de privacy en veiligheid van gebruikersdata.\n\n## 3. Out of Scope\n\nSynguard levert expliciet niet de volgende zaken binnen dit project:\n- Lokale IT-infrastructuur en netwerkconfiguratie.\n- Fysieke bekabeling en installatie van hardware.\n- Onderhoud en ondersteuning van niet-gerelateerde software of systemen.\n\n## 4. Deliverables & Jira Component Mapping\n\n### Deliverables\n- Volledig ge\u00efntegreerd biometrisch toegangscontrolesysteem.\n- Documentatie van de integratieprocessen en gebruikershandleidingen.\n- Training voor beheerders van het systeem.\n\n### Jira Component Mapping\n- **Component 1:** Biometrische Template Opslag - Jira ID: BIOTEMP-001\n- **Component 2:** Realtime Gezichtsherkenning - Jira ID: FACE-REC-002\n- **Component 3:** Systeemintegratie - Jira ID: SYSINT-003\n\n## 5. High-Level Timeline & Milestones\n\n- **Week 1-2:** Initi\u00eble setup en configuratie van de Suprema BioStation 3.\n- **Week 3-4:** Implementatie van de biometrische template opslag en gezichtsherkenning.\n- **Week 5:** Integratie met toegangscontrolesystemen en testen.\n- **Week 6:** Voltooiing van de AVG/GDPR compliance checks en eindvalidatie.\n- **Week 7:** Oplevering en training van systeembeheerders.\n\n## 6. Acceptance Criteria & Sign-off Procedure\n\n### Acceptance Criteria\n- Het systeem moet biometrische templates veilig en AVG/GDPR-compliant opslaan.\n- Realtime gezichtsherkenning moet binnen <1 seconde plaatsvinden met een nauwkeurigheid van 99%+.\n- Naadloze integratie met bestaande toegangscontrolesystemen via Wiegand/OSDP protocollen.\n- Het systeem moet contactloos functioneren en intu\u00eftief beheer bieden via SynApp.\n\n### Sign-off Procedure\n- Na voltooiing van de implementatie zal een formele acceptatietest worden uitgevoerd.\n- De klant dient schriftelijk akkoord te geven op de oplevering van het systeem.\n- Eventuele afwijkingen of problemen worden gedocumenteerd en opgelost voordat de definitieve sign-off plaatsvindt.\n\nWij kijken uit naar een succesvolle samenwerking en implementatie van deze oplossing. Mocht u vragen of opmerkingen hebben, aarzel dan niet om contact met ons op te nemen.\n\nMet vriendelijke groet,\n\n[Naam]\nSynguard Commercial & Delivery Agent",
    "current_filepath": "outputs/generated_srs\\20260615_2026_klant_eist_snelle__contactloz.md",
    "development_type": "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
    "business_driver": "Partner Request",
    "is_customer_specific": "Customer Specific (Unique)",
    "verticals": [
        "Government",
        "Corporate"
    ],
    "benchmark_competitor": "",
    "link_project": "",
    "link_product": "",
    "total_project_value": 85,
    "chargeable_value": 12,
    "potential_yearly_revenue": 10,
    "resolved_problem": "",
    "value_end_customer": "High-security, extreem snelle doorstroom, geen gedoe met fysieke badges verliezen.",
    "value_partner": "Kan meedingen in het absolute high-security segment (datacenters/banken).",
    "value_synguard": "Positioneert Synguard als enterprise-ready platform voor biometrische authenticatie.",
    "current_situation": "",
    "overall_workflow": "\"As a user, I present my face to the Suprema reader. SynCon Evo verifies the biometric template realtime.\"",
    "desired_functionality": "1. Template opslag op SynCon Evo\n2. Realtime gezichtsherkenning (<1s)\n3. Wiegand/OSDP koppeling\n",
    "integration_details": "Systeem: Suprema BioStation 3.\nAPI: Suprema BioStar 2 API.\n",
    "ui_ux_expectations": "Suprema apparaten beheren vanuit het vertrouwde hardware-overzicht in SynApp.",
    "acceptance_criteria": "Authenticatie en deuropening binnen 0.8 seconden na gezichtsscan.",
    "constraints_conditions": "Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).",
    "tender_text": "\"Zie paragraaf 4.2 in bestek 'Datacenter Brussell': Biometrische toegang is een harde uitsluitingsgrond.\"",
    "matrix_data": [
        {
            "FR/NFR ID": "CR-01",
            "Traces To CN": "TS-01",
            "Description": "Template opslag op SynCon Evo",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Opslag van gehashte biometrische templates op SynCon Evo"
        },
        {
            "FR/NFR ID": "CR-02",
            "Traces To CN": "TS-02",
            "Description": "Realtime gezichtsherkenning (<1s)",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Implementatie van snelle gezichtsherkenning via Suprema BioStation 3"
        },
        {
            "FR/NFR ID": "CR-03",
            "Traces To CN": "TS-03",
            "Description": "Wiegand/OSDP koppeling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Integratie met bestaande systemen via Wiegand/OSDP protocollen"
        },
        {
            "FR/NFR ID": "CR-04",
            "Traces To CN": "TS-04",
            "Description": "Contactloze biometrische herkenning",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Gebruik van contactloze Suprema scanners direct gekoppeld aan de controller"
        },
        {
            "FR/NFR ID": "CR-05",
            "Traces To CN": "TS-05",
            "Description": "AVG/GDPR compliance",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Versleuteling van biometrische data met hashing, geen opslag van echte foto's"
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