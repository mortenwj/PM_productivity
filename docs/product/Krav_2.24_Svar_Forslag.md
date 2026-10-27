# Krav 2.24 – Forslag til besvarelse

Besvarelsen er delt i to seksjoner: først løsninger og beskyttelse som svar på hovedkravet, deretter en egen seksjon som adresserer Brukerscenario 4. Tekst kan limes inn i kravtabellen under **Leverandørens besvarelse Ugradert** og **Leverandørens besvarelse Gradert**.

---

## Leverandørens besvarelse Ugradert

### 1) Løsninger og beskyttelse (til og med verktøy og rutiner)

Tjenesten er utformet med løsninger og rutiner som gir Oppdragsgiver tillit til at Kundens data er tilgjengelige, beskyttet mot uautorisert tilgang og uautoriserte endringer, og ikke går tapt.

**Tilgjengelighet:** Kundens data lagres med geo-redundans i norske datasentre (for norske offentlige kunder). Filarkiv og databaser sikres med daglige backuper til dedikerte lagringskontoer i eget abonnement, Point-In-Time Recovery med 35 dagers historikk, Long Term Retention for databaser, og soft delete for filer i 35 dager. Backup-verifikasjon skjer automatisk; ved feil reagerer driftsorganisasjonen. RTO ved full disaster recovery er 12 timer per tenant; gjenopprettingsprosedyrer testes gjennom firedrill- og disaster recovery-øvelser.

**Beskyttelse mot bortfall av Kundens tilgang til Kundens data:** Geo-redundans, backup og DR-rutiner som ovenfor sikrer at data kan gjenopprettes og at Tjenesten kan tas i bruk igjen ved tekniske feil eller katastrofer. Overvåking og kapasitetsstyring med automatiske varsler bidrar til at flaskehalser oppdages og håndteres.

**Beskyttelse mot uautorisert tilgang:** All kommunikasjon er kryptert med TLS 1.2/1.3. Data i ro krypteres med Azure TDE på databaser og AES-256 på arkiv; nøkler forvaltes sikkert. Tilgang til dokumenter og saker styres utelukkende gjennom rettighetsmatrise og radtillatelser i Tjenesten – det finnes ingen bakdør eller skjult mekanisme som gir brukere tilgang utenom eksplisitt tildeling. Tenant-isolasjon (egen applikasjonspool, egen databasebruker, egen blob-container med SAS som fornyes ved oppgradering) sikrer at kundedata ikke lekker mellom kunder. Kun operasjonsteamet hos Skytjenesteleverandøren har tilgang til produksjonsabonnementer (RBAC); dekryptering av filer krever flere nøkler og er begrenset til få tekniske personer; tilgang utenfor EØS fjernes.

**Beskyttelse mot uautoriserte endringer:** Endringer krever Rediger- eller Slett-nivå i tilgangsstyringen; tillatelser som «Rediger fil» er finmasket under tilgangsnivået. Audit trail i Tjenesten logger hvem som har lest, redigert eller endret saker og dokumenter; loggene er tilgjengelige for Kunden. Admin-audit logg i 360° Administrator logger konfigurasjonsendringer. Azure SQL-audit og logging på plattformnivå bidrar til sporbarhet.

**At data ikke går tapt:** Backup, soft delete og LTR som ovenfor; RPO ved serverkrasj er 0 sekund for filarkiv (lagres i Azure Storage) og i millisekunder for database; ved fullt datasenterkrasj er RPO for database under 1 time.

**Verktøy og rutiner – intern risiko (Leverandør, Skytjenesteleverandør og underleverandører, inkl. admin- og installasjonsbrukere):** Tilgangsrettigheter til sky- og administrasjonsportaler gjennomgås regelmessig (månedlig for produksjon) med prinsippet minst mulig tilgang og segregasjon av oppgaver. Ved fratredelse deaktiveres konto umiddelbart. Kun drifts- og automasjonsteam har tilgang til servere; RDP kun fra whitelist (VPN/tillatte kontorer), med audit av hvem som henter påloggingsdata; RDP-passord regenereres hver natt. SQL Server admin-passord regenereres ukentlig. TLS-sertifikater og nøkler forvaltes i Azure Key Vault med full audit trail. Årlig sikkerhetstrening og rutiner ved sikkerhetsbrudd (varsling til Kunde, analyse, mulig stenging av tilgang) er etablert. Sårbarheter og patching vurderes månedlig/kvartalsvis; siste sikkerhetsoppdateringer påføres ved oppgradering. Aktivitets- og audit-logger kopieres til eget abonnement med immutable policy; kun operationsleder har lesetilgang, for å sikre at operatører ikke kan slette spor.

### 2) Brukerscenario 4 – Motstandsdyktighet mot intern utro tjener

**Dokumentintegritet og tilgang:** Tilgang til å lese eller redigere en fil er styrt utelukkende av tilgangsstyringen i Tjenesten (radtillatelser og rettighetsmatrise). Det finnes ikke mulighet for en bruker å lese eller redigere en fil som vedkommende ikke aktivt er tildelt tilgang til – det er ingen bakdør eller skjult mekanisme. Systemroller som teknisk kunne omgå tilgangskontroll tildeles ikke vanlige brukere. Audit trail logger hvem som har lest, redigert eller endret dokumenter og saker, slik at Kunden kan ettergå og oppdage misbruk.

**Hvordan en insider kan utnytte sårbarheter avhengig av rolle:** Med rolle saksbehandler/leder kan en insider kun påvirke saker og dokumenter som vedkommende er tildelt tilgang til via rettighetsmatrise og tilgangsgrupper; mulig skade begrenses til endring eller sletting innenfor eget tilgangsområde, og alle handlinger logges i audit trail. Med rolle administrator (f.eks. brukeradministrator) kan vedkommende endre tilgangsgrupper og rettighetsmatrise og dermed utvide egen eller andres tilgang; slike handlinger logges i Admin-audit, og Oppdragsgiver reduserer risiko ved å begrense antall personer med administratorrolle. Med rolle arkivar har vedkommende ofte brede tilganger via tilgangsgrupper/tokens; tilgang er fortsatt styrt av radtillatelser, og audit trail viser arkivarens handlinger.

**Admin-brukere og passord:** Det finnes ikke felles, statiske admin-passord for brukere av Tjenesten. Tilgang til produksjonsmiljøet hos Skytjenesteleverandøren skjer med personlige kontoer og MFA. RDP-passord til servere regenereres hver natt; SQL Server admin-passord regenereres ukentlig. Oppdragsgiver styrer hvem som får administratorrolle i Tjenesten (f.eks. brukeradministrator).

**Risikoer og arbeid – ansatte hos Skytjenesteleverandøren eller underleverandører:** Leverandøren og Skytjenesteleverandøren kjenner til at personell med tilgang til lagring og nøkler i prinsippet kan nå kundedata; risikoen dempes ved få personer med slik tilgang, personlige kontoer, MFA, tilgang kun innenfor EØS, audit og regelmessig gjennomgang av tilgangsrettigheter. Årlig penetrasjonstest, OWASP ZAP i release-pipeline, kodegjennomgang (inkl. ekstra godkjenning for endringer i tilgangskontroll) og hardening (CIS-referanse) inngår i arbeidet med å identifisere og begrense sårbarheter.

**Eventuelle sårbarheter knyttet til Brukerscenario 4:** Sårbarheter er særlig knyttet til at brukere med administrator- eller arkivrolle har større handlingsrom; dette begrenses av audit trail, at Kunden styrer hvem som får slike roller, og at konfigurasjonsendringer logges i Admin-audit. Teknisk personell hos Skytjenesteleverandøren har i prinsippet mulighet til å nå lagring og med betydelig innsats dekryptere data; tiltakene ovenfor (få personer, personlige kontoer, MFA, EØS-begrensning, audit) reduserer risikoen.

---

## Leverandørens besvarelse Gradert

### 1) Løsninger og beskyttelse (til og med verktøy og rutiner)

Tjenesten er den samme som for ugradert dokumentasjon, men installeres og driftes på Kundens infrastruktur (plattform B og K). Løsninger og rutiner som gir tillit til at Kundens data er tilgjengelige, beskyttet mot uautorisert tilgang og uautoriserte endringer, og ikke går tapt, bygger på samme produktdesign: tilgang styres utelukkende via rettighetsmatrise og radtillatelser; audit trail og Admin-audit logger handlinger og konfigurasjonsendringer; det finnes ikke felles admin-passord for brukere, og tilgang er knyttet til personlige kontoer. For graderte miljøer er det Kunden som sørger for og forvalter infrastruktur, backup og gjenoppretting i tråd med sikkerhetskravene for plattform B og K. Leverandøren bidrar med dokumentasjon og bistand til å utarbeide drifts- og backup-rutiner (jf. krav 2.27 og 2.28). Beskyttelse mot bortfall av tilgang, uautorisert tilgang, uautoriserte endringer og datatap ivaretas gjennom Kundens egen infrastruktur- og driftsstyring, supplert med Tjenestens innebygde tilgangsstyring, logging og revisjonsspor. Verktøy og rutiner som omfatter risiko knyttet til admin- og installasjonsbrukere er i graderte miljøer Kundens ansvar; Leverandøren stiller tilgjengelig dokumentasjon og beste praksis og kan bistå med råd om rutiner og tilgangskontroll i etableringsfasen.

### 2) Brukerscenario 4 – Motstandsdyktighet mot intern utro tjener

**Dokumentintegritet og tilgang:** Som for ugradert styres tilgang til å lese eller redigere en fil utelukkende av tilgangsstyringen i Tjenesten. Det finnes ikke mulighet for å lese eller redigere en fil uten å være aktivt tildelt tilgang til det dokumentet i Tjenestens tilgangsstyring; det er ingen bakdør eller felles brukere. Audit trail og Admin-audit logger handlinger og konfigurasjonsendringer.

**Hvordan en insider kan utnytte sårbarheter avhengig av rolle:** Samme prinsipper som for ugradert: saksbehandler/leder kan kun påvirke det vedkommende har tilgang til; administrator kan endre tilgangsregler (handlinger logges); arkivar har ofte brede tilganger, men styrt av radtillatelser og audit. Oppdragsgiver reduserer risiko ved å begrense antall personer med administratorrolle og ved egne rutiner for tilgangsgjennomgang og sikkerhetstrening.

**Admin-brukere og passord:** Det finnes ikke felles admin-passord for brukere av Tjenesten. Kundens driftspersonell har tilganger i det graderte miljøet; Oppdragsgiver har full kontroll over hvem som har tekniske tilganger og kan gjennom egne rutiner styre admin- og installasjonsbrukere.

**Risikoer og eventuelle sårbarheter:** Risiko knyttet til insidere og ansatte/underleverandører i graderte miljøer avhenger av Kundens styring av administrator- og arkivroller samt Kundens rutiner for driftspersonell og tilgangskontroll. Eventuelle sårbarheter knyttet til Brukerscenario 4 er i tillegg avhengig av disse Kundens rutiner; Leverandøren stiller tilgjengelig dokumentasjon og beste praksis for sikker drift og kan bistå med råd om rutiner og overvåking i etableringsfasen.
