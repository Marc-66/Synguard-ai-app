"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller."
[---SPLIT-DOSSIER---]
**Customer Requirements Rapport**

**Probleem:**
De klant heeft behoefte aan een efficiënte en snelle methode voor toegangscontrole bij de hoofdingang van hun faciliteit. De huidige systemen voldoen niet aan de eisen voor snelheid en contactloze werking, wat leidt tot vertragingen en ongemak voor gebruikers.

**Huidige situatie:**
Momenteel maakt de klant gebruik van een verouderd toegangscontrolesysteem dat niet in staat is om gezichtsherkenning snel en contactloos uit te voeren. Dit systeem is niet direct gekoppeld aan de controller, wat resulteert in een trage verwerking en een minder gebruiksvriendelijke ervaring.

**Gewenste functionaliteit:**
1. **Template opslag op SynCon Evo:**
   De klant wenst dat gezichtsherkenning templates worden opgeslagen op het SynCon Evo platform. Dit zorgt voor een centrale en efficiënte opslag van biometrische gegevens, wat de snelheid en betrouwbaarheid van het systeem verhoogt.

2. **Realtime gezichtsherkenning (<1s):**
   Het systeem moet in staat zijn om gezichtsherkenning in minder dan één seconde uit te voeren. Dit is essentieel voor een snelle en soepele doorstroming bij de hoofdingang, zonder dat gebruikers hoeven te stoppen of te wachten.

3. **Wiegand/OSDP koppeling:**
   Er is behoefte aan een directe koppeling via Wiegand of OSDP protocollen. Dit zorgt voor een veilige en betrouwbare communicatie tussen de Suprema scanners en de controller, waardoor de integriteit van het toegangscontrolesysteem gewaarborgd blijft.

**Conclusie:**
Om aan de eisen van de klant te voldoen, moet het nieuwe systeem snelle, contactloze biometrische gezichtsherkenning bieden via Suprema scanners die direct gekoppeld zijn aan de controller. Het systeem moet gebruik maken van SynCon Evo voor template opslag en moet gezichtsherkenning in realtime (<1s) kunnen uitvoeren, met ondersteuning voor Wiegand/OSDP koppelingen.
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

### Hardware
- **Apparaat**: Suprema BioStation 3
- **Communicatie Protocollen**: Wiegand, OSDP
- **Opslag**: SynCon Evo platform voor biometrische templates

### Software
- **API**: Suprema BioStar 2 API voor integratie en communicatie
- **Gezichtsherkenning**: Realtime (<1s) verwerking

### Beveiliging
- **Versleuteling**: AVG/GDPR compliant hashing van biometrische templates
- **Data Opslag**: Geen opslag van echte foto's, alleen gehashte templates

## Traceability Matrix

| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |
|------------------|--------------|----------------------------|-----------------------|
| CR-01            | Template opslag op SynCon Evo | TS-01 | Implementatie van centrale opslag van biometrische templates op SynCon Evo platform |
| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Optimalisatie van gezichtsherkenningsalgoritmes voor snelle verwerking |
| CR-03            | Wiegand/OSDP koppeling | TS-03 | Integratie van Wiegand en OSDP protocollen voor directe communicatie met de controller |
| CR-04            | AVG/GDPR compliant versleuteling | TS-04 | Implementatie van hashing technieken voor biometrische templates |

## Conclusie
Het nieuwe systeem moet voldoen aan de eisen van snelle, contactloze biometrische gezichtsherkenning via Suprema scanners die direct gekoppeld zijn aan de controller. Het systeem maakt gebruik van SynCon Evo voor template opslag en moet gezichtsherkenning in realtime (<1s) kunnen uitvoeren, met ondersteuning voor Wiegand/OSDP koppelingen. Biometrische gegevens moeten AVG/GDPR compliant worden versleuteld.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Klant eist snelle, contactloze biometrische gezichtsherkenning bij de hoofdingang via Suprema scanners direct gekoppeld aan de controller.\"",
    "cust_req": "**Customer Requirements Rapport**\n\n**Probleem:**\nDe klant heeft behoefte aan een effici\u00ebnte en snelle methode voor toegangscontrole bij de hoofdingang van hun faciliteit. De huidige systemen voldoen niet aan de eisen voor snelheid en contactloze werking, wat leidt tot vertragingen en ongemak voor gebruikers.\n\n**Huidige situatie:**\nMomenteel maakt de klant gebruik van een verouderd toegangscontrolesysteem dat niet in staat is om gezichtsherkenning snel en contactloos uit te voeren. Dit systeem is niet direct gekoppeld aan de controller, wat resulteert in een trage verwerking en een minder gebruiksvriendelijke ervaring.\n\n**Gewenste functionaliteit:**\n1. **Template opslag op SynCon Evo:**\n   De klant wenst dat gezichtsherkenning templates worden opgeslagen op het SynCon Evo platform. Dit zorgt voor een centrale en effici\u00ebnte opslag van biometrische gegevens, wat de snelheid en betrouwbaarheid van het systeem verhoogt.\n\n2. **Realtime gezichtsherkenning (<1s):**\n   Het systeem moet in staat zijn om gezichtsherkenning in minder dan \u00e9\u00e9n seconde uit te voeren. Dit is essentieel voor een snelle en soepele doorstroming bij de hoofdingang, zonder dat gebruikers hoeven te stoppen of te wachten.\n\n3. **Wiegand/OSDP koppeling:**\n   Er is behoefte aan een directe koppeling via Wiegand of OSDP protocollen. Dit zorgt voor een veilige en betrouwbare communicatie tussen de Suprema scanners en de controller, waardoor de integriteit van het toegangscontrolesysteem gewaarborgd blijft.\n\n**Conclusie:**\nOm aan de eisen van de klant te voldoen, moet het nieuwe systeem snelle, contactloze biometrische gezichtsherkenning bieden via Suprema scanners die direct gekoppeld zijn aan de controller. Het systeem moet gebruik maken van SynCon Evo voor template opslag en moet gezichtsherkenning in realtime (<1s) kunnen uitvoeren, met ondersteuning voor Wiegand/OSDP koppelingen.",
    "tech_req": "# Synguard AI Technical Specifications\n\n## Integratie Details\n- **Systeem**: Suprema BioStation 3\n- **API**: Suprema BioStar 2 API\n\n## UI/UX Verwachtingen\n- Beheer van Suprema apparaten vanuit het vertrouwde hardware-overzicht in SynApp.\n\n## Constraints\n- Biometrische templates moeten AVG/GDPR compliant versleuteld zijn (hashing, geen opslag van echte foto's).\n\n## Technische Specificaties\n\n### Hardware\n- **Apparaat**: Suprema BioStation 3\n- **Communicatie Protocollen**: Wiegand, OSDP\n- **Opslag**: SynCon Evo platform voor biometrische templates\n\n### Software\n- **API**: Suprema BioStar 2 API voor integratie en communicatie\n- **Gezichtsherkenning**: Realtime (<1s) verwerking\n\n### Beveiliging\n- **Versleuteling**: AVG/GDPR compliant hashing van biometrische templates\n- **Data Opslag**: Geen opslag van echte foto's, alleen gehashte templates\n\n## Traceability Matrix\n\n| Klantvereiste ID | Beschrijving | Technische Specificatie ID | Implementatie Details |\n|------------------|--------------|----------------------------|-----------------------|\n| CR-01            | Template opslag op SynCon Evo | TS-01 | Implementatie van centrale opslag van biometrische templates op SynCon Evo platform |\n| CR-02            | Realtime gezichtsherkenning (<1s) | TS-02 | Optimalisatie van gezichtsherkenningsalgoritmes voor snelle verwerking |\n| CR-03            | Wiegand/OSDP koppeling | TS-03 | Integratie van Wiegand en OSDP protocollen voor directe communicatie met de controller |\n| CR-04            | AVG/GDPR compliant versleuteling | TS-04 | Implementatie van hashing technieken voor biometrische templates |\n\n## Conclusie\nHet nieuwe systeem moet voldoen aan de eisen van snelle, contactloze biometrische gezichtsherkenning via Suprema scanners die direct gekoppeld zijn aan de controller. Het systeem maakt gebruik van SynCon Evo voor template opslag en moet gezichtsherkenning in realtime (<1s) kunnen uitvoeren, met ondersteuning voor Wiegand/OSDP koppelingen. Biometrische gegevens moeten AVG/GDPR compliant worden versleuteld.",
    "sow_body": "```markdown\n# Statement of Work (SoW)\n**Project:** Suprema BioStation 3 Integratie met SynApp\n**Documentversie:** 1.0\n**Status:** Draft / For Review\n**Project Owner:** Synguard Product Development\n**Klant:** [In te vullen Klantnaam]\n**Datum:** 16-06-2026\n\n## 1. Projectdoel\nHet doel van dit project is om een naadloze integratie te realiseren tussen de Suprema BioStation 3 en het SynApp platform, waarbij de volgende processen worden geautomatiseerd:\n- Bidirectionele synchronisatie van gebruikersgegevens tussen Suprema BioStation 3 en SynApp.\n- Realtime registratie en verwerking van biometrische gegevens.\n- Monitoring van batterijstatussen van aangesloten apparaten.\n\n## 2. Project Scope\n### In Scope\nSynguard zal de volgende functionaliteiten ontwikkelen en opleveren:\n- **FR-001 Biometrische Template Opslag**\n  - **Beschrijving:** Implementatie van centrale opslag van biometrische templates op het SynCon Evo platform.\n  - **Omvang:** Opslag en beheer van gehashte biometrische templates.\n  - **Acceptatiecriteria:** Templates worden AVG/GDPR compliant opgeslagen zonder gebruik van echte foto's.\n\n- **FR-002 Realtime Gezichtsherkenning**\n  - **Beschrijving:** Optimalisatie van gezichtsherkenningsalgoritmes voor snelle verwerking.\n  - **Omvang:** Verwerkingstijd van minder dan 1 seconde voor gezichtsherkenning.\n  - **Acceptatiecriteria:** Gezichtsherkenning wordt binnen de gestelde tijdslimiet uitgevoerd.\n\n- **FR-003 Communicatie Protocollen**\n  - **Beschrijving:** Integratie van Wiegand en OSDP protocollen voor directe communicatie met de controller.\n  - **Omvang:** Ondersteuning van beide protocollen voor apparaatcommunicatie.\n  - **Acceptatiecriteria:** Succesvolle communicatie via Wiegand en OSDP.\n\n- **FR-004 AVG/GDPR Compliant Versleuteling**\n  - **Beschrijving:** Implementatie van hashing technieken voor biometrische templates.\n  - **Omvang:** Versleuteling van alle biometrische gegevens.\n  - **Acceptatiecriteria:** Gegevens worden opgeslagen volgens AVG/GDPR richtlijnen.\n\n## 3. Technische Scope\n### Integratiearchitectuur\n- **Integratiemodel:** Cloud-to-Cloud Integratie\n- **Communicatie:** REST API / HTTPS/TLS / OAuth of API Key conform specificaties\n- **Bronplatformen:** iLOQ API / Synguard Cloud Platform / SynApp User Interface\n\n## 4. Deliverables\n- **D-001 Productieklare Integratie** - Volledig werkende koppeling.\n- **D-002 Synchronisatie Engine** - Data mapping, bidirectionele sync, foutafhandeling.\n- **D-003 Event Logging Module** - Ingestie, opslag en dashboardvisualisatie.\n- **D-004 Batterij Monitoring Module** - Status ophalen, waarschuwingen en SynApp UI.\n- **D-005 Test & Validatie Rapport** - Scenario's, testresultaten en goedkeuringsstatus.\n- **D-006 Technische Documentatie** - Architectuur, API mapping en onderhoudsrichtlijnen.\n\n## 5. Out of Scope\n### Niet inbegrepen\n- Lokale serverinstallaties, on-premise infrastructuur, netwerkbekabeling, VPN-configuraties, firewalls, hardwareleveringen.\n### Integratiebeperkingen\n- De integratie is expliciet beperkt tot functionaliteiten die beschikbaar zijn via de offici\u00eble API's.\n\n## 6. Rollen & Verantwoordelijkheden\n- **Synguard:** Analyse, ontwikkeling, testing, technische documentatie en go-live support.\n- **Klant:** Beschikbaar stellen van API-toegang, testaccounts, functionele validatie en formele acceptatie.\n- **API/Technologie Partner:** Beschikbaarheid van API-services en documentatie.\n\n## 7. Planning & Mijlpalen\n| Fase | Activiteit | Duur |\n|------|------------|------|\n| Analyse | API-connectiviteit bevestigen | 2 weken |\n| Ontwikkeling | Integratie ontwikkelen | 4 weken |\n| Testen | Acceptatietesten uitvoeren | 2 weken |\n| Implementatie | Productie Go-Live | 1 week |\n\n### Mijlpalen\n- **M1 Analyse Afgerond** - API-connectiviteit bevestigd.\n- **M2 Integratie Voltooid** - Koppelingen operationeel.\n- **M3 Acceptatietesten Geslaagd** - Alle scenario's succesvol uitgevoerd.\n- **M4 Productie Go-Live** - Operationeel in productie.\n\n## 8. Afhankelijkheden & Risico's\nEr zijn risico's verbonden aan de beschikbaarheid van de API en de testomgevingen. Eventuele vertragingen in de beschikbaarheid kunnen de projectplanning be\u00efnvloeden.\n\n## 9. Change Request Procedure\nAlle verzoeken tot wijziging van de projectscope moeten schriftelijk worden ingediend en goedgekeurd door zowel Synguard als de klant. Wijzigingen kunnen leiden tot aanpassingen in de planning en kosten.\n\n## 10. Acceptatie & Sign-Off\nDe formele acceptatie van het project vindt plaats na succesvolle voltooiing van alle testscenario's en goedkeuring door de klant. De oplevering wordt formeel ondertekend door beide partijen.\n```",
    "current_filepath": "outputs/generated_srs\\20260616_0941_klant_eist_snelle__contactloz.md",
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
            "QA / Test Scenario (Acceptatiecriterium)": "Implementatie van centrale opslag van biometrische templates op SynCon Evo platform"
        },
        {
            "FR/NFR ID": "CR-02",
            "Traces To CN": "TS-02",
            "Description": "Realtime gezichtsherkenning (<1s)",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Optimalisatie van gezichtsherkenningsalgoritmes voor snelle verwerking"
        },
        {
            "FR/NFR ID": "CR-03",
            "Traces To CN": "TS-03",
            "Description": "Wiegand/OSDP koppeling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Integratie van Wiegand en OSDP protocollen voor directe communicatie met de controller"
        },
        {
            "FR/NFR ID": "CR-04",
            "Traces To CN": "TS-04",
            "Description": "AVG/GDPR compliant versleuteling",
            "Technische Architectuur Component": "[In te vullen door Engineering]",
            "QA / Test Scenario (Acceptatiecriterium)": "Implementatie van hashing technieken voor biometrische templates"
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