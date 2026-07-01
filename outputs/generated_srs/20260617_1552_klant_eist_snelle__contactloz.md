"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller."
[---SPLIT-DOSSIER---]
**Customer Requirements Rapport**

**Probleem:**
De klant heeft behoefte aan een efficiënte en veilige toegangscontrole bij de hoofdingang van hun faciliteit. De huidige methoden voldoen niet aan de eisen voor snelheid en contactloze toegang, wat leidt tot vertragingen en ongemak voor gebruikers.

**Huidige situatie:**
Momenteel maakt de klant gebruik van een verouderd toegangscontrolesysteem dat niet in staat is om snel en contactloos toegang te verlenen. Dit systeem is niet uitgerust met geavanceerde biometrische technologieën zoals gezichtsherkenning, wat resulteert in een minder efficiënte toegangsprocedure.

**Gewenste functionaliteit:**
1. **Template opslag op SynCon Evo:**
   - De klant wenst dat gezichtsherkenningssjablonen worden opgeslagen op het SynCon Evo-platform. Dit zorgt voor een gecentraliseerd en efficiënt beheer van biometrische gegevens.

2. **Realtime gezichtsherkenning (<1s):**
   - De klant eist een gezichtsherkenningssysteem dat in staat is om binnen minder dan één seconde een gebruiker te identificeren. Dit moet zorgen voor een snelle en naadloze toegang zonder wachttijden.

3. **Wiegand/OSDP koppeling:**
   - Er is behoefte aan integratie met bestaande toegangscontrolesystemen via Wiegand of OSDP protocollen. Dit zorgt voor compatibiliteit en eenvoudige implementatie met de huidige infrastructuur.

**Aanvullende specificaties:**
- De klant heeft specifiek aangegeven dat de gezichtsherkenning moet worden uitgevoerd via Suprema scanners. Deze scanners moeten direct gekoppeld zijn aan de controller om de snelheid en efficiëntie van de toegang te maximaliseren.
- Het systeem moet contactloos zijn om het gebruiksgemak te verhogen en hygiënische voordelen te bieden.

Dit rapport vat de kernvereisten van de klant samen en biedt een duidelijk overzicht van de gewenste verbeteringen in hun toegangscontrolesysteem.
[---SPLIT-DOSSIER---]
# Synguard AI Technical Specifications

## Integratie Details

- **Systeem**: Suprema BioStation 3
- **API**: Suprema BioStar 2 API

## UI/UX Verwachtingen

- Beheer van Suprema apparaten vanuit het vertrouwde hardware-overzicht in SynApp.

## Constraints

- Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).

## Technische Specificaties

### Gezichtsherkenning

- **Opslag**: Gezichtsherkenningssjablonen worden opgeslagen op het SynCon Evo-platform.
- **Snelheid**: Realtime gezichtsherkenning binnen minder dan 1 seconde.
- **Contactloos**: Het systeem moet volledig contactloos zijn voor gebruiksgemak en hygiëne.

### Integratie

- **Protocollen**: Ondersteuning voor Wiegand en OSDP voor integratie met bestaande toegangscontrolesystemen.
- **Directe Koppeling**: Suprema scanners moeten direct gekoppeld zijn aan de controller voor maximale snelheid en efficiëntie.

### Beveiliging

- **Versleuteling**: Biometrische gegevens moeten AVG/GDPR compliant versleuteld zijn. Geen opslag van echte foto's, alleen gehashte templates.

## Traceability Matrix

| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |
|------------------|--------------|----------------------------|-----------------------|
| CR-01            | Template opslag op SynCon Evo | TS-01 | Gezichtsherkenningssjablonen worden opgeslagen op SynCon Evo |
| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Gezichtsherkenning binnen minder dan 1 seconde |
| CR-03            | Wiegand/OSDP koppeling | TS-03 | Ondersteuning voor Wiegand en OSDP protocollen |
| CR-04            | Contactloze toegang | TS-04 | Volledig contactloos systeem |
| CR-05            | AVG/GDPR compliant versleuteling | TS-05 | Biometrische gegevens versleuteld en gehashed |

## Implementatie Details

1. **Template Opslag (TS-01)**:
   - Gezichtsherkenningssjablonen worden centraal beheerd op het SynCon Evo-platform voor efficiëntie en beheerbaarheid.

2. **Realtime Gezichtsherkenning (TS-02)**:
   - Implementatie van snelle algoritmen en directe koppeling met Suprema scanners om herkenning binnen minder dan 1 seconde te garanderen.

3. **Protocollen Integratie (TS-03)**:
   - Ondersteuning voor Wiegand en OSDP protocollen om naadloze integratie met bestaande systemen te verzekeren.

4. **Contactloze Toegang (TS-04)**:
   - Gebruik van geavanceerde sensoren en algoritmen om volledig contactloze toegang te bieden.

5. **Beveiliging en Versleuteling (TS-05)**:
   - Gebruik van hashing technieken om biometrische gegevens AVG/GDPR compliant te maken zonder opslag van echte foto's.

Deze specificaties en traceability matrix bieden een gedetailleerd overzicht van de technische vereisten en implementatie details voor het nieuwe toegangscontrolesysteem.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller.\"",
    "cust_req": "**Customer Requirements Rapport**\n\n**Probleem:**\nDe klant heeft behoefte aan een effici\u00ebnte en veilige toegangscontrole bij de hoofdingang van hun faciliteit. De huidige methoden voldoen niet aan de eisen voor snelheid en contactloze toegang, wat leidt tot vertragingen en ongemak voor gebruikers.\n\n**Huidige situatie:**\nMomenteel maakt de klant gebruik van een verouderd toegangscontrolesysteem dat niet in staat is om snel en contactloos toegang te verlenen. Dit systeem is niet uitgerust met geavanceerde biometrische technologie\u00ebn zoals gezichtsherkenning, wat resulteert in een minder effici\u00ebnte toegangsprocedure.\n\n**Gewenste functionaliteit:**\n1. **Template opslag op SynCon Evo:**\n   - De klant wenst dat gezichtsherkenningssjablonen worden opgeslagen op het SynCon Evo-platform. Dit zorgt voor een gecentraliseerd en effici\u00ebnt beheer van biometrische gegevens.\n\n2. **Realtime gezichtsherkenning (<1s):**\n   - De klant eist een gezichtsherkenningssysteem dat in staat is om binnen minder dan \u00e9\u00e9n seconde een gebruiker te identificeren. Dit moet zorgen voor een snelle en naadloze toegang zonder wachttijden.\n\n3. **Wiegand/OSDP koppeling:**\n   - Er is behoefte aan integratie met bestaande toegangscontrolesystemen via Wiegand of OSDP protocollen. Dit zorgt voor compatibiliteit en eenvoudige implementatie met de huidige infrastructuur.\n\n**Aanvullende specificaties:**\n- De klant heeft specifiek aangegeven dat de gezichtsherkenning moet worden uitgevoerd via Suprema scanners. Deze scanners moeten direct gekoppeld zijn aan de controller om de snelheid en effici\u00ebntie van de toegang te maximaliseren.\n- Het systeem moet contactloos zijn om het gebruiksgemak te verhogen en hygi\u00ebnische voordelen te bieden.\n\nDit rapport vat de kernvereisten van de klant samen en biedt een duidelijk overzicht van de gewenste verbeteringen in hun toegangscontrolesysteem.",
    "tech_req": "# Synguard AI Technical Specifications\n\n## Integratie Details\n\n- **Systeem**: Suprema BioStation 3\n- **API**: Suprema BioStar 2 API\n\n## UI/UX Verwachtingen\n\n- Beheer van Suprema apparaten vanuit het vertrouwde hardware-overzicht in SynApp.\n\n## Constraints\n\n- Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).\n\n## Technische Specificaties\n\n### Gezichtsherkenning\n\n- **Opslag**: Gezichtsherkenningssjablonen worden opgeslagen op het SynCon Evo-platform.\n- **Snelheid**: Realtime gezichtsherkenning binnen minder dan 1 seconde.\n- **Contactloos**: Het systeem moet volledig contactloos zijn voor gebruiksgemak en hygi\u00ebne.\n\n### Integratie\n\n- **Protocollen**: Ondersteuning voor Wiegand en OSDP voor integratie met bestaande toegangscontrolesystemen.\n- **Directe Koppeling**: Suprema scanners moeten direct gekoppeld zijn aan de controller voor maximale snelheid en effici\u00ebntie.\n\n### Beveiliging\n\n- **Versleuteling**: Biometrische gegevens moeten AVG/GDPR compliant versleuteld zijn. Geen opslag van echte foto's, alleen gehashte templates.\n\n## Traceability Matrix\n\n| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |\n|------------------|--------------|----------------------------|-----------------------|\n| CR-01            | Template opslag op SynCon Evo | TS-01 | Gezichtsherkenningssjablonen worden opgeslagen op SynCon Evo |\n| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Gezichtsherkenning binnen minder dan 1 seconde |\n| CR-03            | Wiegand/OSDP koppeling | TS-03 | Ondersteuning voor Wiegand en OSDP protocollen |\n| CR-04            | Contactloze toegang | TS-04 | Volledig contactloos systeem |\n| CR-05            | AVG/GDPR compliant versleuteling | TS-05 | Biometrische gegevens versleuteld en gehashed |\n\n## Implementatie Details\n\n1. **Template Opslag (TS-01)**:\n   - Gezichtsherkenningssjablonen worden centraal beheerd op het SynCon Evo-platform voor effici\u00ebntie en beheerbaarheid.\n\n2. **Realtime Gezichtsherkenning (TS-02)**:\n   - Implementatie van snelle algoritmen en directe koppeling met Suprema scanners om herkenning binnen minder dan 1 seconde te garanderen.\n\n3. **Protocollen Integratie (TS-03)**:\n   - Ondersteuning voor Wiegand en OSDP protocollen om naadloze integratie met bestaande systemen te verzekeren.\n\n4. **Contactloze Toegang (TS-04)**:\n   - Gebruik van geavanceerde sensoren en algoritmen om volledig contactloze toegang te bieden.\n\n5. **Beveiliging en Versleuteling (TS-05)**:\n   - Gebruik van hashing technieken om biometrische gegevens AVG/GDPR compliant te maken zonder opslag van echte foto's.\n\nDeze specificaties en traceability matrix bieden een gedetailleerd overzicht van de technische vereisten en implementatie details voor het nieuwe toegangscontrolesysteem.",
    "sow_body": "# Statement of Work (SoW)\n**Project:** Suprema BioStation 3 Integratie met SynApp\n**Documentversie:** 1.0\n**Status:** Draft / For Review\n**Project Owner:** Synguard Product Development\n**Klant:** [In te vullen Klantnaam]\n**Datum:** 17-06-2026\n\n## 1. Projectdoel\nHet doel van dit project is om een naadloze integratie te realiseren tussen de Suprema BioStation 3 en SynApp, waarbij de volgende processen worden geautomatiseerd:\n- Bidirectionele synchronisatie van gezichtsherkenningssjablonen.\n- Realtime registratie van toegangsgebeurtenissen.\n- Monitoring van batterijstatussen van gekoppelde apparaten.\n\n## 2. Project Scope\n### In Scope\nSynguard zal de volgende functionaliteiten ontwikkelen en opleveren:\n\n- **FR-001 Gezichtsherkenningsintegratie**\n  - **Beschrijving:** Integratie van gezichtsherkenning met SynApp voor realtime toegang.\n  - **Omvang:** Implementatie van snelle algoritmen en directe koppeling met Suprema scanners.\n  - **Acceptatiecriteria:** Gezichtsherkenning binnen minder dan 1 seconde.\n\n- **FR-002 Beveiligde Template Opslag**\n  - **Beschrijving:** AVG/GDPR compliant opslag van biometrische templates.\n  - **Omvang:** Gebruik van hashing technieken op het SynCon Evo-platform.\n  - **Acceptatiecriteria:** Geen opslag van echte foto's, alleen gehashte templates.\n\n- **FR-003 Protocollen Integratie**\n  - **Beschrijving:** Ondersteuning voor Wiegand en OSDP protocollen.\n  - **Omvang:** Naadloze integratie met bestaande toegangscontrolesystemen.\n  - **Acceptatiecriteria:** Volledige operationele koppeling.\n\n## 3. Technische Scope\n### Integratiearchitectuur\n- **Integratiemodel:** Cloud-to-Cloud Integratie\n- **Communicatie:** REST API / HTTPS/TLS / OAuth of API Key conform specificaties\n- **Bronplatformen:** iLOQ API / Synguard Cloud Platform / SynApp User Interface\n\n## 4. Deliverables\n- **D-001 Productieklare Integratie** - Volledig werkende koppeling.\n- **D-002 Synchronisatie Engine** - Data mapping, bidirectionele sync, foutafhandeling.\n- **D-003 Event Logging Module** - Ingestie, opslag en dashboardvisualisatie.\n- **D-004 Batterij Monitoring Module** - Status ophalen, waarschuwingen en SynApp UI.\n- **D-005 Test & Validatie Rapport** - Scenario's, testresultaten en goedkeuringsstatus.\n- **D-006 Technische Documentatie** - Architectuur, API mapping en onderhoudsrichtlijnen.\n\n## 5. Out of Scope\n### Niet inbegrepen\n- Lokale serverinstallaties, on-premise infrastructuur, netwerkbekabeling, VPN-configuraties, firewalls, hardwareleveringen.\n### Integratiebeperkingen\n- De integratie is expliciet beperkt tot functionaliteiten die beschikbaar zijn via de offici\u00eble API's.\n\n## 6. Rollen & Verantwoordelijkheden\n- **Synguard:** Analyse, ontwikkeling, testing, technische documentatie en go-live support.\n- **Klant:** Beschikbaar stellen van API-toegang, testaccounts, functionele validatie en formele acceptatie.\n- **API/Technologie Partner:** Beschikbaarheid van API-services en documentatie.\n\n## 7. Planning & Mijlpalen\n### Mijlpalen\n- **M1 Analyse Afgerond** - API-connectiviteit bevestigd.\n- **M2 Integratie Voltooid** - Koppelingen operationeel.\n- **M3 Acceptatietesten Geslaagd** - Alle scenario's succesvol uitgevoerd.\n- **M4 Productie Go-Live** - Operationeel in productie.\n\n## 8. Afhankelijkheden & Risico's\n- Beschikbaarheid van API's en testomgevingen kan de voortgang be\u00efnvloeden.\n- Onvoorziene wijzigingen in API-specificaties kunnen extra ontwikkeltijd vereisen.\n\n## 9. Change Request Procedure\nWijzigingen in de scope moeten schriftelijk worden aangevraagd en goedgekeurd door zowel Synguard als de klant. Elke wijziging kan invloed hebben op de planning en kosten.\n\n## 10. Acceptatie & Sign-Off\nDe formele oplevering vereist goedkeuring van de klant na succesvolle voltooiing van alle acceptatietesten en verificatie van de deliverables.",
    "current_filepath": "outputs/generated_srs\\20260617_1552_klant_eist_snelle__contactloz.md",
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
            "QA / Test Scenario (Acceptatiecriterium)": "Gezichtsherkenningssjablonen worden opgeslagen op SynCon Evo"
        },
        {
            "FR/NFR ID": "CR-02",
            "Traces To CN": "TS-02",
            "Description": "Realtime gezichtsherkenning (<1s)",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Gezichtsherkenning binnen minder dan 1 seconde"
        },
        {
            "FR/NFR ID": "CR-03",
            "Traces To CN": "TS-03",
            "Description": "Wiegand/OSDP koppeling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Ondersteuning voor Wiegand en OSDP protocollen"
        },
        {
            "FR/NFR ID": "CR-04",
            "Traces To CN": "TS-04",
            "Description": "Contactloze toegang",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Volledig contactloos systeem"
        },
        {
            "FR/NFR ID": "CR-05",
            "Traces To CN": "TS-05",
            "Description": "AVG/GDPR compliant versleuteling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Biometrische gegevens versleuteld en gehashed"
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