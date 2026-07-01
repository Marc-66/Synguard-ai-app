

# Page 1

STATEMENT OF WORK
E U R O F I B E R
V. 3.03 - 27/05/2026
A L W A Y S W I T H Y O U

# Page 2

C O N T E N T
1. Project Overzicht 4
2. Flow 5
2.1. WebService 5
2.2. Document scanner 6
2.3. Biostation enrollment 7
3. Scope 8
3.1. In scope 8
3.1.1. Webservice 8
3.1.2. Bezoekers 8
3.1.3. Companies 8
3.1.4. Bezoeken 9
3.1.5. Toegangsprofielen 9
3.1.6. Sleutelcode 9
3.1.7. Vrije veld 9
3.2. Out of scope 9
3.3. Document scanner visitor SelfService rule 10
3.4. Autoremove rule for documents 10
3.5. Visitor select rule 10
3.6. Biostation visitor SelfService rule 10
3.7. SIP call vanaf BioStation 11
4. Systeemvereisten 11
5. Aannames 11
6. Wijzigingsbeheer 11
7. Op te leveren resultaten 11
7.1. Webservices 11
7.2. SelfService – Document Scanner integratie 12
7.3. Autoremove mechanisme documenten 12
7.4. Visitor Select Rule 12
7.5. BioStation SelfService integratie 12
7.6. SIP Call integratie (BioStation) 12
8. Acceptatiecriteria 13
EUROFIBER - V. 3.03 - 27/05/2026 2 / 16

# Page 3

8.1. Webservice 13
8.2. SelfService – Document Scanner integratie 13
8.3. Autoremove mechanisme documenten 13
8.4. Visitor Select Rule 13
8.5. BioStation SelfService integratie 14
8.6. SIP Call integratie (BioStation) 14
9. Inschatting 14
10. Roles & Responsibilities 15
11. Aanvaarding 15
EUROFIBER - V. 3.03 - 27/05/2026 3 / 16

# Page 4

1. PROJECT OVERZICHT
Project Naam Eurofiber bezoeker en nieuwe kaarthouder flow
Eindklant Eurofiber
SOW Datum 23/05/2026
Geschatte project duur 34 werkdagen
Doel In deze ‘Statement of Work’ worden de scope, de te leveren prestaties, de
tijdschema’s en de verantwoordelijkheden voor het project tussen de
Opdrachtgever en Synguard vastgelegd.
Korte omschrijving Eurofiber wil een SelfRegistratie voor bezoekers, en voor nieuw
kaarthouders, op een kiosk waar via hun eID, paspoort of rijbewijs hun
identiteit gecontroleerd wordt. Deze personen worden in Synguard
toegevoegd via de applicatie PowerApp. Na deze controle moet er een
enrollment gebeuren voor gezichtsherkenning op een Biostation 3. Tijdens
deze aanmeldprocedure moeten er voor bezoekers 2 documenten
(Algemene voorwaarden en GDPR) ondertekend worden, voor nieuwe
kaarthouders komt er nog een document bij waarmee ze bevestigen dat ze
hun badge ontvangen hebben. Als er een fout optreedt moet er de
mogelijkheid zijn om een call te starten met de dispatch.
Omschrijving werk • Webservice zodat bezoekers en bezoeken kunnen aangemaakt
worden vanuit PowerApp naar Synguard. Er moet ook een
endpoint zijn om de huidige status van een bezoek op te vragen.
• Indien een flow onverwacht afgebroken wordt moet er verder
gegaan kunnen worden waar er gestopt is.
• Via een documentscanner moet een bezoeker zijn identiteit
verifiëren.
• Enrollment van de gezichtherkenning wordt gestart vanuit de
SelfService flow.
• Er moet via de Biostation contact opgenomen kunnen worden met
de dispatch.
EUROFIBER - V. 3.03 - 27/05/2026 4 / 16

# Page 5

2. FLOW
2.1. WebService
EUROFIBER - V. 3.03 - 27/05/2026 5 / 16

# Page 6

2.2. Document scanner
EUROFIBER - V. 3.03 - 27/05/2026 6 / 16

# Page 7

2.3. Biostation enrollment
EUROFIBER - V. 3.03 - 27/05/2026 7 / 16

# Page 8

3. SCOPE
3.1. In scope
3.1.1. Webservice
Om bezoekers en bezoeken te kunnen aanmaken vanuit PowerApp in Synguard is een uitbreiding nodig aan
de huidige webservice werking. Onderstaande calls worden aangemaakt zodat alle gewenste acties kunnen
uitgevoerd worden.
Endpoints:
• Create visitor
• Update Visitor
• Get all visitors
• Delete visitor
• Create visit
• Update visit
• Get all visits
• Delete visit
• Get visit status
• Get companies
• Get Access profiles
3.1.2. Bezoekers
Er moet gecontroleerd kunnen worden of een bepaalde bezoeker al bestaat in het systeem. Als dit geval is
moet deze bezoeker geüpdatet kunnen worden. In het andere geval moet er een nieuwe bezoeker
aangemaakt worden. Als identifier wordt hiervoor het veld EmployeeCode gebruikt. Onderstaande velden
worden meegestuurd met een bezoeker:
• Voornaam
• Achternaam
• employeeCode
• E-mailadres
• Geboortedatum
• Company-ID
3.1.3. Companies
Om te kunnen werken met een koppeling met de Companies moeten hiervoor CRUD voorzien worden.
Onderstaande velden zijn daarvoor noodzakelijk:
• Company-ID
• Description
EUROFIBER - V. 3.03 - 27/05/2026 8 / 16

# Page 9

3.1.4. Bezoeken
Een bezoek moet toegevoegd kunnen worden aan een bezoeker of meegestuurd met een nieuwe bezoeker.
Deze bezoeken moeten opgevraagd kunnen worden, verwijderd en aangepast. Onderstaande velden worden
hiervoor gebruikt:
• Datum
• Starttijd
• Stoptijd
3.1.5. Toegangsprofielen
Standaard moet er een toegangsprofiel toegevoegd worden aan een bezoeker met beperkte rechten. Nadien
moet hier een ander toegangsprofiel aan gekoppeld kunnen worden. Deze profielen kunnen uit Synguard
opgehaald worden. Onderstaande velden zijn hiervoor nodig:
• AccessProfileID
• Startdate
• Stopdate
3.1.6. Sleutelcode
Vanuit PowerApp kan er een sleutelcode naar Synguard gestuurd worden waarmee de inkom deur geopend
wordt en waarmee de identificatie op de SelfService gestart kan worden. Deze sleutelcode wordt gekoppeld
aan een bezoeker met onderstaande velden:
• Sleutelcode
• startDate
• stopDate
• startTime
• stopTime
• Valid
3.1.7. Vrije veld
Er is een vrij veld dat zorgt voor de identificatie van een nieuwe kaarthouder ten opzichte van een bezoeker.
Als dit veld actief is zal de bezoeker gezien worden als een nieuwe kaarthouder en hierdoor een iets andere
flow krijgen.
• New badge user – Freefield_xxx
3.2. Out of scope
• PowerApp ontwikkelingen
• Hardware- en netwerkbeheer
EUROFIBER - V. 3.03 - 27/05/2026 9 / 16

# Page 10

3.3. Document scanner visitor SelfService rule
Om deze regel te kunnen uitvoeren is er een Windows PC (NUC) nodig waarmee de Adaptive Recognition
Osmond R scanner via USB verbonden is. Op deze pc draait de software van Adaptive Recognition en
SynReg van Synguard. Deze PC wordt door de klant voorzien. De installatie, configuratie en ondersteuning
van deze PC vallen buiten de scope van dit project.
. Er moet één PC per documentscanner beschikbaar zijn om een correcte en stabiele werking te garanderen.
Door op een knop te klikken in de SelfService kiosk wordt de Adaptive Recognition Osmond R scanner
geactiveerd. Op het scherm verschijnt een melding om een document op de scanner te plaatsen. Na het
inscannen van dit document worden onderstaande testen uitgevoerd:
• Is het een geldig document (Eid, paspoort, rijbewijs)
• Is de data geldig (niet vervallen)
• Is de ingelezen persoon de persoon die probeert aan te melden
Als één van deze testen ongeldig is zal er een foto van het document opgeslagen worden bij de aangemelde
persoon. Deze zal opgeslagen worden bij de “documenten” van de aangemelde bezoeker. Er verschijnt op
de kiosk ook een scherm met instructies over hoe de dispatch bereikt kan worden.
3.4. Autoremove rule for documents
Als er tijdens het document scanner proces een fout opgetreden is wordt een foto van het gescande
document opgeslagen bij de bezoeker. Dit document mag echter maar 10 minuten bewaard worden. Er
wordt een job / regel voorzien worden die dit document gaat verwijderen.
3.5. Visitor select rule
Na het inscannen van een document moet er gecheckt worden aan de hand van achternaam en
geboortedatum of dit de aangemelde bezoeker is. Indien deze bezoeker gevonden wordt moeten volgende
acties op zijn naam gebeuren. In het andere geval moet er een foutmelding getoond worden.
3.6. Biostation visitor SelfService rule
Om deze regel te kunnen uitvoeren is er een Windows PC (NUC of VM) nodig waarop een SynAppWindows
geïnstalleerd is. Deze pc wordt door de klant voorzien. Op één pc (SynAppWindows) kunnen meerdere (+/-
10) BioStations gekoppeld worden.
Via de SelfService moet het mogelijk zijn om het enrollment proces op de Biostation te starten. Indien hier
een fout optreedt moet er een scherm met instructies op de kiosk komen over hoe de dispatch te bereiken is.
Als het enrollment gelukt is moet er verder gegaan worden met de flow.
EUROFIBER - V. 3.03 - 27/05/2026 10 / 16

# Page 11

3.7. SIP call vanaf BioStation
Op de BioStation is gedurende het volledige proces een knop zichtbaar waarmee de gebruiker een call kan
initiëren met de dispatch.
Er werd onderzocht of het mogelijk is om een SIP call op de BioStation te starten vanuit de SelfService kiosk.
Dit blijkt echter technisch niet haalbaar, aangezien de BioStation geen API-endpoints voorziet om externe
triggers te ondersteunen.
Een alternatieve oplossing via de SIP-centrale werd overwogen, maar deze brengt bijkomende complexiteit
en onzekerheden met zich mee op vlak van implementatie en betrouwbaarheid.
Daarom wordt gekozen voor een oplossing waarbij de call-knop continu beschikbaar is op de BioStation
tijdens de volledige flow. Indien er tijdens de flow een probleem optreedt op de kiosk worden hier duidelijk
instructies getoond hoe een call gestart kan worden op de BioStation. Deze aanpak garandeert een stabiele
werking en heeft geen negatieve impact op de gebruiksvriendelijkheid.
4. SYSTEEMVEREISTEN
NUC voor installatie SynReg of SynApp Windows:
• Windows 11
• Intel Core i5 (of hoger)
• 4 GB RAM geheugen
• 128 GB SSD HD
5. AANNAMES
• Biostation is compatibel met 8x8 SIP centrale
• Firmware van de Adaptive Recognition Osmond scanner is stabiel
• Alle apparaten zitten op hetzelfde netwerk
• Computers of virtuele machines worden voorzien door de klant.
6. WIJZIGINGSBEHEER
Wijzigingen worden beheerd via:
• Change requests
• Impactanalyse (tijd/kosten/scope)
• Goedkeuring door Product Owner
7. OP TE LEVEREN RESULTATEN
7.1. Webservices
• Implementatie van volgende endpoints:
o Create Visitor
o Update Visitor
o Get All Visitors
o Delete Visitor
o Create Visit
o Update Visit
o Get All Visits
o Delete Visit
o Get Visit Status
EUROFIBER - V. 3.03 - 27/05/2026 11 / 16

# Page 12

o Get Companies
o Get Access Profiles
• API-documentatie (Swagger)
• Authenticatie & security configuratie
• Error handling & logging
7.2. SelfService – Document Scanner integratie
• Integratie met Adaptive Recognition Osmond scanner
• UI flow op kiosk
• Validaties:
o Document type (EID / paspoort / rijbewijs)
o Geldigheid document
o Identiteitscontrole persoon
• Opslaan foto document bij fout
• Kioskmelding met dispatch instructies
7.3. Autoremove mechanisme documenten
• Background job / scheduled task
• Automatische verwijdering na 10 minuten
• Logging van verwijderacties
7.4. Visitor Select Rule
• Matching logica (Achternaam + Geboortedatum)
• Trigger acties bij succesvolle match
• Foutafhandeling + melding bij mismatch
7.5. BioStation SelfService integratie
Om deze regel te kunnen uitvoeren is er een Windows PC (NUC) nodig waarmee de Adaptive Recognition
Osmond R scanner via USB verbonden is. Op deze pc draait de software van Adaptive Recognition en
SynReg van Synguard. Deze pc wordt door de klant voorzien.
• Start enrollment proces via kiosk
• Flow management (success/failure)
• Fallback scherm met instructies
7.6. SIP Call integratie (BioStation)
• SIP call functionaliteit vanuit BioStation
• UI knop op de BioStation beschikbaar tijdens hele flow
• Integratie met dispatch systeem
EUROFIBER - V. 3.03 - 27/05/2026 12 / 16

# Page 13

8. ACCEPTATIECRITERIA
8.1. Webservice
• Alle endpoints zijn beschikbaar en toegankelijk via de afgesproken base URL
• Elke endpoint geeft correcte HTTP statuscodes terug.
• CRUD-operaties werken end-to-end correct (create → retrieve → update → delete)
• Swagger documentatie is beschikbaar
• Alle endpoints, parameters en responses zijn correct beschreven
• Voorbeeldrequests en responses zijn aanwezig
• API is enkel toegankelijk met geldige authenticatie
• Ongeautoriseerde requests worden geweigerd
• Fouten worden op consistente manier teruggegeven
• Alle errors worden gelogd met timestamp en context
• Logs zijn raadpleegbaar
8.2. SelfService – Document Scanner integratie
• Scanner activeert vanuit kiosk UI zonder fouten
• Scanproces start en stopt correct
• System valideert correct:
o Documenttype (eID / paspoort / rijbewijs)
o Document vervaldatum
o Identiteitsmatch
• Ongeldige documenten worden correct afgewezen
• Bij fout:
o Documentfoto wordt opgeslagen
o Kiosk toont duidelijke foutmelding
o Gebruiker krijgt instructies voor dispatch
• Gebruiker kan de flow volledig doorlopen zonder blokkades
• Flow hervat correct na onderbreking
8.3. Autoremove mechanisme documenten
• Background job draait automatisch zonder manuele interventie
• Documenten die ouder zijn dan 10 minuten worden verwijderd
• Documenten jonger dan 10 minuten blijven beschikbaar
• Verwijderacties worden correct gelogd (timestamp + ID)
• Geen impact op andere systemen of performance
8.4. Visitor Select Rule
• Er wordt gematched op achternaam en geboortedatum
• Correcte acties worden getriggerd (flow gaat verder)
• Bij mismatch:
o Correcte foutmelding wordt getoond
o Geen verdere flow acties worden uitgevoerd
o Dispatch optie wordt aangeboden
EUROFIBER - V. 3.03 - 27/05/2026 13 / 16

# Page 14

8.5. BioStation SelfService integratie
• Enrollment kan gestart worden vanuit kiosk
• BioStation reageert binnen acceptabele tijd (<5 sec start)
• Bij succes:
o Enrollment status wordt correct opgeslagen
o Flow gaat verder
• Bij fout:
o Fallback scherm met instructies verschijnt
o Gebruiker kan dispatch contacteren
8.6. SIP Call integratie (BioStation)
• Gebruiker kan op elk moment in de flow een call starten
• SIP call wordt succesvol opgezet met dispatch
• Connectie met dispatch systeem werkt stabiel
9. INSCHATTING
Categorie Item Inschatting (dagen)
Visitor v2.0 Webservice Create Visitor endpoint 0.5
Update Visitor endpoint 0.5
Get All Visitors endpoint 0.5
Delete Visitor endpoint 0.5
Create Visit endpoint 0.5
Update Visit endpoint 0.5
Get All Visits endpoint 0.5
Delete Visit endpoint 0.5
Get Visit Status endpoint 0.5
Get Companies endpoint 0.5
Get Access Profiles endpoint 0.5
Bezoekersregistratie Biostation Visitor Selfservice rule 10
Document Scanner Visitor 5
Selfservice rule
Auto remove date rule voor 0.5
documenten
Visitor check/select rule 3
Software Development 24
Overhead (analyse, testing,…) 10
TOTAAL 34
EUROFIBER - V. 3.03 - 27/05/2026 14 / 16

# Page 15

10. ROLES & RESPONSIBILITIES
Rol Verantwoordelijkheid
Product Owner Backlog, prioriteiten
Chief Technology Officer Proces & team support
Dev Team Design, build, test
Stakeholders Feedback & acceptatie
PowerApp integratie Eurofiber
Hardware- en beheer Eurofiber
11. AANVAARDING
Door hieronder te ondertekenen, gaan beide partijen akkoord met deze opdrachtomschrijving.
Beringen, 23/05/2026
Synguard NV Eurofiber
(handtekening) (handtekening)
Rechtsgeldig vertegenwoordigd door Rechtsgeldig vertegenwoordigd door
(Naam en functie) (Naam en functie)
EUROFIBER - V. 3.03 - 27/05/2026 15 / 16

# Page 16

VERSIEGESCHIEDENIS
Versie Datum Verantwoordelijke Aanpassing
3.01 23/05/2026 HAVTO Aanmaken document
3.02 26/05/2026 HAVTO Toevoegen pc’s
3.03 27/05/2026 HAVTO Aanpassen scherm BioStation
EUROFIBER - V. 3.03 - 27/05/2026 16 / 16