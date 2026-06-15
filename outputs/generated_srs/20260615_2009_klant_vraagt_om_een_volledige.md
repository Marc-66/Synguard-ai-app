"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten..."
[---SPLIT-DOSSIER---]
**Customer Requirements Rapport**

**Probleemstelling:**
Klanten ervaren inefficiëntie en ongemak doordat zij momenteel moeten werken met twee aparte systemen: iLOQ Manager en Synguard. Deze situatie leidt tot dubbel werk en verhoogde kans op fouten, aangezien gegevens niet automatisch tussen de systemen worden gesynchroniseerd.

**Huidige Situatie:**
- Klanten gebruiken iLOQ Manager voor het beheer van RF draadloze sloten.
- Synguard wordt gebruikt voor toegangscontrole en beveiligingsbeheer.
- Er is geen directe communicatie of integratie tussen iLOQ Manager en Synguard, wat leidt tot een gefragmenteerde workflow.

**Gewenste Functionaliteit:**
1. **Bidirectionele Synchronisatie:**
   - Er moet een naadloze integratie komen tussen iLOQ Manager en Synguard, waarbij gegevens automatisch en in beide richtingen worden gesynchroniseerd. Dit betekent dat wijzigingen in het ene systeem direct zichtbaar en toepasbaar zijn in het andere systeem.

2. **Realtime Logging:**
   - Het systeem moet in staat zijn om gebeurtenissen en wijzigingen in realtime te loggen. Dit omvat het bijhouden van toegangspogingen, wijzigingen in slotconfiguraties, en andere relevante activiteiten. Deze logs moeten toegankelijk zijn voor gebruikers binnen Synguard.

3. **Batterijstatus in SynApp:**
   - Gebruikers moeten de batterijstatus van iLOQ RF draadloze sloten kunnen monitoren via de SynApp. Dit biedt inzicht in de operationele status van de sloten en helpt bij het plannen van onderhoud en het voorkomen van onverwachte uitval.

**Conclusie:**
De klant vraagt om een volledige integratie van iLOQ RF draadloze sloten met Synguard, waarbij de focus ligt op het verbeteren van efficiëntie en gebruiksgemak door middel van bidirectionele synchronisatie, realtime logging, en het monitoren van batterijstatussen. Deze integratie zal de workflow stroomlijnen en de operationele effectiviteit van klanten aanzienlijk verbeteren.
[---SPLIT-DOSSIER---]
# Technische Specificaties voor iLOQ Integratie met Synguard

## Overzicht
Deze documentatie beschrijft de technische specificaties voor de integratie van iLOQ S5/S50 met Synguard via de Cloud Gateway API. Het doel is om een naadloze en efficiënte workflow te creëren door bidirectionele synchronisatie, realtime logging, en monitoring van batterijstatussen.

## Integratie Details
- **Systeem:** iLOQ S5/S50
- **API:** Cloud Gateway API
- **Website:** [iloq.com](https://www.iloq.com)
- **UI/UX Verwachtingen:** Gebruik van iLOQ iconen in de SynApp boomstructuur.
- **Constraints:** Cloud-to-cloud integratie via iLOQ Gateway. Geen lokale server-installatie toegestaan.

## Functionele Specificaties

### 1. Bidirectionele Synchronisatie
- **Beschrijving:** Zorgt voor automatische gegevenssynchronisatie tussen iLOQ Manager en Synguard.
- **Functionaliteit:**
  - Wijzigingen in iLOQ Manager worden direct doorgevoerd in Synguard.
  - Wijzigingen in Synguard worden direct doorgevoerd in iLOQ Manager.

### 2. Realtime Logging
- **Beschrijving:** Logt gebeurtenissen en wijzigingen in realtime.
- **Functionaliteit:**
  - Toegangspogingen en slotconfiguratiewijzigingen worden bijgehouden.
  - Logs zijn toegankelijk binnen Synguard voor gebruikers.

### 3. Batterijstatus Monitoring
- **Beschrijving:** Monitoren van de batterijstatus van iLOQ RF draadloze sloten via SynApp.
- **Functionaliteit:**
  - Gebruikers kunnen de batterijstatus inzien.
  - Ondersteunt onderhoudsplanning en voorkomt onverwachte uitval.

## Traceability Matrix

| CRD Vereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |
|-----------------|--------------|----------------------------|-----------------------|
| CRD-01          | Bidirectionele Synchronisatie | TS-01 | Implementatie van API-koppeling voor gegevenssynchronisatie. |
| CRD-02          | Realtime Logging | TS-02 | Gebruik van Cloud Gateway API voor het loggen van gebeurtenissen. |
| CRD-03          | Batterijstatus Monitoring | TS-03 | Integratie van batterijstatusweergave in SynApp UI. |

## Technische Implementatie Details

### API Integratie
- **API Endpoint:** Gebruik de Cloud Gateway API voor gegevensuitwisseling.
- **Authenticatie:** OAuth 2.0 voor veilige communicatie tussen systemen.
- **Data Formaat:** JSON voor het verzenden en ontvangen van gegevens.

### UI/UX Implementatie
- **Iconen:** Gebruik van iLOQ iconen in de boomstructuur van SynApp.
- **Gebruikersinterface:** Intuïtieve weergave van batterijstatus en loggegevens.

### Systeemvereisten
- **Netwerk:** Stabiele internetverbinding voor cloud-to-cloud communicatie.
- **Compatibiliteit:** Ondersteuning voor de nieuwste versies van iLOQ S5/S50 en Synguard.

## Conclusie
Deze integratie zal de workflow van klanten verbeteren door een naadloze synchronisatie tussen iLOQ en Synguard te bieden, realtime logging te ondersteunen, en inzicht te geven in de batterijstatus van sloten. Dit verhoogt de operationele effectiviteit en vermindert de kans op fouten.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant vraagt om een volledige integratie van iLOQ RF draadloze sloten...\"",
    "cust_req": "**Customer Requirements Rapport**\n\n**Probleemstelling:**\nKlanten ervaren ineffici\u00ebntie en ongemak doordat zij momenteel moeten werken met twee aparte systemen: iLOQ Manager en Synguard. Deze situatie leidt tot dubbel werk en verhoogde kans op fouten, aangezien gegevens niet automatisch tussen de systemen worden gesynchroniseerd.\n\n**Huidige Situatie:**\n- Klanten gebruiken iLOQ Manager voor het beheer van RF draadloze sloten.\n- Synguard wordt gebruikt voor toegangscontrole en beveiligingsbeheer.\n- Er is geen directe communicatie of integratie tussen iLOQ Manager en Synguard, wat leidt tot een gefragmenteerde workflow.\n\n**Gewenste Functionaliteit:**\n1. **Bidirectionele Synchronisatie:**\n   - Er moet een naadloze integratie komen tussen iLOQ Manager en Synguard, waarbij gegevens automatisch en in beide richtingen worden gesynchroniseerd. Dit betekent dat wijzigingen in het ene systeem direct zichtbaar en toepasbaar zijn in het andere systeem.\n\n2. **Realtime Logging:**\n   - Het systeem moet in staat zijn om gebeurtenissen en wijzigingen in realtime te loggen. Dit omvat het bijhouden van toegangspogingen, wijzigingen in slotconfiguraties, en andere relevante activiteiten. Deze logs moeten toegankelijk zijn voor gebruikers binnen Synguard.\n\n3. **Batterijstatus in SynApp:**\n   - Gebruikers moeten de batterijstatus van iLOQ RF draadloze sloten kunnen monitoren via de SynApp. Dit biedt inzicht in de operationele status van de sloten en helpt bij het plannen van onderhoud en het voorkomen van onverwachte uitval.\n\n**Conclusie:**\nDe klant vraagt om een volledige integratie van iLOQ RF draadloze sloten met Synguard, waarbij de focus ligt op het verbeteren van effici\u00ebntie en gebruiksgemak door middel van bidirectionele synchronisatie, realtime logging, en het monitoren van batterijstatussen. Deze integratie zal de workflow stroomlijnen en de operationele effectiviteit van klanten aanzienlijk verbeteren.",
    "tech_req": "# Technische Specificaties voor iLOQ Integratie met Synguard\n\n## Overzicht\nDeze documentatie beschrijft de technische specificaties voor de integratie van iLOQ S5/S50 met Synguard via de Cloud Gateway API. Het doel is om een naadloze en effici\u00ebnte workflow te cre\u00ebren door bidirectionele synchronisatie, realtime logging, en monitoring van batterijstatussen.\n\n## Integratie Details\n- **Systeem:** iLOQ S5/S50\n- **API:** Cloud Gateway API\n- **Website:** [iloq.com](https://www.iloq.com)\n- **UI/UX Verwachtingen:** Gebruik van iLOQ iconen in de SynApp boomstructuur.\n- **Constraints:** Cloud-to-cloud integratie via iLOQ Gateway. Geen lokale server-installatie toegestaan.\n\n## Functionele Specificaties\n\n### 1. Bidirectionele Synchronisatie\n- **Beschrijving:** Zorgt voor automatische gegevenssynchronisatie tussen iLOQ Manager en Synguard.\n- **Functionaliteit:**\n  - Wijzigingen in iLOQ Manager worden direct doorgevoerd in Synguard.\n  - Wijzigingen in Synguard worden direct doorgevoerd in iLOQ Manager.\n\n### 2. Realtime Logging\n- **Beschrijving:** Logt gebeurtenissen en wijzigingen in realtime.\n- **Functionaliteit:**\n  - Toegangspogingen en slotconfiguratiewijzigingen worden bijgehouden.\n  - Logs zijn toegankelijk binnen Synguard voor gebruikers.\n\n### 3. Batterijstatus Monitoring\n- **Beschrijving:** Monitoren van de batterijstatus van iLOQ RF draadloze sloten via SynApp.\n- **Functionaliteit:**\n  - Gebruikers kunnen de batterijstatus inzien.\n  - Ondersteunt onderhoudsplanning en voorkomt onverwachte uitval.\n\n## Traceability Matrix\n\n| CRD Vereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |\n|-----------------|--------------|----------------------------|-----------------------|\n| CRD-01          | Bidirectionele Synchronisatie | TS-01 | Implementatie van API-koppeling voor gegevenssynchronisatie. |\n| CRD-02          | Realtime Logging | TS-02 | Gebruik van Cloud Gateway API voor het loggen van gebeurtenissen. |\n| CRD-03          | Batterijstatus Monitoring | TS-03 | Integratie van batterijstatusweergave in SynApp UI. |\n\n## Technische Implementatie Details\n\n### API Integratie\n- **API Endpoint:** Gebruik de Cloud Gateway API voor gegevensuitwisseling.\n- **Authenticatie:** OAuth 2.0 voor veilige communicatie tussen systemen.\n- **Data Formaat:** JSON voor het verzenden en ontvangen van gegevens.\n\n### UI/UX Implementatie\n- **Iconen:** Gebruik van iLOQ iconen in de boomstructuur van SynApp.\n- **Gebruikersinterface:** Intu\u00eftieve weergave van batterijstatus en loggegevens.\n\n### Systeemvereisten\n- **Netwerk:** Stabiele internetverbinding voor cloud-to-cloud communicatie.\n- **Compatibiliteit:** Ondersteuning voor de nieuwste versies van iLOQ S5/S50 en Synguard.\n\n## Conclusie\nDeze integratie zal de workflow van klanten verbeteren door een naadloze synchronisatie tussen iLOQ en Synguard te bieden, realtime logging te ondersteunen, en inzicht te geven in de batterijstatus van sloten. Dit verhoogt de operationele effectiviteit en vermindert de kans op fouten.",
    "sow_body": "# Statement of Work (SoW) Document\n\n## 1. Executive Summary & Project Purpose\n\nDit Statement of Work (SoW) document beschrijft de integratie van iLOQ S5/S50 met Synguard via de Cloud Gateway API. Het doel van dit project is om een effici\u00ebnte en naadloze workflow te cre\u00ebren voor onze partners en klanten door middel van bidirectionele synchronisatie, realtime logging, en monitoring van batterijstatussen. Deze integratie zal de operationele effectiviteit verhogen en de kans op fouten verminderen.\n\n## 2. Detailed Scope of Work\n\n### Functionele Requirements\n\n#### FR-001: Bidirectionele Synchronisatie\n- **Beschrijving:** Implementatie van automatische gegevenssynchronisatie tussen iLOQ Manager en Synguard.\n- **Technische Specificatie:** TS-01\n- **Details:** Wijzigingen in iLOQ Manager en Synguard worden direct gesynchroniseerd.\n\n#### FR-002: Realtime Logging\n- **Beschrijving:** Implementatie van realtime logging van gebeurtenissen en wijzigingen.\n- **Technische Specificatie:** TS-02\n- **Details:** Toegangspogingen en slotconfiguratiewijzigingen worden bijgehouden en zijn toegankelijk binnen Synguard.\n\n#### FR-003: Batterijstatus Monitoring\n- **Beschrijving:** Implementatie van monitoring van de batterijstatus van iLOQ RF draadloze sloten.\n- **Technische Specificatie:** TS-03\n- **Details:** Gebruikers kunnen de batterijstatus inzien via SynApp, wat onderhoudsplanning ondersteunt.\n\n## 3. Out of Scope\n\nSynguard levert expliciet geen lokale IT-infrastructuur, bekabeling, of server-installaties. Alle integraties worden uitgevoerd via cloud-to-cloud communicatie, en lokale server-installaties zijn niet toegestaan.\n\n## 4. Deliverables & Jira Component Mapping\n\n### Deliverables\n- Volledige integratie van iLOQ S5/S50 met Synguard.\n- Ge\u00efmplementeerde bidirectionele synchronisatie.\n- Realtime logging functionaliteit.\n- Batterijstatus monitoring in SynApp UI.\n\n### Jira Component Mapping\n- **Component:** iLOQ Integration\n  - **Issue Type:** Task\n  - **Epic:** iLOQ-Synguard Integration\n  - **Sub-tasks:** API Integration, UI/UX Design, Testing & Validation\n\n## 5. High-Level Timeline & Milestones\n\n### Timeline\n- **Week 1-2:** API Integratie en Authenticatie Setup\n- **Week 3-4:** UI/UX Implementatie en Iconen Integratie\n- **Week 5:** Testing & Validation\n- **Week 6:** Go-Live en Monitoring\n\n### Milestones\n- **Milestone 1:** Voltooiing van API Integratie\n- **Milestone 2:** UI/UX Implementatie voltooid\n- **Milestone 3:** Succesvolle Testing & Validation\n- **Milestone 4:** Project Go-Live\n\n## 6. Acceptance Criteria & Sign-off Procedure\n\n### Acceptance Criteria\n- Volledige functionele integratie van iLOQ S5/S50 met Synguard.\n- Geen kritieke bugs of issues bij Go-Live.\n- Voldoen aan alle functionele requirements zoals beschreven.\n\n### Sign-off Procedure\n- **Review:** Project wordt beoordeeld door de klant en Synguard projectteam.\n- **Approval:** Schriftelijke goedkeuring door de klant.\n- **Closure:** Offici\u00eble afsluiting van het project na goedkeuring.\n\nDit document dient als leidraad voor de succesvolle uitvoering van het integratieproject en verzekert dat alle betrokken partijen duidelijkheid hebben over de verwachtingen en verantwoordelijkheden.",
    "current_filepath": "outputs/generated_srs\\20260615_2009_klant_vraagt_om_een_volledige.md",
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
            "FR/NFR ID": "CRD-01",
            "Traces To CN": "TS-01",
            "Description": "Bidirectionele Synchronisatie",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Implementatie van API-koppeling voor gegevenssynchronisatie."
        },
        {
            "FR/NFR ID": "CRD-02",
            "Traces To CN": "TS-02",
            "Description": "Realtime Logging",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Gebruik van Cloud Gateway API voor het loggen van gebeurtenissen."
        },
        {
            "FR/NFR ID": "CRD-03",
            "Traces To CN": "TS-03",
            "Description": "Batterijstatus Monitoring",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Integratie van batterijstatusweergave in SynApp UI."
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