# Svar på krav 3.5.11 - Risikoklassifisering av endringer

## Hovedkrav 3.5.11: Prosess for klassifisering av endringer basert på risiko og påvirkning

Leverandøren har en etablert prosess for risikostyring som omfatter klassifisering av endringer basert på risiko og påvirkning. Prosessen er dokumentert i vår interne risikostyringsprosess og integrert i våre leveranseprosesser for endringer.

---

## Svar på krav nr. 3.5.11x

**Kundens krav:** Endringer bør vurderes ut fra hvordan de påvirker:
- Kundens hovedarbeidsprosesser
- Kritisk funksjonalitet
- Integrasjoner med kundens systemer
- Brukeropplevelse og tilgjengelighet

**Leverandørens besvarelse:**

Vår prosess for vurdering av endringer inkluderer systematisk vurdering av alle fire aspekter:

### Vurdering av påvirkning på hovedarbeidsprosesser:
- **Prestudie-prosess**: I vår upgrade-prosess gjennomføres en detaljert løsningsanalyse som kartlegger alle kundens arbeidsprosesser og hvordan endringer påvirker disse
- **Workshops med kunde**: Vi gjennomfører workshops hvor vi sammen med kunden går gjennom alle endringer og deres påvirkning på eksisterende prosesser
- **Customer Journey Plan**: Alle endringer dokumenteres i Customer Journey Plan hvor påvirkning på prosesser vurderes

### Kritisk funksjonalitet:
- **Risikovurdering**: Alle endringer gjennomgår risikovurdering hvor kritisk funksjonalitet identifiseres og vurderes
- **SWAT-prosess**: For kritiske endringer som påvirker kritisk funksjonalitet har vi en etablert SWAT-prosess (Special Weapons And Tactics) som sikrer umiddelbar oppfølging
- **Testing**: Kritisk funksjonalitet testes ekstra grundig gjennom vår testprosess

### Integrasjoner med kundens systemer:
- **Integrasjonsanalyse**: Som del av risikovurderingen analyserer vi alltid påvirkning på eksisterende integrasjoner
- **Threat Modeling**: For sikkerhetskritiske integrasjoner benytter vi threat modeling for å identifisere potensielle risikoer
- **Validering av integrasjoner**: Integrasjoner valideres i testmiljø før produksjonsdeployment

### Brukeropplevelse og tilgjengelighet:
- **Acceptance Testing**: Kunden gjennomfører acceptance testing hvor brukeropplevelse og tilgjengelighet verifiseres
- **Performance Testing**: Kontinuerlig oppfølging av ytelse sammenligner hver release med tidligere versjon for å sikre at endringer ikke påvirker brukeropplevelse negativt
- **Tilgjengelighetsovervåking**: Public 360° har kontinuerlig oppfølging av ytelse og tilgjengelighet

---

## Svar på krav nr. 3.5.11a

**Kundens krav:** Leverandøren bør kunne identifisere og dokumentere:
- Funksjoner med lav risiko
- Funksjoner med potensiell risiko for kundens integrasjoner
- Kritisk funksjonalitet som påvirker hovedarbeidsprosesser

**Leverandørens besvarelse:**

Vårt risikostyringssystem og leveranseprosesser sikrer systematisk identifisering og dokumentasjon:

### Funksjoner med lav risiko:
- **Risikoklassifisering**: Vår risikostyringsprosess benytter Tietoevry Risk Matrix and Assessment template som klassifiserer risikoer basert på sannsynlighet og konsekvens
- **Grønn sone**: Risikoer som er klassifisert i "grønn sone" (lav/meget lav påvirkning; medium, lav eller meget lav sannsynlighet) kan aksepteres av risikoeier
- **Dokumentasjon**: Alle risikoer dokumenteres i våre prosjektdokumenter, Risk logs og Status reports

### Funksjoner med potensiell risiko for kundens integrasjoner:
- **Integrasjonsrisiko**: Som del av risikovurderingen identifiseres spesifikt funksjoner som kan påvirke integrasjoner
- **Threat Modeling**: For endringer som berører integrasjoner benytter vi threat modeling for å systematisk analysere potensielle trusler
- **Risk Assessment and Threat Modeling**: Vår prosess for Risk Assessment og Threat Modeling dokumenterer identifiserte risikoer i Archer (GRC-tool)
- **Delivery Validation**: Vår leveranseprosess inkluderer validering som sjekker potensielle påvirkninger på integrasjoner

### Kritisk funksjonalitet som påvirker hovedarbeidsprosesser:
- **Solution Analysis**: I prestudie-fasen analyserer vi løsningen og identifiserer kritisk funksjonalitet
- **SWAT-kriterier**: Kritisk funksjonalitet som kan påvirke hovedarbeidsprosesser identifiseres gjennom våre SWAT-kriterier som inkluderer:
  - VIP-kunder påvirket
  - Stor økonomisk påvirkning
  - Mulig datakorrupsjon
  - Selskapets merkevarepåvirkning
- **Produkt Governance**: Vårt produktutviklingsprosess inkluderer risikovurdering hvor høy-påvirkning, høy-risiko initiativer krever ekstra gjennomgang

### Dokumentasjonsverktøy:
- **Archer (GRC-tool)**: Risikoer dokumenteres i Tietoevry's risikostyringssystem Archer
- **Risk logs**: Prosjektrisikoer følges i Risk logs som del av statusmøter og styringsmøter
- **Delivery documentation**: Alle leveranser inkluderer dokumentasjon av risikoer og påvirkninger
- **Solution description**: Løsningsbeskrivelser dokumenterer kritisk funksjonalitet og deres rolle i kundens prosesser

---

## Svar på krav nr. 3.5.11b

**Kundens krav:** Risikovurdering for hver endring bør inkludere:
- Sannsynlighet og konsekvens
- Potensielle tiltak for risikoredusering
- Behov for involvering av kunde ved høy risiko

**Leverandørens besvarelse:**

Vår risikovurderingsprosess dekker alle tre elementer systematisk:

### Sannsynlighet og konsekvens:
- **Tietoevry Risk Matrix**: Vi benytter Tietoevry Risk Matrix and Assessment template som systematisk vurderer både sannsynlighet (Likelihood) og konsekvens (Impact)
- **Risk Analysis**: Som del av risikostyringsprosessen analyserer vi hver risiko for å definere sannsynlighet og påvirkning
- **Risk Evaluation**: Risikonivå sammenlignes med akseptkriterier for å bestemme hvilke risikoer som kan aksepteres og hvilke som krever tiltak
- **Risk Matrix**: Risikoer plasseres i en risikomatrise (rød/gul/grønn) basert på sannsynlighet og konsekvens:
  - **Rød**: Krever mitigering
  - **Gul**: Overvåking eller mitigering
  - **Grønn**: Kan aksepteres

### Potensielle tiltak for risikoredusering:
- **Risk Control/Treatment**: For risikoer som ikke kan aksepteres, identifiseres og implementeres kontrolltiltak eller mitigasjonshandlinger
- **Residual Risk**: Etter implementering av tiltak vurderes residual risiko (gjenværende risiko) for å sikre at den er på akseptabelt nivå
- **Mitigation Actions**: Konkrete mitigasjonshandlinger dokumenteres med ansvarlig person og tidsramme
- **Threat Modeling**: For sikkerhetsrelaterte risikoer benytter vi threat modeling for å identifisere systematiske tiltak
- **Testing**: Ekstra testing og validering er et viktig tiltak for risikoredusering

### Behov for involvering av kunde ved høy risiko:
- **Kundeinvolvering i risikovurdering**: For høye risikoer involveres kunden aktivt i risikovurderingsprosessen
- **Acceptance Testing**: Kunden er involvert gjennom acceptance testing hvor høye risikoer verifiseres
- **Acceptance Meeting**: Ved høye risikoer gjennomføres acceptance meetings hvor kunden godkjenner løsningen før implementering
- **Workshops**: For komplekse endringer med høy risiko gjennomføres workshops med kunden for å gå gjennom risikoer og tiltak
- **Production Plan**: For høye risikoer utarbeides en Production Plan i samarbeid med kunden som beskriver alle aktiviteter og ansvar ved GoLive
- **Customer approval**: Kunden må eksplisitt godkjenne endringer med høy risiko før implementering gjennom vår acceptance certificate-prosess

### Prosessdokumentasjon:
- Risk Management-prosessen beskriver alle aktiviteter og hvordan risikoer dokumenteres
- Alle risikoer følges gjennom prosjektets levetid og rapporteres til relevante interessenter

---

## Svar på krav nr. 3.5.11c

**Kundens krav:** Rutinen for klassifisering og risikovurdering bør utarbeides og vedlikeholdes i samarbeid med HSØ og leverandøren.

**Leverandørens besvarelse:**

Vår prosess er designet for samarbeid og vedlikehold med kunden (HSØ):

### Samarbeid i utarbeiding:
- **Customer Journey Plan**: Vår Customer Journey Plan utarbeides i samarbeid med kunden og dokumenterer alle endringer og deres risikoer
- **Workshops**: Vi gjennomfører workshops med kunden hvor risikovurderinger diskuteres og justeres
- **Solution Analysis**: I prestudie-fasen samarbeider vi tett med kunden om løsningsanalyse og risikovurdering
- **Acceptance Process**: Kunden er involvert gjennom hele acceptansprosessen hvor risikovurderinger gjennomgås

### Vedlikehold og oppdatering:
- **Kontinuerlig oppfølging**: Risikoer følges kontinuerlig gjennom prosjektets levetid i Status reports og Risk logs
- **Månedlig oppfølging**: Topp-risikoer (Høy/Meget høy sannsynlighet og påvirkning) rapporteres månedlig til ledelsen, og kunden kan involveres ved behov
- **Quarterly reviews**: Fire ganger i året gjennomføres en holistisk risikoreview hvor prosessens brukbarhet og risikobevissthet vurderes
- **Customer Journey Plan**: Planen oppdateres kontinuerlig basert på nye innsikter og endringer
- **Solution Description**: Løsningsbeskrivelsen oppdateres kontinuerlig og kunden godkjenner endringer

### Prosessgovernance:
- **Forbedringsprosess**: Prosessen har en etablert forbedringsprosess hvor alle kan foreslå forbedringer
- **Prosessrevisjon**: Prosessen gjennomgås regelmessig for å sikre relevans og effektivitet
- **Dokumentasjon**: All dokumentasjon er tilgjengelig for kunden gjennom våre prosjektportaler

---

## Svar på krav nr. 3.5.11d

**Kundens krav:** Ved endringer med høy risiko bør kunde involveres i godkjenningsprosessen før implementering.

**Leverandørens besvarelse:**

Vår prosess sikrer obligatorisk kundeinvolvering ved endringer med høy risiko:

### Identifisering av høy risiko:
- **Risk Matrix**: Risikoer klassifiseres i rød/gul/grønn sone. Røde risikoer (høy sannsynlighet og konsekvens) krever obligatorisk kundeinvolvering
- **SWAT-kriterier**: Endringer som oppfyller SWAT-kriterier (kritisk, VIP-kunder berørt, stor økonomisk påvirkning) behandles som høy risiko

### Kundeinvolvering i godkjenningsprosessen:
- **Acceptance Testing**: Ved høye risikoer gjennomfører kunden obligatorisk acceptance testing før implementering
- **Acceptance Meeting**: Et acceptance meeting gjennomføres hvor kunden eksplisitt godkjenner løsningen
- **Acceptance Certificate**: Kunden signerer en Acceptance Certificate/Error correction plan som dokumenterer godkjenning
- **Production Plan**: En Production Plan utarbeides i samarbeid med kunden som beskriver alle aktiviteter ved GoLive

### Prosess før implementering:
1. **Risk Assessment**: Risikovurdering identifiserer endring som høy risiko
2. **Customer Workshop**: Workshop med kunde for å diskutere risikoer og tiltak
3. **Testing**: Ekstra testing med kundeinvolvering
4. **Acceptance Testing**: Kunden gjennomfører acceptance testing
5. **Acceptance Meeting**: Møte hvor løsningen presenteres og diskuteres
6. **Acceptance Certificate**: Kunden signerer godkjenning
7. **Production Plan**: Plan for implementering utarbeides og godkjennes
8. **GoLive**: Implementering skjer først etter eksplisitt kundegodkjenning

### Dokumentasjon:
- Alle godkjenninger dokumenteres i Acceptance Certificate
- Production Plan dokumenterer alle aktiviteter og ansvar
- Email-bekreftelse fra kunde lagres i prosjektdokumentasjon
- Risikovurderinger dokumenteres i Risk logs og prosjektdokumenter

### Eksempel på praktisk implementering:
- **Upgrade Process**: I vår upgrade-prosess er MS4 (Milestone 4) "Customer acceptance according to acceptance criteria" en obligatorisk milepæl før GoLive
- **DP6**: Decision Point 6 "Decision to approve the result of delivery" krever dokumentasjon av kundegodkjenning før implementering
- **GoLive**: GoLive skjer kun etter eksplisitt kundegodkjenning gjennom acceptance certificate

Denne prosessen sikrer at kunden alltid er fullt informert og har godkjent endringer med høy risiko før de implementeres i produksjon.















