# Tender Response — KK — Krav 5.3.2.2

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.2.2 |
| **Titel** | Løst koblet arkitektur |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast |
| **Genereret** | 2026-08-07 |

## Svar på krav 5.3.2.2

**Kundens krav:** Løst koblet arkitektur — Leverandøren bedes redegøre for Systemets interne arkitektur, herunder hvordan Systemets moduler og komponenter er organiseret, samt hvordan de kommunikerer og udveksler data med hinanden. Leverandøren kan vælge at vedlægge et diagram, der illustrerer arkitekturen.

**Leverandørens besvarelse:**

Systemet (Public 360°) er en modulær sags- og dokumentplatform, hvor kernefunktionalitet og valgfrie moduler er organiseret med klart definerede ansvarsområder og kommunikerer via etablerede API'er og integrationsgrænseflader. Arkitekturen er lagdelt og serviceorienteret, så præsentation, forretningslogik, dataadgang og integration kan udvikles og vedligeholdes med minimal indbyrdes afhængighed.

Leverandøren kan vedlægge et arkitekturdiagram som illustration (jf. bilag).

### Overordnet arkitektur

Systemet består overordnet af:

- **Præsentationslag** — webbaseret brugergrænseflade, mobilapp og klientintegrationer (Outlook, Word, Teams m.fl.)
- **Applikations- og forretningslogiklag** — kerneservices for sags- og dokumenthåndtering, arbejdsgange, adgangskontrol og processtyring
- **Integrationslag** — Simple Integration Framework (SIF) med REST/RPC-API'er til indgående og udgående dataudveksling
- **Datalag** — relationel database (Microsoft SQL Server) med defineret informationsmodel
- **Proces- og regellag** — procesmotor, konfigurerbare procesmodeller og konfigurerbar felt-/forretningslogik

Eksterne systemer og klienter kommunikerer med Systemet via SIF og standardintegrationer. Brugergrænsefladen kommunikerer med kernen via HTTP/API gennem en dedikeret sikkerheds- og adgangsproxy (AuthProxy), som adskiller autentificering og frontend-håndtering fra backend-forretningslogikken.

### Velafgrænsede moduler og komponenter

Systemet leveres som en **modulær platform**, hvor Kunden kan aktivere de funktioner, der er relevante for driften — fx dokumentekspedition, aktindsigt, processtyring, e-arkiv, centralregisterintegrationer og Microsoft 365-integrationer. Hvert modul har et afgrænset funktionelt ansvar og kan konfigureres og vedligeholdes uafhængigt inden for platformens rammer.

Kernen håndterer fælles domænelogik (sager, dokumenter, kontakter, metadata, adgangskontrol og arkiv), mens moduler tilføjer specialiseret funktionalitet via standardiserede integrations- og konfigurationsmekanismer — uden at Kunden skal ændre programkode.

I cloud-leverancen (360° Online) hostes Systemet på **Kubernetes** med tydeligt adskilte infrastrukturkomponenter (ingress, services, pods, autoskalering), hvilket understøtter skalerbar og robust drift.

### Anerkendte designprincipper

Arkitekturen følger etablerede principper for **lagdelt design og separation of concerns**, som fremmer testbarhed, vedligeholdelse og udskiftelighed:

- Forretningslogikken er centraliseret i kernen og genbruges på tværs af klienter og integrationer
- Adgangskontrol udgør et tværgående lag, så al datalæsning og -skrivning valideres konsistent
- Integrationer bygger på SIF's objektmodel, som abstraherer domænekompleksitet og giver stabile, testbare integrationskontrakter
- Procesunderstøttelse er bygget på et **transaktionelt mønster**, der sikrer konsistens mellem processtatus og underliggende data

Leverandørens udviklingspraksis understøtter modulær kode og systematisk test (enhedstest, integrationstest og automatiseret regression), hvilket styrker kvaliteten ved løbende produktudvikling.

### Lagdelt adskillelse (UI, forretningslogik, data)

Systemet er **lagdelt med tydelig adskillelse** mellem:

| Lag | Ansvar |
|-----|--------|
| **Brugergrænseflade** | Webbrowser, mobilapp, Office-tilføjelser — præsentation og brugerinteraktion |
| **Forretningslogik** | Sags-/dokumenthåndtering, arbejdsgange, validering, adgangskontrol, procesmotor |
| **Dataadgang** | Relationel datamodel og persistens i SQL Server |
| **Integration** | SIF, AuthProxy og standardintegrationer mod eksterne systemer |

Bindinger på tværs af lag minimeres: klienter og integrationer tilgår forretningslogikken via veldefinerede API'er, og adgangskontrol håndhæves centralt — ikke i enkeltvisninger eller integrationsadaptere.

### Brugergrænseflade adskilt fra kernefunktionalitet

Brugergrænsefladen er **adskilt fra kerneforretningslogikken**. Systemet understøtter flere klienter mod samme kernefunktionalitet:

- Webbrowser (primær brugerflade)
- Mobilapp til udvalgte arbejdsopgaver
- Outlook-sidepanel, Word/Template Designer og Teams/SharePoint-integrationer

Dette gør det muligt at udvikle og tilpasse brugeroplevelsen (fx rollebaserede skriveborde, registreringsskærme og klientintegrationer) uden at ændre kernens forretningsregler. AuthProxy sikrer desuden, at autentificering og autorisationshåndtering kan styres uafhængigt af backend-processer.

### Adskillelse af det foranderlige fra det uforanderlige (AR 2.6)

I overensstemmelse med den fælleskommunale rammearkitekturs princip om at **adskille det foranderlige fra det uforanderlige** adskiller Systemet:

**Stabile platformskomponenter (uforanderlige):**

- Kernens datamodel og domænelogik for sager, dokumenter og metadata
- Procesmotor og arbejdsgangsmotor
- Adgangskontrol og sikkerhedsmekanismer
- SIF og integrationsrammeværk

**Konfigurerbare/foranderlige dele (Kundens ansvar):**

- Procesmodeller og forløp (PAF) — faser, milepæler, frister og sjekklister per sagstype
- Dokumentarbejdsgange — parametriserede standardflyter (review, godkendelse m.fl.)
- Feltlogik og kontekstafhængige registreringer — obligatoriske felter, vis/skjul, standardværdier
- Kodetabeller, sagstyper, dokumentkategorier og metadatakonfiguration
- Integrationsopsætning via administratorværktøj

Kundens administratorer kan således tilpasse processer, registrering og forretningsregler **uden programmering**, mens den underliggende platform forbliver stabil og opgraderingssikker.

**Forretningsregelmotor (BRE):** Leverandøren udvikler et rammeverk for forretningsregler (Business Rules Engine), som på sigt vil udvide muligheden for regelstyret automatisering uden custom udvikling, når funktionaliteten gøres tilgængelig i Systemet. Systemet kan i dag tages i brug med standard arbejdsgange, procesmodeller og konfigurerbar feltlogik uden at BRE er en forudsætning.

### Dataudveksling mellem komponenter

Kommunikation sker primært via:

- **Interne API-kald** mellem præsentationslag og forretningslogik (via AuthProxy)
- **SIF REST/RPC** for integrationer og tredjepartssystemer
- **Standardintegrationer** mod fx Datafordeleren, Microsoft 365, eFormidling og andre fagsystemer
- **Procesmotor** der orkestrerer opgaver, status og metadata i atomare transaktioner

Alle integrationskald kan logges for sporbarhed, og Kundens administrator kan konfigurere endepunkter, filtre og feltbegrænsninger per integration.

### Samlet effekt for Kunden

Denne arkitektur giver Kunden:

- **Modulær fleksibilitet** — aktiver kun de funktioner, der er nødvendige
- **Opgraderingssikker tilpasning** — proces- og metadataændringer via konfiguration, ikke kode
- **Fremtidssikret integration** — åbne API'er og standardintegrationsmønstre
- **Klar adskillelse** mellem stabil platform og Kundens forretningsmæssige tilpasninger

## Evidence (intern)

| Claim | Kilde | Confidence |
|-------|--------|------------|
| Modulær platform med valgfrie moduler | Wiki: 360° Architecture; Public_360_Wiki_Collection | Verified |
| SIF som integrations-API mod kernen | Wiki: 360° Architecture; RFP-udtræk (NND) | Verified |
| AuthProxy adskiller frontend/autentificering fra forretningslogik | Wiki: 360° Architecture | Verified |
| Lagdelt applikationsarkitektur (adgangskontrol som tværgående lag) | Wiki: 360° Architecture | Verified |
| Procesmotor + konfigurerbare procesmodeller (PAF) | NND/RFP-udtræk | Verified |
| BRE som fremtidig regelmotor | NND/RFP-udtræk | Lead — når tilgængelig |
| Cloud: Kubernetes med ingress/services/pods | Wiki: 360° Architecture | Verified |
| Clean/Hexagonal navngivet i produktdok | — | Ikke verificeret — brug "lagdelt / separation of concerns" |

## Review-noter

- Microservices overclaim undgået — "modulær/serviceorienteret", ikke "microservices-first"
- BRE ærligt markeret som fremtidig udvidelse
- Overvej at vedlægge arkitekturdiagram fra wiki (Overall.jpg / Kubernetes) som bilag
