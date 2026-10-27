# Tender Response — KK — Krav 5.3.3.1.1

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.3.1.1 |
| **Titel** | Datakvalitet og -integritet i Systemet |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast |
| **Genereret** | 2026-08-06 |

## Svar på krav 5.3.3.1.1

**Kundens krav:** Datakvalitet og -integritet i Systemet — Leverandøren bedes redegøre for, hvordan dataintegritet og høj datakvalitet sikres i Systemet.

**Leverandørens besvarelse:**

Systemet sikrer dataintegritet og høj datakvalitet gennem en kombination af en robust datamodel, konfigurerbare registreringsregler, standardiserede værdilister og integrationer mod eksterne registre, hvor det er relevant. Kvalitetssikring sker både på databaselaget, i applikationslogikken og i brugergrænsefladen ved registrering og vedligehold.

### Datamodel og dataintegritet i databasen

Systemet er bygget på en relationel databasemodel i Microsoft SQL Server. Centrale objekter (sager, dokumenter, kontakter, ejendomme m.fl.) identificeres med unikke nøgler, og data hænger sammen via definerede relationer mellem entiteter. Databaseændringer følger etablerede udviklings- og review-retningslinjer, herunder håndtering af constraints som del af standard databasepraksis. Dette understøtter dataintegritet, konsistens og sporbarhed gennem hele produktets livscyklus.

### Foruddefinerede værdilister (kodetabeller)

Systemet anvender kodetabeller (værdilister) til en lang række centrale metadatafelter, herunder bl.a. sagstype, dokumentkategori, journalstatus, tilgangskode/klassifikation og adgangskoder. Kodetabellerne administreres af Kundens administratorer i Administratormodulet og anvendes som dropdown-felter ved registrering, søgning og filtrering.

Det sikrer ensartet terminologi, reducerer frie tekstindtastninger og forbedrer datakvalitet og gjenfinding. Kodetabeller kan tilpasses Kundens behov uden programmering, og ændringer kan logges som del af konfigurationsstyringen.

### Obligatoriske felter

Systemet understøtter obligatoriske felter på flere niveauer:

- **Systemdefinerede obligatoriske felter** — visse kernefelter kan ikke fjernes, fx adgangsgruppe, titel, oprettelsesdato og objektstatus, for at understøtte ESDH-principper og sikkerhedsmodel.
- **Kundekonfigurerede obligatoriske felter** — administrator kan markere felter som obligatoriske på sager, dokumenter og øvrige objekttyper (aktiviteter, kontakter, ejendomme, projekter).

Felter markeret som obligatoriske skal udfyldes, før registrering kan gennemføres; brugeren gøres opmærksom på manglende værdier ved forsøg på gem/udfør. Dette gælder også i oprettelsesdialoger, fx ved journalisering fra Outlook.

### Forretningsregler og forebyggelse af konfliktende data

Systemet understøtter konfigurerbare forretningsregler og feltlogik, som begrænser fejlregistrering og inkonsistente data:

- **Kontekstafhængige registreringer** — værdier i ét felt kan automatisk udfylde, skjule, låse eller gøre andre felter obligatoriske.
- **Vejvisere og registreringsskærme** — administrator kan bygge procesnære registreringsbilleder med sektioner, standardværdier, hjelpetekster og feltafhængigheder (dra-og-slip med forhåndsvisning).
- **Proces- og statusregler** — dokumentkategorier kan knyttes til dokumenttype med regler for ekspedering, opfølgning og arkivhåndtering; journalstatus og tilgangsregler styres via kodetabeller med rollebinding.

Når betingelser i et triggerfelt er opfyldt, kan handlinger som *Vis*, *Skjul*, *Sæt obligatorisk*, *Angiv værdi* og *Sæt skrivebeskyttet* udløses på målfelter. Det gør det muligt at sikre, at brugeren kun kan registrere kombinationer af metadata, der er i overensstemmelse med Kundens forretningsregler.

Leverandøren udvikler desuden et rammeverk for forretningsregler (Business Rules Engine), som på sigt vil udvide muligheden for regelstyret automatisering uden custom udvikling, når funktionaliteten gøres tilgængelig i Systemet.

### Validering mod eksterne registre og klassifikationer

Hvor det er relevant, kan Systemet validere og berige data mod eksterne registre og autoritative kilder, herunder:

- **Grunddata via Datafordeleren** — i KK-konteksten omfatter det bl.a. CPR, CVR, BBR, ejerfortegnelse, matriklen, ejendomsbeliggenhed, DAR, danske stednavne og ejendomsvurderinger (jf. krav 5.3.8.2.2.1 og B1-03).
- **Person- og adressedata** — ved kontaktoprettelse kan oplysninger hentes/valideres mod Folkeregisteret, og kontakter knyttes til sager og dokumenter i korrekt kontekst.
- **Ejendomsdata** — standardobjektet Ejendom understøtter matrikelrelaterede felter og integration mod matrikelregister.
- **Klassifikationer** — standardiserede klassifikations- og tilgangskodefelter (inkl. NOARK-relaterede værdilister) sikrer ensartet klassificering på tværs af sager og dokumenter.

Integrationsdata anvendes til at sikre korrekt og opdateret registrering frem for manuel indtastning, hvilket direkte understøtter datakvalitet og dataintegritet.

### Samlet effekt for Kunden

Denne helhedstilgang giver Kunden:

- **Højere datakvalitet** ved registrering — vejledte skemaer, værdilister og obligatoriske felter
- **Færre fejl og konflikter** — feltlogik og forretningsregler forhindrer inkonsistente kombinationer
- **Bedre sporbarhed** — relationel datamodel, entydige nøgler og autoritative datakilder
- **Løbende forbedring uden leverandør** — administrator kan tilpasse datamodel, værdilister og registreringsregler i Administratormodulet

## Evidence (intern)

| Claim | Kilde | Confidence |
|-------|--------|------------|
| Kodetabeller/værdilister | Ratatoskr: Code tables | Verified |
| Obligatoriske felter + validering | Nationalbanken løsningsbeskrivelse; KUM-SLKS kravspec | Verified |
| Kontekstafhængige feltregler | NND kravtabell; KUM-SLKS kravspec | Verified |
| Validering mod eksterne registre | NND kravtabell; KK krav 5.3.8.2.2.1 / B1-03 | Verified |
| Relationel SQL Server-database | Wiki: Public 360° Database | Verified |
| BRE | RFP-udtræk (NND) | Lead — når tilgængelig |
