# Tender Response — KK — Krav 5.3.5.3

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.5.3 |
| **Titel** | Genoptagelse af arbejde efter nedbrud |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast |
| **Genereret** | 2026-08-07 |

## Svar på krav 5.3.5.3

**Kundens krav:** Genoptagelse af arbejde efter nedbrud — Leverandøren bedes redegøre for, hvordan Systemet ved opstart efter et nedbrud føres tilbage i en tilstand med konsistente data og opsætning, så Brugerne oplever, at Systemet igen er funktionelt. Desuden skal der også redegøres for hvilke konkrete tekniske foranstaltninger der er implementeret for at opnå sammenhængende og ubrudte arbejdsprocesser, også efter afbrydelser.

**Leverandørens besvarelse:**

Systemet er designet til at sikre dataintegritet og genoptagelse på flere niveauer: infrastruktur og database, persistens af arbejdsgange og processer, samt beskyttelse af brugerens igangværende arbejde i klienter og dokumentredigering.

### Genoprettelse efter systemnedbrud

Ved opstart efter et nedbrud føres Systemet tilbage til en konsistent tilstand gennem en kombination af:

- **Transaktionel databehandling** — dataændringer i Systemets database (Microsoft SQL Server) håndteres transaktionsbaseret, så enten gennemføres en handling fuldt ud, eller den rulles tilbage. Det sikrer, at Systemet efter genstart ikke efterlades i en inkonsistent halv-gemt tilstand.
- **Backup og disaster recovery** — daglige sikkerhedskopier af database og filarkiv med geo-redundant lagring, Point-In-Time Recovery (35 dages historik for databaser) og soft delete for filer (35 dage). Genoprettelsesprocedurer testes regelmæssigt gennem planlagte øvelser.
- **Driftsarkitektur** — i cloud-leverancen (360° Online) hostes Systemet på Kubernetes med autoskalering, overvågning og automatisk genopretning af tjenester, så Brugerne oplever Systemet som funktionelt efter kortvarige infrastrukturafbrud.
- **Persistens af konfiguration** — Kundens opsætning (sagstyper, kodetabeller, arbejdsgange, integrationer m.m.) lagres i Systemets database og genindlæses konsistent ved opstart.

Efter et gennemført recovery kan Brugerne logge ind og fortsætte arbejdet med de sager, dokumenter og processer, der var i systemet på tidspunktet før nedbruddet — inden for rammerne af backup/restore-punktet.

### Sammenhængende arbejdsprocesser efter afbrydelser

Systemet implementerer flere foranstaltninger, så arbejdsprocesser kan genoptages efter afbrydelser:

| Mekanisme | Effekt |
|-----------|--------|
| **Persistente arbejdsgange** | Aktive dokumentarbejdsgange (fx review, godkendelse) og opgaver gemmes i Systemet og kan genoptages, når Brugeren vender tilbage |
| **Procesmotor** | Sagsprocesser (forløb/procesmodeller) bygges på et transaktionelt mønster, hvor processtatus og underliggende data opdateres atomart. Processer kan sættes i dvale (hibernate) og genoptages ved hændelser eller udløb af tidsperioder |
| **Integrationsjob** | Planlagte integrationsjob (fx 360° AutoSaver) kører med logging og kan genkøres ved fejl, så datafangst og automatisk registrering genoptages efter afbrydelser |
| **Tjek-ud/tjek-ind** | Dokumenter tjekkes ud til redigering og tjekkes ind igen; ved afbrydelse kan filer gendannes fra versionshistorik |
| **Kladde-status** | Dokumenter kan markeres som kladde, så igangværende arbejde tydeligt adskilles fra færdigbehandlet materiale |

Brugere kan desuden genoptage delvist færdiggjort sagsbehandling (fx aktindsigtsbehandling), hvor materiale er indhentet og behandlet, men sagen endnu ikke er endeligt afsendt.

### Autogem og beskyttelse af brugerinput

**Dokumentredigering (positivt vægtet — opfyldt):**
Når Brugeren redigerer dokumenter i Word via Systemet, gemmes indhold **automatisk løbende** (Word's indbyggede autogem). Når Word lukkes, tjekkes filen automatisk ind i Systemet. Dette beskytter mod datatab ved nedbrud eller utilsigtet lukning under dokumentarbejde (jf. også krav 5.2.8.11).

Ved samarbejde via Teams/SharePoint-integration gemmes ændringer automatisk og synkront i Systemet, inklusive versionering og historik.

**Metadataregistrering (præcisering):**
For registrering af sager, dokumenter og metadata anvender Systemet primært **eksplicit gemning** via Gem/Udfør. Brugeren får valideringsfeedback, hvis obligatoriske felter mangler, og data persisteres først ved bekræftet gemning. Det sikrer kontrolleret datakvalitet og undgår utilsigtede halvregistreringer.

Systemet understøtter **ikke generelt løbende autogem på alle skærmbilleder med mange inputrækker** (fx tabeller med medarbejderrækker) som en standardfunktion. Tilsvarende gælder for **paginering med særskilt gemning per side** — Systemet anvender paginering i lister og søgeresultater, men metadataregistrering gemmes som helhed ved eksplicit handling, ikke side for side.

### Yderligere tekniske foranstaltninger

- **Versionshistorik** — hver gang en fil åbnes til redigering, oprettes en ny version; Brugeren kan se, sammenligne og gendanne tidligere versioner
- **Logning og historik** — ændringer på sager, dokumenter, kontakter og projekter logges med tidsstempel og brugeridentitet
- **Fil-låsning** — ved tjek-ud vises lås i Systemet, Teams og SharePoint, så filer ikke redigeres to steder samtidig
- **Arkiveringsstatus** — tydelig visning af, om filer er gemt i Systemet eller fortsat under udarbejdelse (SharePoint-integration)
- **Fejlhåndtering ved gemning** — Systemet giver Brugeren feedback, hvis gemning fejler (fx pga. netværksafbrud eller manglende obligatoriske felter), så Brugeren ved, at data ikke er persisteret

### Tydelighed om gemt vs. ugemt data

Systemet gør det tydeligt for Brugeren, hvad der er gemt:

- **Filer:** versionshistorik viser hvem der har redigeret og hvornår; arkiveringsstatus viser gemt vs. under udarbejdelse
- **Objekter:** logvisning/historik på sager, dokumenter m.fl. viser ændringer med tidsstempel
- **Dokumenter:** kladde-status adskiller uafsluttet arbejde; journalført/afsluttet materiale låses mod yderligere redigering
- **Arbejdsgange:** aktive opgaver og arbejdsgange vises på Brugerens arbejdsliste/skrivebord, så igangværende processer er synlige efter genlogin

For metadata, der endnu ikke er eksplicit gemt, gælder det generelle princip, at data først er persisteret efter vellykket gemning — Brugeren informeres ved valideringsfejl, hvis gemning ikke kan gennemføres.

### Samlet effekt for Kunden

Kombinationen af transaktionel database, backup/DR, persistente arbejdsgange og dokumentautogem giver Kunden:

- **Høj dataintegritet** efter systemnedbrud
- **Genoptagelse af processer og opgaver** uden at starte forfra
- **Beskyttelse af dokumentarbejde** via autogem og versionshistorik
- **Sporbarhed** — tydelig historik for, hvad der er gemt og af hvem

## Evidence (intern)

| Claim | Kilde | Confidence |
|-------|--------|------------|
| DR/backup, PITR, datagenoprettelse efter nedbrud | RFP-udtræk (NND); Krav_2.24 | Verified |
| Word autosave ved dokumentredigering | Nationalbanken løsningsbeskrivelse; KK 5.2.8.11 | Verified |
| Versionshistorik med hvem/hvornår | Nationalbanken §2.9 | Verified |
| Arbejdsgange/processtatus persisteres (genoptagelse) | Wiki: Process support; Process Engine | Verified |
| Tjek-ud/ind + lås (Teams/SharePoint/360°) | Nationalbanken §8 | Verified |
| Kladde-status på dokumenter | KK 5.2.8.12 | Verified |
| Autogem på generelle metadataformularer (mange rækker) | — | Gap / ikke verificeret |
| Paginering med særskilt gem per side | — | Gap / ikke verificeret |

## Review-noter

- Terminologi: **review** og **godkendelse** (ikke gennemgang/godkjenning)
- Autogem på multi-row inputskærme: delvis — opfyldt for dokumentredigering; ikke generelt for metadataformularer
- Paginering med gem per side: gap — må ikke overclaims
