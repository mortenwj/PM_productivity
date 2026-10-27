# Tender Response — KK — Krav 5.3.7.2

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.7.2 |
| **Titel** | Privacy by design |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast (efter review) |
| **Genereret** | 2026-08-13 |

## Svar på krav 5.3.7.2

**Kundens krav:** Privacy by design — Leverandøren bedes, ved brug af konkrete eksempler, redegøre for hvilke foranstaltninger der anvendes og hvordan disse benyttes for at Systemet efterlever privacy-by-design-princippet.

**Leverandørens besvarelse:**

Privacy by design er indbygget i Systemets arkitektur, konfiguration og livscyklus. Databeskyttelse er indtænkt fra planlægning og design over udvikling og test til drift og vedligehold — i overensstemmelse med GDPR og Leverandørens etablerede rammeværk for databeskyttelse (Privacy Engineering Framework og obligatoriske Privacy Risk Assessments).

Systemet understøtter, at Kunden som dataansvarlig bestemmer, hvilke personoplysninger der registreres, hvem der har adgang, hvor længe data opbevares, og hvornår data slettes eller anonymiseres. Leverandøren sikrer de tekniske og organisatoriske forudsætninger for dette.

### Privacy by design i praksis

| Fase | Foranstaltning |
|------|----------------|
| **Planlægning og design** | Vurdering af art, formål og omfang af personoplysninger; dataminimering og formålsbegrænsning indtænkes i datamodel og adgangsdesign |
| **Udvikling og test** | Sikker udviklingspraksis; test- og demomiljøer benyttes med fiktive eller anonymiserede data — ikke reelle personoplysninger |
| **Risikovurdering** | Obligatoriske Privacy Risk Assessments (PRA) før release; årlig opfølgning og ekstern revision (ISAE 3000) |
| **Drift** | Tenant-isolation, kryptering, adgangsstyring, logning og livscyklusstyring for data |

### Anonymisering og pseudonymisering

Systemet understøtter anonymisering og pseudonymisering, hvor det er relevant for Kundens sagsbehandling og offentlighedslovgivning:

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **360° Archive Inspector** | Modul til automatiseret detektion af personoplysninger og følsomme oplysninger i tekst og metadata. Understøtter registrering, arkivering, offentliggørelse og kvalitetssikring ved at identificere, markere og screene data direkte i brugergrænsefladen. Modulet er i drift i det norske marked og tilpasses i øjeblikket til det danske marked |
| **Overstregning (Redaction)** | I arkivadministration kan metadata anonymiseres eller skjules på tværs af mange poster — fx erstattes sagstitler og kontaktnavne med "Redacted", mens sagen bevares. Udføres via skabeloner og batch-job af autoriserede Brugere |
| **Overstregning i filvisning** | I 360° File Viewer kan følsomme oplysninger i dokumenter overstreges, så de ikke fremgår i den version, der deles eller offentliggøres |
| **Anonymisering i svar på aktindsigtsanmodninger** | Ved besvarelse af aktindsigtsanmodninger (360° Information Act Request) kan filtitler anonymiseres, så svardokumentet viser relationsbetegnelse i stedet for fuld titel — konfigurerbart via indstillingen *Anonymize file titles on IFAR Response letter* |
| **Pseudonymisering i praksis** | Ved anonymisering af filtitler i svardokumenter erstattes læsbare titler med dokumentnummer/sekvens/relationsformat, så indholdet kan håndteres internt uden unødig eksponering af følsomme betegnelser |

**Eksempel:** Et uregistreret dokument modtages via integration. Archive Inspector markerer personoplysninger i indhold og metadata, så sagsbehandleren kan vurdere afskærmning, før dokumentet registreres og evt. offentliggøres. Ved en aktindsigtsanmodning overstreger sagsbehandleren CPR-numre i PDF'en via File Viewer og anonymiserer filtitler i svarbrevet — kun den nødvendige version udleveres.

### Dataminimering

Dataminimering sikrer, at Systemet kun indeholder og behandler de personoplysninger, der er nødvendige for Kundens formål:

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Need-to-know-adgang** | Rettighedsmatrix, adgangsgrupper og tilgangskoder sikrer, at Brugere kun ser personoplysninger, de har tjenstligt behov for |
| **Konfigurerbar datamodel** | Kunden konfigurerer, hvilke felter der er obligatoriske, og hvilke integrationer der henter data fra eksterne registre — kun relevante oplysninger indsamles |
| **Integrationsfiltrering** | Via SIF og AuthProxy kan data filtreres og begrænses per integration, så kun nødvendige oplysninger udveksles |
| **Proaktiv identifikation af følsomme data** | Archive Inspector understøtter dataminimering ved at afsløre personoplysninger tidligt i registreringsprocessen, så unødig eksponering kan undgås |
| **Begrænsning af opbevaring** | Bevaringskoder og kassationsregler knyttes til klassifikation/arkivnøgle; bevaringstid beregnes automatisk ved sagsafslutning. Dokumenter og filer arver som standard sagens kassationsdata |
| **Regelstyret sletning** | Kassation og permanent sletning initieres af autoriserede Brugere efter review og godkendelse ("man-in-the-loop"); Systemet sletter ikke automatisk uden at opfyldte kriterier og nødvendig godkendelse er på plads |
| **Soft delete og gendannelse** | Midlertidig sletning og soft delete (35 dage for filer) giver kontrolleret håndtering uden unødig permanent opbevaring |

**Eksempel:** En sag klassificeres med en arkivnøgle, der har foruddefineret bevaringstid. Ved sagsafslutning beregnes kassationsdato automatisk. Når perioden udløber, gennemgår en autoriseret administrator en rapport og godkender sletning — data opbevares ikke længere end nødvendigt.

### Kryptering

Kryptering beskytter personoplysninger mod uautoriseret adgang (jf. krav 5.3.7.1):

| Lag | Foranstaltning |
|-----|----------------|
| **I transit** | TLS 1.2+ mellem klient, Systemet og integrationer |
| **I hvile** | AES-256 for database og filarkiv; nøgler i Azure Key Vault |
| **Backup** | Krypterede sikkerhedskopier med adskilt nøgleforvaltning |

**Eksempel:** Personoplysninger i en kontaktregistrering og tilknyttede dokumenter er krypteret i hvile og kun tilgængelige for autoriserede Brugere via krypteret forbindelse.

### Information Lifecycle Management (ILM)

Systemet understøtter styring af personoplysningers livscyklus fra oprettelse til sletning eller arkivering:

| ILM-fase | Funktionalitet i Systemet |
|----------|---------------------------|
| **Oprettelse/registrering** | Kontrolleret registrering med validering, obligatoriske felter og adgangskoder; Archive Inspector kan gennemgå uregistrerede dokumenter som del af registreringsflowet |
| **Aktiv brug** | Adgangsstyring, audit trail, versionshistorik og journalføringslåsning |
| **Screening og kvalitet** | Archive Inspector til detektion af personoplysninger; overstregning af følsomme oplysninger før offentliggørelse eller udlevering |
| **Opbevaring og kassation** | Bevaringskoder, kassationsdatoer, masseopdatering og rapporter over kommende/udførte kassationer |
| **Sletning** | Midlertidig sletning, permanent sletning af filer og fuld sletning af metadata — med kassationslog og revisionsspor |
| **Kontraktophør** | Sletning eller returnering af personoplysninger efter Kundens valg ved kontraktophør (jf. databehandleraftale) |

**Eksempel:** En kontakt oprettes i en sag, gennemgås for følsomme oplysninger via Archive Inspector ved registrering, behandles i en arbejdsgang med fuld logning, klassificeres med bevaringstid ved afslutning, og slettes efter udløb af kassationsperiode med dokumenteret historik i kassationsloggen.

### Organisatoriske foranstaltninger

Ud over produktfunktioner understøtter Leverandøren privacy by design og databeskyttelse gennem:

- ISO 27001-certificering og GDPR-alignment i design og drift
- Obligatoriske Privacy Risk Assessments for produktændringer
- Testmiljøer uden reelle personoplysninger
- Dokumenterede rutiner for hændelseshåndtering og varsling til Kunden ved persondatasikkerhedsbrud

Privacy-by-design-principperne er således indtænkt i hele Systemets livscyklus — fra arkitektur og udvikling over konfiguration og drift til sletning og kontraktophør.
