# Tender Response — KK — Krav 5.3.7.3

| Field | Value |
|-------|-------|
| **Krav ID** | 5.3.7.3 |
| **Titel** | Security by default |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast (efter review) |
| **Genereret** | 2026-08-17 |

## Svar på krav 5.3.7.3

**Kundens krav:** Security by default — Leverandøren bedes redegøre for, hvilke foranstaltninger der anvendes og hvordan disse benyttes for at Systemet efterlever security-by-default-princippet. Leverandøren bedes anvende konkrete eksempler på designmønstrene: economy of mechanism, least privilege, defense in depth, failing securely, separation of privilege, least common mechanism og promoting privacy.

**Leverandørens besvarelse:**

Systemet er designet med security by default som udgangspunkt: sikker konfiguration, restriktiv adgang som standard og lagdelte kontroller er indbygget i produktarkitektur, standardopsætning og drift — i overensstemmelse med ISO 27001 og CIS Controls.

Nedenfor redegøres for, hvordan de efterspurgte designmønstre er indtænkt med konkrete eksempler fra Systemet.

### Economy of mechanism (enkelhed i mekanisme)

Princippet om enkelhed reducerer angrebsfladen ved at holde sikkerhedsmekanismer fokuserede og gennemskuelige.

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Centraliseret autentificering** | AuthProxy håndterer autentificering og autorisation for integrationskald — ét kontrolleret indgangspunkt i stedet for mange parallelle adgangsveje |
| **Standardiseret integrationslag** | SIF (Software Innovation Framework) giver et fælles, dokumenteret API-lag med strukturerede fejlmeddelelser og sporbarhed |
| **Ingen bagdøre** | Tilgang til sager og dokumenter styres udelukkende via rettighedsmatrix og radtilladelser; der findes ingen skjult mekanisme, der giver Brugere adgang uden eksplicit tildeling |
| **Fokuseret sikkerhedsarkitektur** | Kryptering (TLS/AES-256), RBAC og tenant-isolation implementeres gennem veldefinerede komponenter frem for ad hoc-løsninger |

**Eksempel:** En ekstern integration autentificeres via AuthProxy og SIF. Adgangen begrænses til de API-operationer og datafelter, Kunden har konfigureret — uden alternative adgangsveje udenom de etablerede kontroller.

### Least privilege (mindst privilegium)

Brugere og systemkomponenter får kun den adgang, der er nødvendig for deres opgave.

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Rettighedsmatrix og radtilladelser** | Standard rettighedsmatrix skelner mellem læse- og redigeringsadgang; Brugere ser kun sager og dokumenter, de er eksplicit tildelt via adgangsgrupper |
| **Rollebaseret adgang (RBAC)** | Funktioner som kassation, permanent sletning, overstregning og administratoropsætning kræver særskilte roller og tilladelser |
| **Drift og administration** | Adgang til produktionsmiljøet begrænses til autoriseret driftspersonale med personlige konti, MFA og regelmæssig review af rettigheder |
| **Integrationer** | Integrationsbrugere og API-adgange konfigureres med minimale nødvendige rettigheder og kan filtreres per integration |

**Eksempel:** En sagsbehandler kan læse og redigere sager inden for sin adgangsgruppe, men kan ikke udføre kassation, ændre rettighedsmatrix eller tilgå administrator-modulet uden særskilt tildeling.

### Defense in depth (forsvar i dybden)

Flere uafhængige sikkerhedslag beskytter data og funktionalitet, så et enkelt lag ikke er en enkelt fejlkilde.

| Lag | Eksempel i praksis |
|-----|-------------------|
| **Identitet** | Entra ID-integration med SSO og MFA |
| **Netværk** | TLS 1.2+ for al ekstern kommunikation; netværkssegmentering og firewall i cloud-drift |
| **Applikation** | RBAC, rettighedsmatrix, tilgangskoder og adgangskoder |
| **Data** | AES-256-kryptering i hvile; Azure Key Vault til nøgleforvaltning |
| **Isolation** | Tenant-isolation med separat database, filcontainer og applikationskontekst per Kunde |
| **Overvågning** | Audit trail, admin-audit, central logning og 24/7 overvågning via Cloud Operations |
| **Test og vedligehold** | Sårbarhedsscanning, patch management og årlige penetratonstests |

**Eksempel:** Selv om en Bruger er autentificeret via Entra ID, skal vedkommende også opfylde rettighedsmatrix, adgangsgruppe og tilgangskode for det konkrete dokument — og alle forsøg logges i audit trail.

### Failing securely (sikker fejlhåndtering)

Ved fejl eller afvigelse bevarer Systemet sikkerheden og eksponerer ikke data eller funktioner unødig.

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Autentificeringsfejl** | Mislykkede loginforsøg giver afvisning uden adgang til data; forsøg logges |
| **Autorisation afvises som standard** | Manglende eller utilstrækkelig adgang medfører afvisning — Brugeren får ikke delvis adgang til beskyttede objekter |
| **Transaktionel databehandling** | Databaseændringer gennemføres atomart; ved fejl rulles ændringen tilbage frem for at efterlade inkonsistente data |
| **Integrationsfejl** | SIF API returnerer strukturerede fejlmeddelelser med CorrelationId til sporing uden at lække følsomme oplysninger |
| **Immutable logning** | Aktivitets- og sikkerhedslogs kopieres til beskyttet lagring, så operatører ikke kan slette spor efter hændelser |

**Eksempel:** En Bruger uden redigeringsadgang forsøger at ændre et journaliseret dokument. Systemet afviser handlingen, ændrer intet i databasen og logger forsøget — der sker ingen utilsigtet eksponering eller delvis ændring.

### Separation of privilege (adskillelse af privilegier)

Kritiske handlinger kræver adskilte rettigheder og roller — ingen enkelt Bruger har alene fuld kontrol over følsomme operationer.

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Adskilte administratorroller** | Brugeradministration, arkivadministration og systemkonfiguration kan delegeres til forskellige roller med begrænset overlap |
| **Man-in-the-loop ved sletning** | Kassation og permanent sletning kræver autoriseret Bruger, review og godkendelse via rapport — sletningen udføres først efter eksplicit initiering |
| **Adskillelse af drift og kunde** | Kundens sagsbehandlere administrerer adgang inden for Systemet; Leverandørens driftspersonale har adskilte tekniske rettigheder med audit og MFA |
| **Segregation of duties i drift** | Adgangsrettigheder til produktionsmiljø gennemgås regelmæssigt; dekryptering af filer kræver flere nøgler og er begrænset til få tekniske personer |

**Eksempel:** En arkivar kan forberede kassation via rapport, men den autoriserede kassationsrolle skal godkende og initierer sletningen — samme person har typisk ikke begge rettigheder, medmindre Kunden eksplicit har konfigureret det.

### Least common mechanism (mindst fælles mekanisme)

Delt infrastruktur og fælles mekanismer minimeres, så fejl eller kompromittering hos én Kunde ikke påvirker andre.

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Tenant-isolation** | Hver Kunde har isoleret database, filcontainer og applikationskontekst |
| **Ingen fælles brugerkonti** | Der findes ikke fælles administratoradgangskoder; alle Brugere og driftspersonale anvender personlige konti |
| **Adskilt backup og nøgler** | Sikkerhedskopier og krypteringsnøgler holdes adskilt per Kunde/abonnement |
| **Integrationsfiltrering** | Hver integration konfigureres separat med egne rettigheder og datafiltre via SIF |

**Eksempel:** Kundens data lagres i egen database og filcontainer med egne adgangsnøgler. En anden Kundes miljø deles ikke — fejl eller misbrug i ét tenant påvirker ikke Kundens data.

### Promoting privacy (fremme af databeskyttelse)

Security by default understøtter databeskyttelse som standard — ikke som tilvalg (jf. krav 5.3.7.2).

| Foranstaltning | Eksempel i praksis |
|----------------|-------------------|
| **Restriktiv standardadgang** | Brugere har som udgangspunkt ingen adgang til sager og dokumenter, før de tildeles via adgangsgrupper og rettighedsmatrix |
| **Dataminimering** | Kunden konfigurerer obligatoriske felter og integrationer, så kun nødvendige personoplysninger indsamles |
| **Kryptering som standard** | Personoplysninger krypteres i transit og hvile uden at Kunden skal aktivere det manuelt |
| **360° Archive Inspector** | Understøtter proaktiv identifikation af personoplysninger (i drift i Norge; tilpasses til det danske marked) |
| **Overstregning og anonymisering** | Følsomme oplysninger kan afskærmes som standard i aktindsigtsflow og arkivadministration |

**Eksempel:** En ny Bruger oprettes via Entra ID med minimal rolle. Vedkommende kan logge ind, men ser ingen sager, før Kunden har tildelt adgangsgruppe og rettigheder — databeskyttelse er standard, ikke eftermontering.

### Samlet effekt

Security-by-default-principperne er indtænkt i Systemets standardopsætning, adgangsmodel og drift. Kunden får et system, hvor sikker konfiguration er udgangspunktet, og hvor yderligere adgang kun gives eksplicit og sporbar.

Detaljer om CIA, databeskyttelse, autentifikation og logning uddybes i krav 5.3.7.1, 5.3.7.2 og 5.3.7.1.x.
