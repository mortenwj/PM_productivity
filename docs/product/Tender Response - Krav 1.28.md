# Krav 1.28 — Produktstrategi og veikart (2026–2029)

**Kundens krav:** Leverandøren skal beskrive produktstrategi og veikart for de neste tre årene, herunder planlagt funksjonalitet, teknologiske endringer, utfasing av komponenter, bruk av åpne standarder og hvordan Kunden varsles og involveres ved vesentlige endringer.

---

## Leverandørens besvarelse

Leverandøren videreutvikler Tjenesten (Public 360° Online) som ett standardisert SaaS-produkt for offentlig sak-, dokument- og arkivhåndtering. Produktstrategien bygger på kontinuerlig reinvestering i produktutvikling, etterlevelse av nasjonale krav og fellesløsninger, og tett dialog med offentlige kunder — behov identifiseres gjennom Serviceportal, CSM, brukerforum, discovery og felles arrangementer (f.eks. kunde- og brukerkonferanser). Veikartet for de neste tre årene (2026–2029) uttrykker Leverandørens gjeldende prioriteringer; enkelte leveransetidspunkter kan justeres i ordinær produktforvaltning uten at dette endrer avtalt leveranseomfang eller SLA. Detaljert roadmap fremlegges som vedlegg til tilbudet og holdes ajour gjennom Leverandørens kunde- og serviceportal.

Produktstrategien balanserer produktivitet (prosessstøtte, regler, KI-assistenter), kontroll (digital suverenitet, logging, Human-in-the-loop) og samhandling (nasjonale fellesløsninger, åpne API-er), slik at Kunden kan automatisere rutiner uten å miste faglig ansvar og etterrettelighet. Overordnet søker Leverandøren å forbedre arbeidslivet for offentlig ansatte og samfunnsnytten for innbyggere og virksomheter Kunden betjener.

### Verdikjede og strategiske prioriteringer

Tjenesten plasseres i en sammenhengende verdikjede for digitale tjenester: innsamling av strukturerte data, saksbehandling, publisering, arkivering og engasjement mot innbyggere og parter — med Public 360° som kjerne for saks- og dokumentforvaltning, supplert av moduler som 360° Collect (digitale skjema/e-tjenester), 360° OpenGov, 360° Flow og planlagte kapabiliteter som 360° My Pages (innbyggeroppfølging). Strategien har tre komplementære spor på tvers av planperioden:

- Individuell standard (kjernefleksibilitet) — konfigurerbare registreringsbilder, maler, tilgangsstyring og Full Flex UI-retning for entiteter, slik at Kunden kan tilpasse arbeidsflaten uten kjernekodeendringer.
- Digital helhet (ende-til-ende) — tettere kobling mellom innsending, sak, dokument, prosess, signering og arkiv; API Gateway og neste generasjon integrasjons-API (NG Integration API) styrker samhandling med Kundens øvrige IKT-miljø.
- Intelligent prosesstøtte — Flow, Forløp, BRE, KI-assistenter og beslutningsstøtte (søk, rapportering, sakstid) som reduserer manuelt arbeid og styrker datakvalitet og ledelsesinformasjon.

Videreutviklingen styres av brukerorientert verdiskaping (løse reelle problemer, ikke teknologi for teknologiens skyld), innebygd compliance (sikkerhet og personvern by design, oppfølging av lov og regulering), ansvarlig innovasjon (menneskesentrert, forklarlig og kontrollerbar KI) og geopolitisk/regulatorisk utvikling — herunder økende krav til digital suverenitet og dokumenterbar kontroll over data, tilgang, drift og portabilitet.

### Overordnet produktstrategi (2026–2029)

Strategien har seks hovedspor som gjelder hele planperioden:

1. Effektiv saks- og dokumentbehandling — konfigurerbare registreringsbilder, dokumentflyt, distribusjon, frister og arbeidslister, med mål om færre manuelle steg og høyere datakvalitet (jfr. krav 3.1).

2. Prosessstøtte og kontrollert automatisering — kombinasjon av dokumentflyt, saksprosesser (360° Flow og Forløp), regelstyring (Business Rules Engine) og integrasjonsbasert automatisering, slik at Kunden kan standardisere behandlingsløp uten skreddersøm i kjernekode. Retningen er et prosessorientert arbeidsområde der nødvendig informasjon samles på ett sted, i stedet for fragmentert oppfølging på tvers av faner og manuelle overleveringer.

3. Digital samhandling og integrasjon — produktiserte koblinger mot nasjonale fellesløsninger og virksomhetens øvrige IKT-miljø gjennom standardmoduler og 360° Simple Integration Framework (SIF API) (jfr. krav 1.24).

4. Ansvarlig bruk av kunstig intelligens (KI) — KI inngår som integrert del av standardproduktet der teknologien gir dokumenterbar nytte, med Human-in-the-loop, AI Governance Framework, GDPR og EU AI Act (inkl. ISO/IEC 23894 i utviklingsprosesser). Leverandøren prioritiserer industrielle, oppgavebundne KI-moduler (forutsigbar kvalitet og kostnad) fremfor generell «chat i kjernen». Enkelte moduler beskrives nærmere under krav 1.29.

5. Digital suverenitet og valgfrihet i plattform og dokumentlag — se eget avsnitt under; inkluderer alternativer til tradisjonell public cloud der Kundens krav, risikoprofil og styringsmodell tilsier det (jfr. krav 2.20).

6. Moderne, sikker og vedlikeholdbar plattform — web-først brukeropplevelse, designsystem, sikker utvikling (bl.a. OWASP ZAP før release), drift med public cloud i Norge som strategisk utgangspunkt, videreutvikling på Linux, containere og Kubernetes for økt portabilitet, og etterlevelse av ISO/IEC 27001.

Tjenesten videreutvikles kontinuerlig gjennom planlagte releaser. Det planlegges normalt fire funksjonalitetsleveranser per år, supplert med vedlikeholdsleveranser etter behov (jfr. krav 1.21).

### Planlagt funksjonalitet og veikart (2026–2029)

Veikartet er prioritert på tema- og modulnivå. Vedlegg Roadmap 2026–2029 viser detaljer på release-nivå. Alle områder på roadmap kan endres med hensyn til leveransetidspunkt og om de leveres, som ledd i ordinær produktforvaltning.

**2026 — KI, gjenfinning og mottak**  
Videreutvikling av 360° Search Assistant (naturlig språk → deterministisk, strukturert avansert søk med synlige kriterier; statistikk/gruppering for kvalitets- og ledelsesrapporter); moden bruk av 360° Mimir (veiledning i rutiner og produkthjelp) og 360° Archive Inspector; Intelligent dokumentregistrering for effektiv og metadata-sterk registrering (jfr. krav 1.29). Styrket regelstyrt mottak gjennom 360° AutoSaver og dokumentfangst fra e-post, eFormidling og integrasjoner.

**2026–2027 — Digital innsamling og innbyggerreise**  
360° Collect — plattform for digitale skjema og e-tjenester med direkte overføring til Public 360° via SIF, nordisk eID, tilgjengelighet, revisjonsspor og kobling til AutoSaver/Flow. 360° My Pages (planlagt videreutvikling) skal gi innbyggere og parter status, varsler og oppfølging etter innsending, som supplement til saksbehandling i Kjerne-Tjenesten.

**2026–2027 — Prosessstøtte (360° Flow og Forløp)**  
For strukturerte behandlingsløp benyttes Forløp og 360° Flow: prosessmodeller med faser, milepæler, sjekklister, ansvar, frister og oppgaver. Veikart inkluderer Online Process Models, Process Library (neste generasjon), styrket modellering i administratorverktøy, og tettere kobling mellom Flow, registrering, distribusjon og integrasjoner (inkl. innsendinger fra Collect i definert prosesstrinn). Første modeller etableres normalt i implementeringsprosjekt; Kunden kan deretter forvalte modeller innenfor standard funksjonalitet.

**2026–2027 — Business Rules Engine (BRE)**  
Regelstyrt automatisering konfigurert uten programutvikling, knyttet til registrering, tilgangsstyring, arbeidsflyt og Flow. Tjenesten kan brukes med etablerte dokumentflyter og Flow uten at BRE er forutsetning; BRE innføres gradvis i sky.

**2026–2027 — Agentisk og generativ støtte (kontrollert)**  
Orkestrert, flertrinns støtte der systemet foreslår og forbereder begrensede deloppgaver innenfor regler; menneske beholder ansvar for vedtak og disposisjoner. Veikart: kobling KI-funn, BRE og Flow (forslag → godkjenning → prosesstrinn); 360° GAIIA og GAIIA API for sikker, formålsbundet tilgang til arkivdata; sakstidsprediksjon som planleggingsstøtte — ikke autonom saksavgjørelse.

**2026–2028 — Ledelse, rapportering og API**  
360° Management Reporting API og NG Integration API — dokumentert vei fra Public 360° til BI og dataplattform (redusert manuell SQL/API-mapping); 360° API Gateway for konsolidert integrasjonsinngang; videreutvikling av maler/saksopprettelse og møtestøtte der det inngår i standardproduktet.

**2026–2029 — Microsoft 365 og kontor-alternativer**  
Videre styrking av webbasert dokumentarbeid (360° Integration with MS Office Apps, New Outlook-sidepanel, Teams/SharePoint); 360° Power Automate Connector; strategisk retning mot Office-alternativer (bl.a. browserbasert redigering via åpne integrasjonsmodeller som WOPI/Collabora Online) og klientuavhengighet (Windows/Mac/Linux, desktop og nettleser) slik at Kunden ikke låses til én dokumentleverandør alene (jfr. krav 1.10).

**2026–2029 — Nasjonale fellesløsninger**  
Løpende tilpasning av integrasjoner (eFormidling, DPI/KRR, eInnsyn, eSignering m.fl.) og vurdering av nye fellesløsninger for standardproduktet (jfr. krav 1.24).

**2026–2029 — Tilgjengelighet og etterlevelse**  
Løpende oppfølging av WCAG 2.2 og EN 301 549; videreutvikling i tråd med NOARK 5.5 og myndighetskrav (jfr. krav 1.19).

### Prosessstøtte — lagdelt modell (status og retning)

Dokumentflyt — standard arbeidsflyter (Send til gjennomgang/godkjenning) med oppgaver, frister og varsling.

360° Flow og Forløp — saksnivå med virksomhetstilpassede prosessmodeller.

BRE — regelstyrt automatisering på tvers av registrering og prosess.

Integrasjon (SIF API, Power Automate, AutoSaver, Collect→Flow) — eksterne hendelser inn i samme sakskontekst med logging.

Retningen er sammenhengende prosesstøtte fra mottak til arkiv, med sporbarhet i hele løpet.

### Digital suverenitet og plattformvalg (produktstrategi)

Leverandøren skiller mellom cloud-suverenitet (organisasjonens kontroll over data, tilgang, drift, jurisdiksjon, portabilitet og teknologivalg) og Microsoft Sovereign Cloud (et konkret Microsoft-tilbud og kontrollmodell i Microsoft-økosystemet). Suverenitet er en vurdering av kontroll og risiko; Sovereign Cloud er ett mulig spor — ikke synonymt med Leverandørens helhetlige suverenitetsstrategi.

**Public cloud som strategisk utgangspunkt (for de fleste kunder)**  
Ordinær SaaS-leveranse bygger på Microsoft Azure i Norge (Norway East primær, Norway West redundans): rask tilgang til produktroadmap, skalerbarhet, sikkerhetskapabiliteter og KI-spor, med dokumenterte kontroller (datalokalitet, kryptering, tilgangsstyring, overvåking, backup/gjenoppretting, KI-dataløp med eksplisitt region/formål). Kunden beholder governance over data, klassifisering, prosesser og organisatoriske beslutninger. Public cloud er default, ikke eneste mulighet.

**Alternativer når krav, risiko eller politikk tilsier mer kontroll**  
Hostingmodell og suverenitetsnivå velges ut fra krav → kontroller → evidens → rest-risiko → beslutning, ikke ut fra leverandørnavn alene:

| Spor | Når det er aktuelt | Hovedtrekk |
|------|-------------------|------------|
| Public cloud (Azure Norge) | Standard SaaS; krav dekkes med evidens | Innovation, skala, KI; Kundens data i Norge |
| Domestic cloud | Krav om domestic drift, leverandørkjede eller risikoprofil | Tieto Sovereign Cloud — datasentre eid og driftet i Norge, alternativ til amerikansk-eid hyperscaler |
| Microsoft Sovereign Cloud | Krav som adresseres med Microsofts sovereignty-kontrollmodell | Supplerende spor der Kunden og kravene peker dit |
| Self-hosted / on-premises | Kunden bevisst tar platform-, livssyklus- og driftsansvar | Unntaksspor; krever avklart driftsmodell, kompetanse og økonomi |

Jo mer kontroll Kunden tar på plattformlag, desto mer eget ansvar for patching, overvåking, backup, hendelser og release — kontroll uten driftsmodell gir falsk trygghet. Leverandøren bistår Kunden med å oversette suverenitetskrav til valg, inkludert når default-sporet fortsatt er tilstrekkelig.

**Suverenitet i produktarkitekturen — ikke bare «hvor serveren står»**  
Public 360° videreutvikles for valgfrihet høyere i stacken:

- Kundens prosesser — saksbehandling, journalisering, arkiv, tilgangsstyring.
- Integrasjon og data — SIF/OpenAPI, OAuth/OIDC, dokumenterte uttrekk og exit (database/arkiv i avtalte formater, kontrollert overføring, midlertidig klargjøring og sletting etter overlevering).
- Dokument- og samarbeidslag — redusert avhengighet av én kontorleverandør; støtte for Microsoft 365, browserbasert redigering og åpne alternativer (retning: Collabora/LibreOffice-spor, WOPI-baserte integrasjoner), på tvers av Windows/Mac/Linux.
- Plattform og portabilitet — roadmap for Linux, containere og Kubernetes styrker mulighet for domestic/self-hosted driftsmodeller uten å låse produktutviklingen til én hyperscaler-API.

Leverandørens posisjon er pro-valgfrihet, pro-portabilitet og pro-dokumentert kontroll — ikke anti-sky, men forberedt på skjerpede krav i Norge og Europa (jurisdiksjon, CADA-lignende vurderinger av assurance og suverenitetsrisiko).

**Underleverandører og KI**  
Transparent dokumentasjon via Trust Center/DPA; Kunden varsles ved endringer i underleverandørkjede (jfr. krav 2.19–2.20). 360° GAIIA skal sikre at Kunden kan utnytte arkivdata innenfor egne styringsrammer, ikke bare i Leverandørens ferdigdefinerte funksjoner.

**Åpne standarder**  
NOARK, OpenAPI/SIF, OAuth/OIDC og nasjonale fellesløsninger støtter uttrekk, samhandling og systemskifte (jfr. krav 1.19).

### Teknologiske endringer

Over planperioden planlegges blant annet:

- Product Change Management — konsekvensanalyse, testing (regresjon, ytelse, sikkerhet), godkjenning og kontrollert produksjonssetting (jfr. krav 1.3 og 1.21).
- Skyplattform — videre utvikling på Azure i Norge som default; parallelt container-/Kubernetes-spor for portabilitet og alternative driftsmodeller; plattformoppdateringer følger leverandørens livssyklus innenfor sikkerhets- og compliance-krav.
- Integrasjonsarkitektur — konsolidering rundt REST/OpenAPI 3.0 (SIF), API Gateway, NG Integration API, og OAuth 2.0 / OpenID Connect (Entra ID).
- Utrulling — planlagte oppgraderinger normalt kl. 22.00–06.00; kritiske sårbarheter etter nødpatch-rutiner med varsling til Kunden.

Større teknologiske skifte vurderes mot sikkerhet, kundemodenhet og oppgraderingssikker konfigurasjon (standard low-code/no-code).

### Utfasing av komponenter

Leverandøren følger en kontrollert utfasingsmodell:

- Planlagt endring, reduksjon eller utfasing dokumenteres i Release Notes og, ved vesentlige endringer, via kundeportal og direkte varsler.
- Der det er praktisk mulig, tilbys parallelle arbeidsmåter i overgangsperiode (f.eks. Outlook Classic med 360° Client og New Outlook / Office på web med 360° Integration with MS Office Apps; på sikt flere Office-alternativer der Kunden velger det).
- Integrasjoner forvaltes med dokumentasjon, test og eventuell utfasing (jfr. krav 1.23).
- Enkelte funksjoner (bl.a. skanning, Noark-eksport og deler av maladministrasjon) forutsetter fortsatt 360° Client på Windows; strategien er å redusere behovet for lokal klient for ordinær saksbehandling, ikke å fjerne støtte uten varsel og erstatningsløp.

Konkrete utfasingsdatoer annonseres i Release Notes når beslutning er tatt.

### Bruk av åpne standarder

Videreutviklingen bygger på åpne og anerkjente standarder, som beskrevet under krav 1.19, herunder OpenAPI 3.0 og REST (SIF), OAuth 2.0 / OpenID Connect, NOARK 5 (XML/metadata), PDF/A (ISO 19005), WCAG 2.2, og Digdirs dokumenterte grensesnitt for relevante nasjonale fellesløsninger. Nye funksjoner designes med dokumenterte API-er før proprietære punkt-løsninger.

### Varsling og involvering ved vesentlige endringer

Leverandøren skiller mellom (A) informasjon om planlagte produktendringer, (B) Kundens innspill til videreutvikling av standardproduktet, og (C) kundespesifikke endringer/tilleggsleveranser.

#### A. Informasjon om planlagte endringer (roadmap og releaser)

**Kanaler:** kunde-/serviceportal, e-postvarsler, Release Notes (Tjenestens hjelpetekst / Information Hub), webinarer ved større funksjonalitetsreleaser, og Continuous Service Manager (CSM) som fast kontaktpunkt (jfr. krav 1.22 og 5.8). Drifts- og sikkerhetshendelser varsles etter gjeldende prosesser (jfr. krav 1.3).

**Varsling før planlagte oppgraderinger (SaaS):** For funksjonalitetsleveranser sendes normalt forhåndsvarsel ti virkedager før oppgradering, med lenke til Release Notes. Tre dager før sendes bekreftelse med nøyaktig dato og tidspunkt. Gjennomføring skjer normalt kl. 22.00–06.00. Alle varsler inneholder lenke til Release Notes med endringer, feilrettinger og eventuelle konsekvenser.

**Hotfixes:** Kritiske feil kan distribueres uten full forhåndsvarsel, men dokumenteres (hotfixlogg) og kommuniseres til berørte kunder.

**Involvering i mottak av endringer:** Kundens definerte kontaktpersoner og superbrukere forberedes via Release Notes, webinar og oppdatert brukerdokumentasjon/e-læring. Testmiljø gjør at større endringer og integrasjoner kan verifiseres før produksjonssetting; etablerte integrasjoner kan reverifiseres i avtalt testvindu (jfr. krav 1.23). I operative møter med CSM kan kommende releaser og konsekvenser for Kunden tas opp (jfr. krav 1.22).

#### B. Kundens innspill til produktutvikling (endringsønsker til standardproduktet)

Kunden skal kunne påvirke retningen i standardproduktet, ikke bare motta ferdige releaser. Leverandøren har etablert en strukturert innmeldings- og prioriteringsmodell for forbedringsønsker:

**Innmelding av endringsønsker**  
Kunden kan melde inn produktutviklingsønsker, forbedringsforslag og behov knyttet til standardfunksjonalitet via Leverandørens Serviceportal (jfr. krav 5.8). Portalen brukes også til hendelser, feil og support; ved innmelding kategoriseres saken slik at forbedringsønsker skilles fra feilretting. Kundens CSM er et alternativ og supplementært kontaktpunkt for å avklare, formulere og eskalere forslag som bør inn i produktsporet.

**Vurdering og sporbarhet**  
Innmeldte forslag registreres med referansenummer og følges i portalen. Leverandørens produktorganisasjon vurderer hvert forslag med utgangspunkt i blant annet relevans for offentlig sak-/arkivdomene og Kundens behov, gjenbruk på tvers av kundegrunnlaget (standardprodukt vs. unntak), sammenheng med nasjonale krav, fellesløsninger og sikkerhet, samt kapasitet, avhengigheter og risiko i releaseplanen.

Forslag som vurderes å ha generell verdi, prioriteres inn i produktbacklog og veikart. Kunden får tilbake status og avklaring (implementert, planlagt, under vurdering, avslått med begrunnelse der det er mulig). Leverandøren garanterer ikke at hvert enkelt ønske implementeres, men garanterer at innspill mottas, registreres og vurderes etter felles kriterier.

**Dialog utover enkelthenvendelser**  
I tillegg til enkeltinnmeldinger skjer innhenting av behov gjennom løpende dialog med CSM og i operative/forvaltningsmøter, erfaringer fra implementering og forvaltning hos Kunden (superbrukere, prosess-eiere), og bruker- og fagmiljø i offentlig sektor der Leverandøren deltar (kunde-/brukergrupper, fagforum, tilgjengelighetsarbeid m.m.).

#### C. Discovery-prosjekter sammen med kunder

For større eller mer usikre behov, der løsningen ikke kan avklares gjennom enkeltkrav eller konfigurasjon alene, gjennomfører Leverandøren discovery-prosjekter i samarbeid med utvalgte kunder — inkludert offentlige virksomheter med lignende domene.

**Formål:** Avklare problem, mål, prosess, data og risiko før funksjonalitet forpliktes i roadmap og release. Discovery skal redusere feilprioritering og sikre at ny funksjonalitet er oppgraderingssikker og standardiserbar.

Kunden kan inviteres inn i discovery der temaene er relevante (f.eks. prosessstøtte/360° Flow, regelstyring/BRE, KI-assistenter, integrasjon mot fellesløsninger, plattform- og suverenitetsvalg, Office-alternativer). Deltakelse er frivillig og avtales case for case; det medfører ikke at Kunden alene finansierer standardproduktutvikling.

**Tidlig tilgang:** Der Leverandøren kjører pilot/beta av ny funksjonalitet, kan Kunden etter avtale få tidlig innsyn i testmiljø, gi tilbakemelding før generell release, og dermed påvirke kvalitet og utforming før produksjonssetting.

#### D. Skille mot kundespesifikke endringer og tilleggsleveranser

Feil og hendelser håndteres i supportløpet med SLA (jfr. krav 5.8).

Nye bestillinger, endringsønsker som krever tilleggsarbeid utenfor standardprodukt, og kundespesifikk videreutvikling håndteres som egne bestillinger gjennom ordinære endrings- og forvaltningsprosesser og er normalt ikke omfattet av SLA for support og feilretting (jfr. krav 5.9). Leverandøren informerer Kunden når et innspill faller utenfor SaaS-standardleveransen eller kan medføre ekstrakostnader, og slike tiltak godkjennes av Kunden før igangsetting (jfr. krav 5.8).

**Oppsummert for Kunden:** Kunden har flere kanaler for involvering — Serviceportal for produktutviklingsønsker, CSM og møter for dialog og oppfølging, testmiljø for verifisering, og discovery for dypere avklaring av større tema — samtidig som varsling om releaser skjer forutsigbart og dokumentert.

### Dokumentasjon / vedlegg

- Vedlegg: Roadmap 2026–2029 (produktplan, i tråd med offentlig roadmap presentert for kunder)
- Release Notes / Information Hub (løpende)
- Detaljer om hosting, suverenitet og underleverandører: krav 2.20 (og 2.19)
- Detaljer om Serviceportal, support og tjenestenivå: krav 5.8 og tilhørende bilag
