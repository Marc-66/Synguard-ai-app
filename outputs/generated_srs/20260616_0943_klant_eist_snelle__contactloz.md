"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller."
[---SPLIT-DOSSIER---]
**Customer Requirements Rapport**

**Probleem:**
De klant heeft behoefte aan een efficiënte en snelle toegangsmethode bij de hoofdingang van hun faciliteit. De huidige toegangsmethoden zijn mogelijk traag en vereisen fysiek contact, wat niet ideaal is voor de gewenste gebruikservaring en veiligheid.

**Huidige situatie:**
Momenteel maakt de klant gebruik van traditionele toegangssystemen die mogelijk niet voldoen aan de eisen voor snelheid en contactloos gebruik. Er is behoefte aan een geavanceerde oplossing die biometrische gezichtsherkenning kan bieden zonder vertraging.

**Gewenste functionaliteit:**

1. **Template opslag op SynCon Evo:**
   - De klant wenst dat gezichtsherkenning templates worden opgeslagen op het SynCon Evo platform. Dit vereist een betrouwbare en veilige opslag van biometrische gegevens die gemakkelijk toegankelijk zijn voor het gezichtsherkenningssysteem.

2. **Realtime gezichtsherkenning (<1s):**
   - De klant eist dat het gezichtsherkenningssysteem in staat is om binnen minder dan één seconde een gezicht te herkennen en toegang te verlenen. Dit benadrukt de noodzaak voor een snelle en efficiënte verwerking van biometrische gegevens.

3. **Wiegand/OSDP koppeling:**
   - Er is behoefte aan integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen. Dit zorgt voor compatibiliteit en naadloze communicatie tussen de gezichtsherkenningsscanners en de controller.

**Aanvullende specificaties:**
- De gezichtsherkenning moet contactloos zijn en uitgevoerd worden via Suprema scanners, die direct gekoppeld zijn aan de controller. Dit vereist een robuuste en betrouwbare hardware-oplossing die compatibel is met de bestaande infrastructuur van de klant.

Dit rapport biedt een overzicht van de klantvereisten voor een verbeterd toegangssysteem dat gebruikmaakt van geavanceerde biometrische technologieën. Het doel is om een snelle, veilige en contactloze toegang te realiseren die voldoet aan de moderne eisen van de klant.
[---SPLIT-DOSSIER---]
# Synguard AI Technical Specifications

## Integratie Details
- **Systeem:** Suprema BioStation 3
- **API:** Suprema BioStar 2 API

## UI/UX Verwachtingen
- Beheer van Suprema apparaten vanuit het vertrouwde hardware-overzicht in SynApp.

## Constraints
- Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).

## Technische Specificaties

### Hardware
- **Suprema BioStation 3:** Ondersteuning voor gezichtsherkenning en integratie met bestaande toegangssystemen.
- **SynCon Evo Platform:** Opslag en verwerking van biometrische templates.

### Software
- **Suprema BioStar 2 API:** Voor communicatie en integratie met Suprema apparaten.
- **SynApp:** UI/UX interface voor beheer van apparaten.

### Functionaliteit
1. **Template Opslag op SynCon Evo:**
   - AVG/GDPR compliant versleuteling van biometrische templates.
   - Betrouwbare en veilige opslag van gegevens.

2. **Realtime Gezichtsherkenning (<1s):**
   - Snelle verwerking en herkenning van gezichten binnen minder dan één seconde.
   - Contactloze toegang via Suprema scanners.

3. **Wiegand/OSDP Koppeling:**
   - Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen.
   - Naadloze communicatie tussen gezichtsherkenningsscanners en de controller.

## Traceability Matrix

| Customer Requirement ID | Description | Technical Specification ID | Description |
|-------------------------|-------------|----------------------------|-------------|
| CR-1                    | Template opslag op SynCon Evo | TS-1                       | AVG/GDPR compliant versleuteling en opslag van biometrische templates |
| CR-2                    | Realtime gezichtsherkenning (<1s) | TS-2                       | Snelle verwerking en herkenning van gezichten binnen minder dan één seconde |
| CR-3                    | Wiegand/OSDP koppeling | TS-3                       | Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen |

## Aanvullende Specificaties
- **Contactloze Gezichtsherkenning:** Uitgevoerd via Suprema scanners, direct gekoppeld aan de controller.
- **Robuuste Hardware-Oplossing:** Compatibel met de bestaande infrastructuur van de klant.

Dit document biedt een gedetailleerd overzicht van de technische specificaties en traceability matrix voor de implementatie van een geavanceerd biometrisch toegangssysteem dat voldoet aan de moderne eisen van de klant.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller.\"",
    "cust_req": "**Customer Requirements Rapport**\n\n**Probleem:**\nDe klant heeft behoefte aan een effici\u00ebnte en snelle toegangsmethode bij de hoofdingang van hun faciliteit. De huidige toegangsmethoden zijn mogelijk traag en vereisen fysiek contact, wat niet ideaal is voor de gewenste gebruikservaring en veiligheid.\n\n**Huidige situatie:**\nMomenteel maakt de klant gebruik van traditionele toegangssystemen die mogelijk niet voldoen aan de eisen voor snelheid en contactloos gebruik. Er is behoefte aan een geavanceerde oplossing die biometrische gezichtsherkenning kan bieden zonder vertraging.\n\n**Gewenste functionaliteit:**\n\n1. **Template opslag op SynCon Evo:**\n   - De klant wenst dat gezichtsherkenning templates worden opgeslagen op het SynCon Evo platform. Dit vereist een betrouwbare en veilige opslag van biometrische gegevens die gemakkelijk toegankelijk zijn voor het gezichtsherkenningssysteem.\n\n2. **Realtime gezichtsherkenning (<1s):**\n   - De klant eist dat het gezichtsherkenningssysteem in staat is om binnen minder dan \u00e9\u00e9n seconde een gezicht te herkennen en toegang te verlenen. Dit benadrukt de noodzaak voor een snelle en effici\u00ebnte verwerking van biometrische gegevens.\n\n3. **Wiegand/OSDP koppeling:**\n   - Er is behoefte aan integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen. Dit zorgt voor compatibiliteit en naadloze communicatie tussen de gezichtsherkenningsscanners en de controller.\n\n**Aanvullende specificaties:**\n- De gezichtsherkenning moet contactloos zijn en uitgevoerd worden via Suprema scanners, die direct gekoppeld zijn aan de controller. Dit vereist een robuuste en betrouwbare hardware-oplossing die compatibel is met de bestaande infrastructuur van de klant.\n\nDit rapport biedt een overzicht van de klantvereisten voor een verbeterd toegangssysteem dat gebruikmaakt van geavanceerde biometrische technologie\u00ebn. Het doel is om een snelle, veilige en contactloze toegang te realiseren die voldoet aan de moderne eisen van de klant.",
    "tech_req": "# Synguard AI Technical Specifications\n\n## Integratie Details\n- **Systeem:** Suprema BioStation 3\n- **API:** Suprema BioStar 2 API\n\n## UI/UX Verwachtingen\n- Beheer van Suprema apparaten vanuit het vertrouwde hardware-overzicht in SynApp.\n\n## Constraints\n- Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).\n\n## Technische Specificaties\n\n### Hardware\n- **Suprema BioStation 3:** Ondersteuning voor gezichtsherkenning en integratie met bestaande toegangssystemen.\n- **SynCon Evo Platform:** Opslag en verwerking van biometrische templates.\n\n### Software\n- **Suprema BioStar 2 API:** Voor communicatie en integratie met Suprema apparaten.\n- **SynApp:** UI/UX interface voor beheer van apparaten.\n\n### Functionaliteit\n1. **Template Opslag op SynCon Evo:**\n   - AVG/GDPR compliant versleuteling van biometrische templates.\n   - Betrouwbare en veilige opslag van gegevens.\n\n2. **Realtime Gezichtsherkenning (<1s):**\n   - Snelle verwerking en herkenning van gezichten binnen minder dan \u00e9\u00e9n seconde.\n   - Contactloze toegang via Suprema scanners.\n\n3. **Wiegand/OSDP Koppeling:**\n   - Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen.\n   - Naadloze communicatie tussen gezichtsherkenningsscanners en de controller.\n\n## Traceability Matrix\n\n| Customer Requirement ID | Description | Technical Specification ID | Description |\n|-------------------------|-------------|----------------------------|-------------|\n| CR-1                    | Template opslag op SynCon Evo | TS-1                       | AVG/GDPR compliant versleuteling en opslag van biometrische templates |\n| CR-2                    | Realtime gezichtsherkenning (<1s) | TS-2                       | Snelle verwerking en herkenning van gezichten binnen minder dan \u00e9\u00e9n seconde |\n| CR-3                    | Wiegand/OSDP koppeling | TS-3                       | Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen |\n\n## Aanvullende Specificaties\n- **Contactloze Gezichtsherkenning:** Uitgevoerd via Suprema scanners, direct gekoppeld aan de controller.\n- **Robuuste Hardware-Oplossing:** Compatibel met de bestaande infrastructuur van de klant.\n\nDit document biedt een gedetailleerd overzicht van de technische specificaties en traceability matrix voor de implementatie van een geavanceerd biometrisch toegangssysteem dat voldoet aan de moderne eisen van de klant.",
    "sow_body": "# Statement of Work (SoW)\n**Project:** Suprema BioStation 3 Integratie met SynApp\n**Documentversie:** 1.0\n**Status:** Draft / For Review\n**Project Owner:** Synguard Product Development\n**Klant:** [In te vullen Klantnaam]\n**Datum:** 16-06-2026\n\n## 1. Projectdoel\nHet doel van dit project is om een geavanceerd biometrisch toegangssysteem te implementeren dat voldoet aan de moderne eisen van de klant. De te automatiseren processen omvatten:\n- Bidirectionele synchronisatie van biometrische gegevens tussen Suprema BioStation 3 en SynCon Evo Platform.\n- Realtime registratie van gezichtsherkenning voor snelle en contactloze toegang.\n- Monitoring van batterijstatussen van Suprema apparaten via SynApp UI.\n\n## 2. Project Scope\n### In Scope\nSynguard zal de volgende functionaliteiten ontwikkelen en opleveren:\n\n- **FR-001 Template Opslag op SynCon Evo**\n  - **Beschrijving:** AVG/GDPR compliant versleuteling en opslag van biometrische templates.\n  - **Omvang:** Implementatie van versleutelingstechnieken en veilige opslag.\n  - **Acceptatiecriteria:** Templates zijn versleuteld en voldoen aan AVG/GDPR richtlijnen.\n\n- **FR-002 Realtime Gezichtsherkenning**\n  - **Beschrijving:** Snelle verwerking en herkenning van gezichten binnen minder dan \u00e9\u00e9n seconde.\n  - **Omvang:** Optimalisatie van gezichtsherkenningsalgoritmen.\n  - **Acceptatiecriteria:** Gezichtsherkenning binnen <1s voor alle geregistreerde gebruikers.\n\n- **FR-003 Wiegand/OSDP Koppeling**\n  - **Beschrijving:** Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen.\n  - **Omvang:** Configuratie van communicatieprotocollen.\n  - **Acceptatiecriteria:** Naadloze communicatie tussen scanners en controllers.\n\n## 3. Technische Scope\n### Integratiearchitectuur\n- **Integratiemodel:** Cloud-to-Cloud Integratie\n- **Communicatie:** REST API / HTTPS/TLS / OAuth of API Key conform specificaties\n- **Bronplatformen:** iLOQ API / Synguard Cloud Platform / SynApp User Interface\n\n## 4. Deliverables\n- **D-001 Productieklare Integratie** - Volledig werkende koppeling.\n- **D-002 Synchronisatie Engine** - Data mapping, bidirectionele sync, foutafhandeling.\n- **D-003 Event Logging Module** - Ingestie, opslag en dashboardvisualisatie.\n- **D-004 Batterij Monitoring Module** - Status ophalen, waarschuwingen en SynApp UI.\n- **D-005 Test & Validatie Rapport** - Scenario's, testresultaten en goedkeuringsstatus.\n- **D-006 Technische Documentatie** - Architectuur, API mapping en onderhoudsrichtlijnen.\n\n## 5. Out of Scope\n### Niet inbegrepen\n- Lokale serverinstallaties, on-premise infrastructuur, netwerkbekabeling, VPN-configuraties, firewalls, hardwareleveringen.\n### Integratiebeperkingen\n- De integratie is expliciet beperkt tot functionaliteiten die beschikbaar zijn via de offici\u00eble API's.\n\n## 6. Rollen & Verantwoordelijkheden\n- **Synguard:** Analyse, ontwikkeling, testing, technische documentatie en go-live support.\n- **Klant:** Beschikbaar stellen van API-toegang, testaccounts, functionele validatie en formele acceptatie.\n- **API/Technologie Partner:** Beschikbaarheid van API-services en documentatie.\n\n## 7. Planning & Mijlpalen\n### Mijlpalen\n- **M1 Analyse Afgerond** - API-connectiviteit bevestigd.\n- **M2 Integratie Voltooid** - Koppelingen operationeel.\n- **M3 Acceptatietesten Geslaagd** - Alle scenario's succesvol uitgevoerd.\n- **M4 Productie Go-Live** - Operationeel in productie.\n\n## 8. Afhankelijkheden & Risico's\nDe beschikbaarheid van API-services en testomgevingen is cruciaal voor de voortgang van het project. Eventuele onderbrekingen kunnen leiden tot vertragingen in de implementatie.\n\n## 9. Change Request Procedure\nWijzigingen in de projectscope moeten formeel worden aangevraagd via een Change Request formulier. Elke wijziging vereist goedkeuring van zowel Synguard als de klant voordat deze wordt doorgevoerd.\n\n## 10. Acceptatie & Sign-Off\nDe formele oplevering van het project vereist dat alle deliverables voldoen aan de gespecificeerde acceptatiecriteria en dat de klant formeel akkoord gaat met de resultaten.",
    "current_filepath": "outputs/generated_srs\\20260616_0943_klant_eist_snelle__contactloz.md",
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
            "FR/NFR ID": "CR-1",
            "Traces To CN": "TS-1",
            "Description": "Template opslag op SynCon Evo",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "AVG/GDPR compliant versleuteling en opslag van biometrische templates"
        },
        {
            "FR/NFR ID": "CR-2",
            "Traces To CN": "TS-2",
            "Description": "Realtime gezichtsherkenning (<1s)",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Snelle verwerking en herkenning van gezichten binnen minder dan \u00e9\u00e9n seconde"
        },
        {
            "FR/NFR ID": "CR-3",
            "Traces To CN": "TS-3",
            "Description": "Wiegand/OSDP koppeling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Integratie met bestaande toegangssystemen via Wiegand of OSDP protocollen"
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