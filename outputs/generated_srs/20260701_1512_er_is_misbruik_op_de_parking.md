"Er is misbruik op de parking: medewerkers geven hun badge door. We hebben Timed Anti-Passback nodig op de slagbomen."
[---SPLIT-DOSSIER---]
# Customer Requirements Document (CRD)

## Samenvatting

Dit document beschrijft de vereisten voor het implementeren van een Timed Anti-Passback systeem op de slagbomen van de parkeerfaciliteit. Het doel is om misbruik van toegangspassen door medewerkers te voorkomen, waarbij passen worden doorgegeven om meerdere voertuigen toegang te verlenen zonder toestemming.

## Customer Needs

**CN-001: Preventie van badge-misbruik**  
De klant heeft behoefte aan een systeem dat voorkomt dat medewerkers hun toegangspassen doorgeven aan anderen om meerdere voertuigen toegang te verlenen tot de parkeerfaciliteit.

**CN-002: Verbeterde beveiliging van de parkeerfaciliteit**  
Het systeem moet bijdragen aan de algehele beveiliging van de parkeerfaciliteit door ongeautoriseerde toegang te minimaliseren.

## Functionele Eisen

**FE-001: Implementatie van Timed Anti-Passback**  
Het systeem moet een Timed Anti-Passback mechanisme bevatten dat voorkomt dat dezelfde badge binnen een bepaalde tijdsperiode opnieuw wordt gebruikt om toegang te verkrijgen.

**FE-002: Configuratie van tijdsintervallen**  
Het systeem moet de mogelijkheid bieden om de tijdsintervallen voor de Anti-Passback functionaliteit aan te passen, zodat deze kan worden afgestemd op de specifieke behoeften van de klant.

**FE-003: Logregistratie van toegangspogingen**  
Het systeem moet alle toegangspogingen registreren, inclusief succesvolle en geweigerde pogingen, om een audit trail te bieden voor beveiligingsdoeleinden.

## Niet-functionele Eisen

**NFE-001: Betrouwbaarheid**  
Het systeem moet een hoge mate van betrouwbaarheid bieden, met minimale downtime, om ervoor te zorgen dat de parkeerfaciliteit continu beveiligd is.

**NFE-002: Gebruiksvriendelijkheid**  
De interface voor het beheren van de Timed Anti-Passback instellingen moet gebruiksvriendelijk zijn, zodat beheerders eenvoudig aanpassingen kunnen maken zonder uitgebreide training.

**NFE-003: Schaalbaarheid**  
Het systeem moet schaalbaar zijn om toekomstige uitbreidingen van de parkeerfaciliteit of wijzigingen in het aantal gebruikers te kunnen ondersteunen.

**NFE-004: Compatibiliteit**  
Het systeem moet compatibel zijn met de bestaande toegangscontrole-infrastructuur van de parkeerfaciliteit om een naadloze integratie te garanderen.
[---SPLIT-DOSSIER---]
# Technische Specificaties voor Timed Anti-Passback Systeem

## Integratie Details

1. **Systeemarchitectuur**: Het systeem zal worden geïntegreerd met de bestaande toegangscontrole-infrastructuur van de parkeerfaciliteit. Dit omvat de slagbomen, badgelezers en het centrale toegangscontrolesysteem.
   
2. **Communicatieprotocol**: Het systeem zal gebruik maken van een standaard communicatieprotocol (bijv. TCP/IP) om gegevens tussen de badgelezers en het centrale systeem uit te wisselen.

3. **Database**: Een centrale database zal worden gebruikt om loggegevens van toegangspogingen op te slaan. Deze database moet compatibel zijn met de bestaande IT-infrastructuur van de klant.

## UI/UX Verwachtingen

1. **Beheerdersinterface**: De interface moet intuïtief en gebruiksvriendelijk zijn, met een dashboard dat een overzicht biedt van alle toegangspogingen en de status van het Anti-Passback systeem.

2. **Configuratiepaneel**: Beheerders moeten eenvoudig tijdsintervallen kunnen instellen en wijzigen via een configuratiepaneel. Dit paneel moet duidelijke instructies en feedback geven bij het opslaan van wijzigingen.

3. **Logboekweergave**: Er moet een functie zijn om logboeken te bekijken en te filteren op datum, tijd, badge-ID en type toegangspoging (succesvol of geweigerd).

## Constraints

1. **Compatibiliteit**: Het systeem moet compatibel zijn met de bestaande hardware en software van de parkeerfaciliteit zonder dat er grote aanpassingen nodig zijn.

2. **Veiligheid**: Gegevensoverdracht tussen de componenten van het systeem moet beveiligd zijn om ongeautoriseerde toegang en gegevensmanipulatie te voorkomen.

3. **Prestaties**: Het systeem moet snel reageren op toegangspogingen en binnen enkele seconden beslissingen kunnen nemen om wachttijden bij de slagbomen te minimaliseren.

## Traceability Matrix

| FR/NFR ID | Traces To CN | Description | Technische Architectuur Component | QA / Test Scenario |
|-----------|--------------|-------------|-----------------------------------|--------------------|
| FE-001    | CN-001       | Implementatie van Timed Anti-Passback | Toegangscontrole Software | Test of het systeem een badge binnen de ingestelde tijdsperiode blokkeert na gebruik. |
| FE-002    | CN-001       | Configuratie van tijdsintervallen | Beheerdersinterface | Test de mogelijkheid om tijdsintervallen in te stellen en te wijzigen. |
| FE-003    | CN-002       | Logregistratie van toegangspogingen | Centrale Database | Verifieer dat alle toegangspogingen correct worden gelogd en opgeslagen. |
| NFE-001   | CN-002       | Betrouwbaarheid | Systeemarchitectuur | Voer stresstests uit om de uptime en fouttolerantie te evalueren. |
| NFE-002   | CN-001       | Gebruiksvriendelijkheid | Beheerdersinterface | Gebruikerstests om de gebruiksvriendelijkheid van de interface te beoordelen. |
| NFE-003   | CN-002       | Schaalbaarheid | Systeemarchitectuur | Test de prestaties bij een verhoogd aantal gebruikers en toegangspogingen. |
| NFE-004   | CN-002       | Compatibiliteit | Integratie met bestaande infrastructuur | Test de integratie met de huidige toegangscontrole systemen. |

Deze technische specificaties en traceability matrix bieden een gedetailleerd overzicht van de vereisten en de manier waarop ze zullen worden geïmplementeerd en getest binnen het Timed Anti-Passback systeem.
[---SPLIT-DOSSIER---]
{
    "cust_input": "\"Er is misbruik op de parking: medewerkers geven hun badge door. We hebben Timed Anti-Passback nodig op de slagbomen.\"",
    "cust_req": "# Customer Requirements Document (CRD)\n\n## Samenvatting\n\nDit document beschrijft de vereisten voor het implementeren van een Timed Anti-Passback systeem op de slagbomen van de parkeerfaciliteit. Het doel is om misbruik van toegangspassen door medewerkers te voorkomen, waarbij passen worden doorgegeven om meerdere voertuigen toegang te verlenen zonder toestemming.\n\n## Customer Needs\n\n**CN-001: Preventie van badge-misbruik**  \nDe klant heeft behoefte aan een systeem dat voorkomt dat medewerkers hun toegangspassen doorgeven aan anderen om meerdere voertuigen toegang te verlenen tot de parkeerfaciliteit.\n\n**CN-002: Verbeterde beveiliging van de parkeerfaciliteit**  \nHet systeem moet bijdragen aan de algehele beveiliging van de parkeerfaciliteit door ongeautoriseerde toegang te minimaliseren.\n\n## Functionele Eisen\n\n**FE-001: Implementatie van Timed Anti-Passback**  \nHet systeem moet een Timed Anti-Passback mechanisme bevatten dat voorkomt dat dezelfde badge binnen een bepaalde tijdsperiode opnieuw wordt gebruikt om toegang te verkrijgen.\n\n**FE-002: Configuratie van tijdsintervallen**  \nHet systeem moet de mogelijkheid bieden om de tijdsintervallen voor de Anti-Passback functionaliteit aan te passen, zodat deze kan worden afgestemd op de specifieke behoeften van de klant.\n\n**FE-003: Logregistratie van toegangspogingen**  \nHet systeem moet alle toegangspogingen registreren, inclusief succesvolle en geweigerde pogingen, om een audit trail te bieden voor beveiligingsdoeleinden.\n\n## Niet-functionele Eisen\n\n**NFE-001: Betrouwbaarheid**  \nHet systeem moet een hoge mate van betrouwbaarheid bieden, met minimale downtime, om ervoor te zorgen dat de parkeerfaciliteit continu beveiligd is.\n\n**NFE-002: Gebruiksvriendelijkheid**  \nDe interface voor het beheren van de Timed Anti-Passback instellingen moet gebruiksvriendelijk zijn, zodat beheerders eenvoudig aanpassingen kunnen maken zonder uitgebreide training.\n\n**NFE-003: Schaalbaarheid**  \nHet systeem moet schaalbaar zijn om toekomstige uitbreidingen van de parkeerfaciliteit of wijzigingen in het aantal gebruikers te kunnen ondersteunen.\n\n**NFE-004: Compatibiliteit**  \nHet systeem moet compatibel zijn met de bestaande toegangscontrole-infrastructuur van de parkeerfaciliteit om een naadloze integratie te garanderen.",
    "tech_req": "# Technische Specificaties voor Timed Anti-Passback Systeem\n\n## Integratie Details\n\n1. **Systeemarchitectuur**: Het systeem zal worden ge\u00efntegreerd met de bestaande toegangscontrole-infrastructuur van de parkeerfaciliteit. Dit omvat de slagbomen, badgelezers en het centrale toegangscontrolesysteem.\n   \n2. **Communicatieprotocol**: Het systeem zal gebruik maken van een standaard communicatieprotocol (bijv. TCP/IP) om gegevens tussen de badgelezers en het centrale systeem uit te wisselen.\n\n3. **Database**: Een centrale database zal worden gebruikt om loggegevens van toegangspogingen op te slaan. Deze database moet compatibel zijn met de bestaande IT-infrastructuur van de klant.\n\n## UI/UX Verwachtingen\n\n1. **Beheerdersinterface**: De interface moet intu\u00eftief en gebruiksvriendelijk zijn, met een dashboard dat een overzicht biedt van alle toegangspogingen en de status van het Anti-Passback systeem.\n\n2. **Configuratiepaneel**: Beheerders moeten eenvoudig tijdsintervallen kunnen instellen en wijzigen via een configuratiepaneel. Dit paneel moet duidelijke instructies en feedback geven bij het opslaan van wijzigingen.\n\n3. **Logboekweergave**: Er moet een functie zijn om logboeken te bekijken en te filteren op datum, tijd, badge-ID en type toegangspoging (succesvol of geweigerd).\n\n## Constraints\n\n1. **Compatibiliteit**: Het systeem moet compatibel zijn met de bestaande hardware en software van de parkeerfaciliteit zonder dat er grote aanpassingen nodig zijn.\n\n2. **Veiligheid**: Gegevensoverdracht tussen de componenten van het systeem moet beveiligd zijn om ongeautoriseerde toegang en gegevensmanipulatie te voorkomen.\n\n3. **Prestaties**: Het systeem moet snel reageren op toegangspogingen en binnen enkele seconden beslissingen kunnen nemen om wachttijden bij de slagbomen te minimaliseren.\n\n## Traceability Matrix\n\n| FR/NFR ID | Traces To CN | Description | Technische Architectuur Component | QA / Test Scenario |\n|-----------|--------------|-------------|-----------------------------------|--------------------|\n| FE-001    | CN-001       | Implementatie van Timed Anti-Passback | Toegangscontrole Software | Test of het systeem een badge binnen de ingestelde tijdsperiode blokkeert na gebruik. |\n| FE-002    | CN-001       | Configuratie van tijdsintervallen | Beheerdersinterface | Test de mogelijkheid om tijdsintervallen in te stellen en te wijzigen. |\n| FE-003    | CN-002       | Logregistratie van toegangspogingen | Centrale Database | Verifieer dat alle toegangspogingen correct worden gelogd en opgeslagen. |\n| NFE-001   | CN-002       | Betrouwbaarheid | Systeemarchitectuur | Voer stresstests uit om de uptime en fouttolerantie te evalueren. |\n| NFE-002   | CN-001       | Gebruiksvriendelijkheid | Beheerdersinterface | Gebruikerstests om de gebruiksvriendelijkheid van de interface te beoordelen. |\n| NFE-003   | CN-002       | Schaalbaarheid | Systeemarchitectuur | Test de prestaties bij een verhoogd aantal gebruikers en toegangspogingen. |\n| NFE-004   | CN-002       | Compatibiliteit | Integratie met bestaande infrastructuur | Test de integratie met de huidige toegangscontrole systemen. |\n\nDeze technische specificaties en traceability matrix bieden een gedetailleerd overzicht van de vereisten en de manier waarop ze zullen worden ge\u00efmplementeerd en getest binnen het Timed Anti-Passback systeem.",
    "sow_body": "# Statement of Work (SoW)\n\n**Datum:** 01-07-2026  \n**Status:** Draft / For Review\n\n## 1. Projectdoel\n\nHet doel van dit project is om een Timed Anti-Passback systeem te implementeren dat naadloos integreert met de bestaande toegangscontrole-infrastructuur van de parkeerfaciliteit. Dit systeem zal de beveiliging verbeteren door te voorkomen dat toegangspassen meerdere keren binnen een bepaalde tijdsperiode worden gebruikt.\n\n## 2. Project Scope\n\n### Functionele Vereisten (FR) en Acceptatiecriteria\n\n- **FR-001: Implementatie van Timed Anti-Passback**\n  - **Acceptatiecriteria:** Het systeem moet een badge binnen de ingestelde tijdsperiode blokkeren na gebruik.\n  \n- **FR-002: Configuratie van tijdsintervallen**\n  - **Acceptatiecriteria:** Beheerders moeten tijdsintervallen kunnen instellen en wijzigen via de beheerdersinterface.\n  \n- **FR-003: Logregistratie van toegangspogingen**\n  - **Acceptatiecriteria:** Alle toegangspogingen moeten correct worden gelogd en opgeslagen in de centrale database.\n\n### Niet-Functionele Vereisten (NFR)\n\n- **NFR-001: Betrouwbaarheid**\n  - **Acceptatiecriteria:** Het systeem moet een hoge uptime en fouttolerantie hebben, getest door stresstests.\n  \n- **NFR-002: Gebruiksvriendelijkheid**\n  - **Acceptatiecriteria:** De beheerdersinterface moet intu\u00eftief en gebruiksvriendelijk zijn, beoordeeld door gebruikerstests.\n  \n- **NFR-003: Schaalbaarheid**\n  - **Acceptatiecriteria:** Het systeem moet goed presteren bij een verhoogd aantal gebruikers en toegangspogingen.\n  \n- **NFR-004: Compatibiliteit**\n  - **Acceptatiecriteria:** Het systeem moet zonder grote aanpassingen integreren met de bestaande infrastructuur.\n\n## 3. Technische Scope & Integratiearchitectuur\n\nHet systeem zal worden ge\u00efntegreerd met de bestaande toegangscontrole-infrastructuur, inclusief slagbomen, badgelezers en het centrale toegangscontrolesysteem. Communicatie zal plaatsvinden via TCP/IP en er zal een centrale database worden gebruikt voor loggegevens. Het systeem moet compatibel zijn met de huidige IT-infrastructuur en voldoen aan strikte veiligheidsnormen om gegevensoverdracht te beveiligen.\n\n## 4. Deliverables\n\n- **D-001:** Volledig functionerend Timed Anti-Passback systeem\n- **D-002:** Beheerdersinterface met configuratiepaneel\n- **D-003:** Centrale database voor logregistratie\n- **D-004:** Integratie met bestaande toegangscontrole-infrastructuur\n- **D-005:** Documentatie van systeemarchitectuur en gebruikershandleiding\n- **D-006:** Testresultaten en acceptatierapporten\n\n## 5. Out of Scope\n\n- Hardware-upgrades van de bestaande toegangscontrole-infrastructuur\n- Training van personeel buiten de beheerdersinterface\n\n## 6. Rollen & Verantwoordelijkheden\n\n- **Projectmanager:** Verantwoordelijk voor de algehele projectco\u00f6rdinatie en communicatie.\n- **Technisch Lead:** Verantwoordelijk voor de technische implementatie en integratie.\n- **QA Specialist:** Verantwoordelijk voor het testen en valideren van systeemfunctionaliteit.\n- **Beheerder:** Verantwoordelijk voor het configureren en beheren van het systeem na implementatie.\n\n## 7. Planning & Mijlpalen\n\n| Mijlpaal                  | Datum       |\n|---------------------------|-------------|\n| Start van het project     | 01-08-2026  |\n| Voltooiing systeemontwerp | 15-09-2026  |\n| Voltooiing ontwikkeling   | 01-11-2026  |\n| Testfase afgerond         | 15-12-2026  |\n| Implementatie voltooid    | 01-01-2027  |\n| Projectafsluiting         | 15-01-2027  |\n\n## 8. Afhankelijkheden & Risico's\n\n- **Afhankelijkheden:** Beschikbaarheid van de huidige toegangscontrole-infrastructuur en IT-ondersteuning.\n- **Risico's:** Potenti\u00eble compatibiliteitsproblemen met bestaande systemen en vertragingen in de levering van benodigde hardware.\n\n## 9. Change Request Procedure\n\nAlle wijzigingen in de projectscope moeten schriftelijk worden aangevraagd en goedgekeurd door de projectmanager. Elke wijziging zal worden ge\u00ebvalueerd op impact op tijd, kosten en kwaliteit.\n\n## 10. Acceptatie & Sign-Off\n\nDe acceptatie van het project zal plaatsvinden na de succesvolle voltooiing van alle testscenario's en de goedkeuring van de projectdocumentatie door de klant. Sign-off zal worden verkregen van de projectmanager en de klantvertegenwoordiger.",
    "current_filepath": "outputs/generated_srs\\20260701_1512_er_is_misbruik_op_de_parking.md",
    "development_type": "1. Hardware Integrations SynApp/Con or extension with 3rd party device",
    "business_driver": "Requested in Official Tender",
    "is_customer_specific": "Customer Specific (Unique)",
    "verticals": [],
    "benchmark_competitor": "",
    "link_project": "",
    "link_product": "",
    "total_project_value": 0,
    "chargeable_value": 0,
    "potential_yearly_revenue": 0,
    "resolved_problem": "",
    "value_end_customer": "",
    "value_partner": "",
    "value_synguard": "",
    "current_situation": "",
    "overall_workflow": "",
    "desired_functionality": "",
    "integration_details": "",
    "ui_ux_expectations": "",
    "acceptance_criteria": "",
    "constraints_conditions": "",
    "tender_text": "",
    "matrix_data": [
        {
            "FR/NFR ID": "FE-001",
            "Traces To CN": "CN-001",
            "Description": "Implementatie van Timed Anti-Passback",
            "Technische Architectuur Component": "Toegangscontrole Software",
            "QA / Test Scenario (Acceptatiecriterium)": "Test of het systeem een badge binnen de ingestelde tijdsperiode blokkeert na gebruik."
        },
        {
            "FR/NFR ID": "FE-002",
            "Traces To CN": "CN-001",
            "Description": "Configuratie van tijdsintervallen",
            "Technische Architectuur Component": "Beheerdersinterface",
            "QA / Test Scenario (Acceptatiecriterium)": "Test de mogelijkheid om tijdsintervallen in te stellen en te wijzigen."
        },
        {
            "FR/NFR ID": "FE-003",
            "Traces To CN": "CN-002",
            "Description": "Logregistratie van toegangspogingen",
            "Technische Architectuur Component": "Centrale Database",
            "QA / Test Scenario (Acceptatiecriterium)": "Verifieer dat alle toegangspogingen correct worden gelogd en opgeslagen."
        },
        {
            "FR/NFR ID": "NFE-001",
            "Traces To CN": "CN-002",
            "Description": "Betrouwbaarheid",
            "Technische Architectuur Component": "Systeemarchitectuur",
            "QA / Test Scenario (Acceptatiecriterium)": "Voer stresstests uit om de uptime en fouttolerantie te evalueren."
        },
        {
            "FR/NFR ID": "NFE-002",
            "Traces To CN": "CN-001",
            "Description": "Gebruiksvriendelijkheid",
            "Technische Architectuur Component": "Beheerdersinterface",
            "QA / Test Scenario (Acceptatiecriterium)": "Gebruikerstests om de gebruiksvriendelijkheid van de interface te beoordelen."
        },
        {
            "FR/NFR ID": "NFE-003",
            "Traces To CN": "CN-002",
            "Description": "Schaalbaarheid",
            "Technische Architectuur Component": "Systeemarchitectuur",
            "QA / Test Scenario (Acceptatiecriterium)": "Test de prestaties bij een verhoogd aantal gebruikers en toegangspogingen."
        },
        {
            "FR/NFR ID": "NFE-004",
            "Traces To CN": "CN-002",
            "Description": "Compatibiliteit",
            "Technische Architectuur Component": "Integratie met bestaande infrastructuur",
            "QA / Test Scenario (Acceptatiecriterium)": "Test de integratie met de huidige toegangscontrole systemen."
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