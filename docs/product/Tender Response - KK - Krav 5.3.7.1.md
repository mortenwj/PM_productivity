# Tender Response — KK — Krav 5.3.7.1

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.7.1 |
| **Titel** | CIA — Fortrolighed, integritet og tilgængelighed |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast (efter review) |
| **Genereret** | 2026-08-10 |

## Svar på krav 5.3.7.1

**Kundens krav:** Leverandøren bedes redegøre for, hvordan de klassiske tre sikkerhedsegenskaber (CIA) opfyldes i Systemet: Confidentiality (fortrolighed af data), Integrity (integritet/korrekthed af data) og Availability (tilgængelighed af data og funktionalitet). Leverandøren bedes anvende konkrete eksempler på, hvordan principperne er tænkt ind i løsningen.

**Leverandørens besvarelse:**

Systemets sikkerhedsarkitektur er designet med CIA-triaden som grundprincip. Fortrolighed, integritet og tilgængelighed adresseres gennem en kombination af tekniske kontroller i produktet, sikker drift af platformen og etablerede processer for overvågning, test og forbedring — i overensstemmelse med anerkendte rammeværker som ISO 27001 og CIS Controls.

### Confidentiality — Fortrolighed af data

Fortrolighed sikrer, at data kun er tilgængelige for autoriserede brugere og systemer.

**Konkrete eksempler i Systemet:**

| Kontrol | Eksempel i praksis |
|---------|-------------------|
| **Kryptering i transit** | Al kommunikation mellem Brugerens browser/klient og Systemet samt mellem Systemet og integrationer sker med TLS 1.2 eller nyere |
| **Kryptering i hvile** | Database og filarkiv krypteres med AES-256; nøgler forvaltes i Azure Key Vault med audit trail og nøglerotation |
| **Adgangsstyring** | Tilgang til sager og dokumenter styres via rettighedsmatrix, adgangsgrupper og radtilladelser — Brugere ser kun det, de er eksplicit tildelt |
| **Klassifikation** | Tilgangskoder og adgangskoder (fx offentlig/begrænset offentlighed) styrer, hvem der kan se og behandle dokumenter og sager |
| **Identitetsstyring** | Integration med Kundens Entra ID med understøttelse af Single Sign-On og multifaktorautentifikation (MFA) |
| **Tenant-isolation** | Hver Kunde har isoleret database, filcontainer og applikationskontekst, så data ikke deles mellem kunder |
| **API-sikkerhed** | AuthProxy og SIF sikrer autentificering og autorisation ved integrationskald; data kan filtreres per integration |

**Eksempel:** En sagsbehandler i en adgangsgruppe ser kun sager og dokumenter inden for sin tildelte adgangskontekst. Et dokument med tilgangskode "Fortroligt" er kun synligt for Brugere med den nødvendige adgang — uanset om de søger bredt i Systemet.

### Integrity — Integritet (korrekthed) af data

Integritet sikrer, at data er korrekte, fuldstændige og beskyttet mod uautoriserede ændringer.

**Konkrete eksempler i Systemet:**

| Kontrol | Eksempel i praksis |
|---------|-------------------|
| **Transaktionel databehandling** | Databaseændringer gennemføres atomart — enten gemmes en handling fuldt ud, eller den rulles tilbage |
| **Audit trail** | Alle læsninger, redigeringer og ændringer på sager og dokumenter logges med brugeridentitet og tidsstempel |
| **Admin-audit** | Konfigurationsændringer (kodetabeller, adgangsgrupper, integrationer) logges i administrator-modulet |
| **Versionshistorik** | Filændringer gemmes som versioner; Brugeren kan se, sammenligne og gendanne tidligere versioner |
| **Validering og constraints** | Obligatoriske felter, kodetabeller og forretningsregler forhindrer inkonsistent eller ufuldstændig registrering (jf. krav 5.3.3.1.1) |
| **Journalføringslåsning** | Når dokumenter afsluttes/journaliseres, låses metadata mod uautoriserede ændringer |
| **Immutable backup** | Sikkerhedskopier lagres immutable, så backup-data ikke kan manipuleres |
| **Sikker udvikling** | OWASP ZAP i release-pipeline, kode-review og årlige penetratonstests af uafhængigt sikkerhedsselskab |

**Eksempel:** Når et dokument sendes til review og godkendelse, logges hver handling i arbejdsgangens historik. Efter godkendelse og journalføring kan metadata ikke ændres uden korrekt adgang — og alle tidligere versioner af filen bevares i versionshistorikken.

### Availability — Tilgængelighed af data og funktionalitet

Tilgængelighed sikrer, at Systemet og data er tilgængelige, når autoriserede Brugere har behov for dem.

**Konkrete eksempler i Systemet:**

| Kontrol | Eksempel i praksis |
|---------|-------------------|
| **Geo-redundant lagring** | Data lagres med redundans på tværs af datacentre |
| **Backup og gendannelse** | Daglige sikkerhedskopier af database og filarkiv; Point-In-Time Recovery (35 dages historik); soft delete for filer (35 dage) |
| **Disaster recovery** | Dokumenterede DR-procedurer testes regelmæssigt gennem planlagte øvelser; RTO ved fuld disaster recovery er 12 timer per tenant |
| **Skalerbar drift** | I cloud-leverancen (360° Online) hostes Systemet på Kubernetes med autoskalering og overvågning |
| **Overvågning** | 24/7 overvågning via Cloud Operations; automatiske alarmer ved afvigelser |
| **Patch og vedligehold** | Regelmæssige sikkerhedsopdateringer og patch management; sårbarhedsscanning |
| **Serviceinformation** | Driftsstatus og planlagt vedligehold kommunikeres via serviceportal |

**Eksempel:** Ved en infrastrukturafbrud kan Systemet gendannes fra backup til et tidligere konsistent tidspunkt. Brugerne kan herefter logge ind og fortsætte arbejdet med sager, dokumenter og igangværende arbejdsgange.

### Tidssvarende teknologier og trusselbillede

Systemet anvender tidssvarende teknologier og metoder, der tager højde for det aktuelle trusselbillede:

- **Rammeværker:** ISO 27001-certificering; design i overensstemmelse med CIS Controls Cloud Companion Guide v.8.1
- **Trusselsdetektion:** Microsoft Defender for Cloud, antimalware og central logning
- **Proaktiv test:** Årlige penetratonstests, automatiske sårbarhedssscanninger og OWASP ZAP i CI/CD-pipeline
- **Hændelseshåndtering:** Dokumenterede rutiner for identifikation, eskalering og varsling til Kunden
- **Kontinuerlig forbedring:** Månedlige sikkerhedsrutiner, patch-vurdering og opdatering af kontroller ved nye trusler

CIA-principperne er indtænkt i hele Systemets livscyklus — fra arkitektur og udvikling over drift til vedligehold og incident response.
