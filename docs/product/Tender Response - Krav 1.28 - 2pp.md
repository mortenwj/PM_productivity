# Krav 1.28 — Produktstrategi og veikart (2026–2029) — utgave 2 sider

**Kundens krav:** Leverandøren skal beskrive produktstrategi og veikart for de neste tre årene, herunder planlagt funksjonalitet, teknologiske endringer, utfasing av komponenter, bruk av åpne standarder og hvordan Kunden varsles og involveres ved vesentlige endringer.

*(Kundens krav telles ikke med i sideantallet nedenfor.)*

## Leverandørens besvarelse

Leverandøren videreutvikler Tjenesten (Public 360° Online) som ett standardisert SaaS-produkt for offentlig sak-, dokument- og arkivhåndtering. Produktstrategien bygger på kontinuerlig reinvestering i produktutvikling, etterlevelse av nasjonale krav og fellesløsninger, og tett dialog med offentlige kunder. Behov identifiseres gjennom Serviceportal, Continuous Service Manager (CSM), brukerforum, discovery og felles arrangementer. Veikartet for 2026–2029 uttrykker Leverandørens gjeldende prioriteringer; enkelte leveransetidspunkter kan justeres i ordinær produktforvaltning uten at dette endrer avtalt leveranseomfang eller SLA. Detaljert roadmap fremlegges som vedlegg og holdes ajour i kunde- og serviceportalen.

Strategien balanserer produktivitet, kontroll og samhandling, slik at Kunden kan automatisere rutiner uten å miste faglig ansvar. Public 360° er kjerne i en verdikjede fra strukturert innsamling via saksbehandling og arkiv til oppfølging mot innbyggere og parter, supplert av bl.a. 360° Collect, 360° OpenGov og 360° Flow.

### Produktstrategi og veikart (2026–2029)

Produktstrategi og veikart utgjør én plan: prioriterte retninger som realiseres gjennom planlagte releaser. Veikartet er angitt på tema- og modulnivå; vedlegg Roadmap 2026–2029 viser detaljer per release. Prioriteringer og tidspunkter kan justeres i ordinær produktforvaltning. Tjenesten videreutvikles normalt med fire funksjonalitetsleveranser per år (jfr. krav 1.21).

Hovedretningen er å gjøre det daglige saks- og dokumentarbeidet enklere og mer konsistent (jfr. krav 3.1), og samtidig løfte komplekse behandlingsløp til sammenhengende prosesstøtte — fra mottak til arkiv. Det bygges lagvis: dokumentflyt for godkjenning og oppgaver, 360° Flow og Forløp for virksomhetstilpassede prosessmodeller, regelstyring gjennom Business Rules Engine (BRE) som innføres gradvis i sky, og integrasjon som binder eksterne hendelser inn i samme sakskontekst (SIF API, Power Automate, AutoSaver, innsendinger fra Collect til definerte prosesstrinn). Målet er ett prosessorientert arbeidsområde fremfor fragmentert oppfølging på tvers av faner og manuelle overleveringer. I 2026–2027 styrkes dette bl.a. gjennom Online Process Models og Process Library, tettere kobling mellom Flow, registrering og distribusjon, og kobling mot digital innsamling.

Parallelt utvikles digitale innkanaler og innbyggerreisen: 360° Collect for skjema og e-tjenester med overføring til Public 360°, og planlagt videreutvikling av 360° My Pages for status og oppfølging etter innsending. Samhandling mot Kundens øvrige IKT-miljø og nasjonale fellesløsninger forsterkes gjennom standardmoduler og integrasjons-API (jfr. krav 1.24); fra 2026–2028 suppleres dette med 360° Management Reporting API, NG Integration API og API Gateway for rapportering og datadeling.

Ansvarlig KI er integrert der teknologien gir dokumenterbar nytte, med Human-in-the-loop, AI Governance Framework og etterlevelse av GDPR og EU AI Act (moduler nærmere under krav 1.29). Allerede i 2026 prioriteres gjenfinning og kvalitet i mottak: videreutvikling av 360° Search Assistant mot strukturert avansert søk med synlige kriterier, moden bruk av 360° Mimir og 360° Archive Inspector, intelligent dokumentregistrering og styrket mottak via 360° AutoSaver og dokumentfangst fra e-post og eFormidling. I 2026–2027 kobles kontrollert agentisk støtte til prosess og regler (KI-funn, BRE og Flow), med 360° GAIIA og GAIIA API for formålsbundet tilgang til arkivdata; sakstidsprediksjon er planleggingsstøtte, ikke autonom saksavgjørelse.

Gjennom hele planperioden videreutvikles web-først brukeropplevelse, sikker plattform (Azure i Norge som default, arbeid med Linux, containere og Kubernetes, ISO/IEC 27001), webbasert dokumentarbeid og Microsoft 365, med retning mot Office-alternativer og klientuavhengighet (jfr. krav 1.10). Etterlevelse følges løpende mot WCAG 2.2 og NOARK 5.5 (jfr. krav 1.19). Digital suverenitet og valgfrihet i plattform og dokumentlag behandles under eget avsnitt (jfr. krav 2.20).

### Digital suverenitet, teknologi og standarder

Leverandøren skiller cloud-suverenitet — organisasjonens kontroll over data, tilgang, drift, jurisdiksjon og portabilitet — fra Microsoft Sovereign Cloud som ett mulig spor i Microsoft-økosystemet. Ordinær SaaS bygger på Azure i Norge (Norway East/West) med dokumenterte kontroller; Kunden beholder governance over data og prosesser. Der krav, risiko eller politikk tilsier mer kontroll, kan det velges domestic cloud (Tieto Sovereign Cloud), Microsoft Sovereign Cloud eller self-hosted/on-premises, forutsatt avklart driftsmodell og ansvar. Produktretningen er valgfrihet og portabilitet: åpne integrasjoner, dokumentert exit, redusert avhengighet av én kontorleverandør, og containere/Kubernetes som grunnlag for alternative driftsmodeller. Endringer i underleverandørkjede varsles (jfr. krav 2.19–2.20).

Teknologiske endringer håndteres gjennom Product Change Management med testing og kontrollert produksjonssetting (jfr. krav 1.3 og 1.21). Integrasjonsarkitekturen konsolideres rundt REST/OpenAPI 3.0 (SIF), API Gateway, NG Integration API og OAuth 2.0/OpenID Connect. Planlagte oppgraderinger gjennomføres normalt kl. 22.00–06.00; kritiske sårbarheter håndteres etter nødpatch-rutiner med varsling til Kunden.

Videreutviklingen bygger på åpne standarder som beskrevet under krav 1.19, herunder OpenAPI og REST (SIF), OAuth/OIDC, NOARK 5, PDF/A, WCAG 2.2 og Digdirs grensesnitt mot fellesløsninger. Nye funksjoner designes med dokumenterte API-er før proprietære punkt-løsninger.

### Utfasing

Planlagt endring, reduksjon eller utfasing dokumenteres i Release Notes og, ved vesentlige endringer, via kundeportal og direkte varsler. Der det er praktisk mulig, tilbys parallelle arbeidsmåter i overgangsperioder, for eksempel Outlook Classic med 360° Client og New Outlook med 360° Integration with MS Office Apps. Integrasjoner forvaltes med dokumentasjon, test og eventuell utfasing (jfr. krav 1.23). Enkelte funksjoner forutsetter fortsatt 360° Client på Windows; strategien er å redusere behovet for lokal klient gradvis, ikke å fjerne støtte uten varsel og erstatningsløp. Konkrete utfasingsdatoer annonseres i Release Notes når beslutning er tatt.

### Varsling og involvering ved vesentlige endringer

Planlagte produktendringer formidles via kunde- og serviceportal, e-post, Release Notes (Information Hub), webinar ved større releaser og CSM (jfr. krav 1.22 og 5.8). Før funksjonalitetsleveranser varsles Kunden normalt ti virkedager i forveien og får bekreftelse tre dager før, med lenke til Release Notes; gjennomføring skjer normalt om natten. Hotfixes ved kritiske feil kan komme uten full forhåndsvarsel, men dokumenteres og kommuniseres. Superbrukere forberedes gjennom Release Notes og oppdatert dokumentasjon, og testmiljø gir mulighet til å verifisere endringer og integrasjoner før produksjon (jfr. krav 1.23).

Kunden kan påvirke standardproduktet ved å melde forbedringsønsker i Serviceportal eller via CSM; forslag registreres, vurderes og besvares med status. Større behov kan avklares i discovery med utvalgte kunder etter avtale. Tilleggsarbeid utenfor standardleveransen behandles som egne bestillinger (jfr. krav 5.8 og 5.9) og igangsettes etter Kundens godkjenning.

**Vedlegg:** Roadmap 2026–2029; Release Notes; hosting og suverenitet jfr. krav 2.19–2.20; Serviceportal og support jfr. krav 5.8.
