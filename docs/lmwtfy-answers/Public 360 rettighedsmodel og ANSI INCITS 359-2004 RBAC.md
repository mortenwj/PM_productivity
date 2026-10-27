# Public 360° rettighetsmodell, forhåndskonfigurerte roller og ANSI INCITS 359-2004

Public 360° har et eget, rollebasert tilgangskontrollsystem (rettighetsmatrise, tilgangsgrupper, radtillatelser og tilgangskoder). Systemet støtter kundetilpasning, flere samtidige roller per bruker og dataavgrensing per sakstype. Det finnes ingen dokumentert samsvar med ANSI INCITS 359-2004 som formell standard; «RBAC» brukes i produktdokumentasjon i generell forstand, ikke som ANSI-sertifisering.

---

## Original Question

> Leverandøren bedes redegøre for Systemets rettighedsmodel for brugeradgange, som anvendes internt i Systemet, herunder hvilke funktionelle afgrænsninger, dataafgrænsninger og dataklassifikationer, som der kan opbygges roller af.
>
> Leverandøren bedes ligeledes oplyse, hvilke roller og rettigheder som Systemet er prækonfigureret med.
>
> Det vægtes positivt, at rettighedsmodellen:
> - muliggør kundespecifikke tilpasninger af autorisationer og roller i Systemet
> - muliggør at en Bruger kan tildeles flere samtidige roller
> - efterlever RBAC standarden jf. ANSI INCITS 359-2004
> - understøtter dataafgræsning på baggrund af sagstyper, f.eks. basert … *(teksten er avkortet i kravet)*

## Context

Typisk anbudskrav (dansk kommune/region) om intern tilgangsstyring i Public 360°. Evalueringskriteriene matcher det produktet faktisk kan levere på de fleste punkter, unntatt formell ANSI INCITS 359-2004-compliance. Svaret under kan brukes som grunnlag for leverandørens besvarelse.

---

## Findings

### 1. Rettighetsmodell (intern brukeradgang)

Public 360° bruker et **proprietært tilgangskontrollsystem** som er dokumentert internt på wiki og i admin-hjelp. Modellen bygger på disse lagene:

**A. Brukere og profiler**

- En «bruker» er en 360°-kontakt knyttet til en innlogging (`ct_contact` + `us_user`).
- Tilgang styres via **brukerprofiler**: kombinasjon av **rolle** og **avdeling** (organisasjonsenhet). Fra versjon 4.0 gjelder samme tilgangsnivå uavhengig av aktiv profil i øyeblikket.
- Kilden: https://wiki.software-innovation.com/wiki/Access_control (seksjon «Users»)

**B. Roller (funksjonelle avgrensninger)**

- Roller styrer **hvilke moduler og funksjoner** brukeren har tilgang til i 360° Administrator og webklient (f.eks. arkivadministrasjon, brukeradministrasjon, endpoint-konfigurasjon).
- Roller brukes også som **medlemskapskriterium** i tilgangsgrupper og i rettighetsmatrisen.
- Spesielle systemroller (f.eks. «All access», «Integration service user») omgår normal tilgangskontroll og skal ikke tildeles ordinære brukere.
- Kilden: https://wiki.software-innovation.com/wiki/Access_control (seksjon «Special user roles»)

**C. Tilgangsgrupper (dataavgrensing)**

- Tilgangsgrupper (`uag_accessgroup`) avgrenser **hvem som får tilgang til hvilke objekter** (saker, dokumenter, filer, aktiviteter, prosjekter).
- Medlemmer kan defineres som:
  - spesifikke kontakter
  - brukerroller
  - avdelinger
  - rolle innen avdeling
- Grupper kan være **statiske** (faste medlemmer) eller **dynamiske** (medlemskap oppdateres når roller/avdelinger endres).
- Typer: Assigned, Enterprise templates, System, System generated, Custom.
- Kilder:
  - https://wiki.software-innovation.com/wiki/Access_control (seksjon «Groups»)
  - https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/accessgrouptypes.htm

**D. Rettighetsmatrise / access matrix (autorisasjon per entitetstype)**

- Regler defineres per **entitet** og **undertype** (f.eks. sakstype, dokumentarkiv, kontaktdomene).
- Hver regel svarer på fire spørsmål:
  1. Hvem? (bruker, tilgangsgruppe eller token)
  2. Hvilket tilgangsnivå? (Les offentlig, Les, Rediger, Slett)
  3. Hvilke handlinger? (f.eks. vis fil, sett inn fil, gi rettigheter)
  4. Hvilket kriterium? (f.eks. saksstatus)
- Forhåndsdefinerte **access templates** kan knyttes til løsning/subsetup og sakstyper.
- Kilder:
  - https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/viewandconfigurecasepermissionspermissionstab.htm
  - https://wiki.software-innovation.com/wiki/Access_control (seksjoner «Access rules», «Insert Access», «How to add new entity to access control»)

**E. Radtillatelser (instansnivå)**

- Faktisk tilgang til et konkret objekt lagres i `urp_rowpermission`.
- Genereres automatisk ved opprettelse/oppdatering basert på rettighetsmatrise-regler.
- Ingen skjult «back door»: det som står i radtillatelser er det som gjelder (med unntak av revoke-regler).
- Tilgangsnivå avgjøres av **høyeste** matchende regel (Slett > Rediger > Les).
- Kilden: https://wiki.software-innovation.com/wiki/Access_control

**F. Dataklassifikasjoner (tilgangskoder / access codes)**

- **Tilgangskoder** (access codes) klassifiserer informasjon (f.eks. gradert, unntatt offentlighet, intern).
- Tilgangskoder arves og brukes sammen med rettighetsmatrise for å begrense hva brukere med f.eks. «les offentlig» kan se.
- **Tilgangsnivå** på filer kan settes separat; strengeste tilgangskode kan gjelde ved sammenslåing (f.eks. møtebok).
- Kilder:
  - https://wiki.software-innovation.com/wiki/Access_control (Read public, field filters)
  - https://help.360online.com/Release_information/Index.html#!Documents/fixesandimprovementsin360onlinemarch2025.htm (access code i møtebok-kontekst)

**G. Ytterligere avgrensningsdimensjoner**

- **Journalenhet** (journal unit): logisk inndeling av saker; brukes bl.a. for Registrar 2 / Document Controller.
- **Avdeling / organisasjonsenhet**: enterprise templates og profiltilknytning.
- **Dokumentarkiv / sakstype / kontaktdomene / prosjekttype / eiendomstype**: entitetsundertyper i tilgangskontroll.
- **Field filters**: kan skjule/erstatte metadata basert på brukerens rolle/avdeling.
- **Revoke-regler**: eksplisitt tilbakekall av tilgang for bruker/gruppe på enkeltobjekt.

---

### 2. Forhåndskonfigurerte roller og rettigheter

**Standard brukerroller** (fra admin-hjelp; noen krever feature setup/subsetup):

| Rolle | Typisk funksjonell avgrensning |
|-------|-------------------------------|
| Administrator | Maler, overvåking, autorisasjon, arkivadmin (unntatt visse deler), kodebord, import/eksport |
| User Administrator | Autorisasjon og brukeradministrasjon |
| Technical Administrator | Opprette/redigere endpoints (kombineres med Administrator) |
| Caseworker (Sagsbehandler) | Saksbehandling |
| Manager (Leder) | Ledelsesfunksjoner |
| Registrar (Arkivar) | Full tilgang til arkivsaker og dokumentarkiv; arkiv- og klassifikasjonssystem |
| Registrar 2 | Registrator begrenset til egen journalenhet |
| Board secretary | Styremøtefunksjoner (feature setup) |
| Employee | Business 360° (korrespondanse) |
| Document controller | Business 360° arkivtilgang |
| Process Manager | Prosessmodell-administrasjon (Process Platform) |

**Systemroller** (skal normalt ikke tildeles brukere):

- All access (21), Data Reader (14/23), Integration service user (24), System administrator (27), m.fl.

**Kodebekreftet liste** (`EnumSysrole` i core-bl):

Administrator_0, Registrar_1, Registrar2_2, Manager_3, Caseworker_4, Boardsecretary_5, Useradministrator_8, Datareader_14, Departmentadministrator_19, Allaccess_21, Guest_22, ServiceReader_23, ServiceAllAccess_24, ServicePublicAccess_25, TechnicalAdministrator_26, SystemAdministrator_27, ProcessManager_28

Kilde: https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Linq.Meta/Code.cs#L81875

**Forhåndskonfigurerte rettigheter (tilgangsnivå og handlinger)**

- Tilgangsnivå: Read public (-1), Read (1), Edit (3), Delete (4); spesialnivå Insert (2) og Deny for revoke.
- Handlinger (utdrag): View File (100), Insert File (101), Modify File (102), Insert Rev (103), Modify Rev (104), Insert Doc (105), Grant permissions (21).
- Forhåndsdefinerte **rettighetsmatriser** (access templates) følger med per løsning (Public 360°, Business 360°, land/oppsett).
- Kilde: https://wiki.software-innovation.com/wiki/Access_control

**Profil- og rolleinnstillinger**

- Hver rolle har forhåndsdefinerte **rolleverdier** for innstillinger (standard tilgangsgruppe ved opprettelse, distribusjonsrettigheter, journalenhet osv.).
- Prioritet: profilverdi > rolleverdi > global verdi.
- Kilde: https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/creatingandregistering360users.htm

---

### 3. Vurdering mot positive kriterier

#### 3.1 Kundespecifikke tilpasninger — **JA (sterkt)**

Kunden kan:

- opprette egne tilgangsgrupper og knytte dem til rettighetsmatrisen
- tilpasse/erstatte rettighetsmatriser per sakstype, dokumentarkiv osv.
- definere egne access templates (typisk via subsetup/konsulent)
- legge til kriterier i regler (inntil 4 per undertype, f.eks. saksstatus)
- mappe AD/Entra-grupper til roller og tilgangsgrupper (UserZync/AD Sync)
- konfigurere tilgangskoder og field filters

Kilder: wiki Access control; help access group authorization; creating users.

#### 3.2 Flere samtidige roller per bruker — **JA**

- Hver bruker har minst én **brukerprofil** (rolle + avdeling).
- **Flere profiler** kan legges til med ulike roller/avdelinger, gyldighetsperiode og valgfri journalenhet.
- Brukeren velger aktiv profil ved innlogging; tilgangsnivå er likt på tvers av profiler (fra v4.0).
- `RolesCsv` i session støtter flere roller i teknisk kontekst (integrasjon/test).

Kilde: https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/creatingandregistering360users.htm

#### 3.3 ANSI INCITS 359-2004 — **NEI (formell compliance)**

**Konklusjon:** Public 360° kan **ikke** dokumenteres som compliant med ANSI INCITS 359-2004.

**Funn:**

- Ingen referanse til INCITS 359-2004 i kildekode, wiki, help eller interne tenderutkast.
- «RBAC» i sikkerhetsdokumentasjon gjelder **Azure-abonnements-RBAC** for driftspersonell, ikke applikasjonens modell.
  - Kilde: https://wiki.software-innovation.com/wiki/360%C2%B0_Online_Security_Specifications_customer_version

**ANSI INCITS 359-2004 krever (forenklet):**

- **Core RBAC:** brukere, roller, permissions, sessions med role activation; globale user-role og permission-role-relasjoner.
- **Hierarchical RBAC:** rollearv (partial order).
- **Constrained RBAC:** Static/Dynamic Separation of Duty.
- **Symmetric RBAC:** (valgfri komponent).

**Public 360° avviker:**

| ANSI-krav | Public 360° |
|-----------|-------------|
| Globale permission→role-tilordninger | Regler i rettighetsmatrise + **instansbaserte radtillatelser** |
| Sessions med role activation | Brukerprofil/rolle i session; ikke ANSI-modell |
| Hierarchical RBAC | Ingen dokumentert rollearv (`uro_parent` e.l.) |
| Static/Dynamic SoD | Ikke innebygd i applikasjons-RBAC (SoD nevnes for drift/portaler) |
| Symmetric RBAC | Ikke funnet |

**Anbefalt formulering i anbud:** «Systemet implementerer rollebasert tilgangsstyring med brukerprofiler, tilgangsgrupper, rettighetsmatrise og radtillatelser. Dette er RBAC i praksis, men Public 360° har ikke formell sertifisering eller dokumentert samsvar med ANSI INCITS 359-2004.»

#### 3.4 Dataavgrensing på sakstyper — **JA**

- **Sak** er en access-controlled entitet med undertype **CaseType** (`ToCaseType`).
- Rettighetsmatrise og access templates kan knyttes per sakstype og subsetup.
- Kriterier (f.eks. saksstatus) kan variere tilgang innen samme sakstype.
- Enterprise templates kan begrense tilgang på avdelingsnivå per sakstype.
- Kilder:
  - https://wiki.software-innovation.com/wiki/Access_control (Insert Access / subtype Case → CaseType)
  - https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/viewandconfigurecasepermissionspermissionstab.htm

---

### 4. Utkast til leverandørbesvarelse (dansk)

**Kort svar til anbud:**

Systemets interne rettighedsmodel bygger på brugerprofiler (rolle + afdeling), adgangsgrupper, rettighedsmatrix og rættigheder på objektniveau (row permissions). Funktionelle afgrænsninger styres primært via roller og moduladgang. Dataafgrænsninger styres via adgangsgrupper, rettighedsmatrix og objektspecifikke tilladelser. Dataklassifikation understøttes via adgangskoder (access codes) og tilknyttede regler i rettighedsmatrixen.

Systemet leveres med standardroller (bl.a. Administrator, Sagsbehandler, Leder, Arkivar, Brugeradministrator) og foruddefinerede rettighedsmatrix-skabeloner tilpasset Public 360°. Kunden kan tilpasse autorisationer, oprette egne adgangsgrupper og konfigurere regler per sagstype.

En bruger kan tildeles flere profiler (flere roller/afdelingskombinationer) med individuelle gyldighedsperioder.

Rettighedsmodel understøtter dataafgrænsning baseret på sagstyper via entitetsundertype CaseType i adgangskontrolsystemet.

Vedr. ANSI INCITS 359-2004: Systemet anvender rollebaseret adgangskontrol, men er ikke certificeret eller dokumenteret som compliant med denne standard. Modellen afviger bl.a. ved instansbaserede tilladelser, adgangsgrupper og betingede matrixregler, som ikke er en del af INCITS referencemodellen.

---

## Documentation assessment

- **Status:** partially_documented
- **Explanation:** Rettighetsmodellen er godt dokumentert internt på wiki (Access control) og i admin-hjelp (brukerprofiler, tilgangsgrupper, rettighetsmatrise). Det finnes ingen kundevendt dokumentasjon som adresserer ANSI INCITS 359-2004, og «RBAC» brukes uten presisering av standard vs. generisk begrep.
- **Suggested documentation changes:**
  - Ny wiki-side eller seksjon under Access control: «Role-based access control model» som forklarer modellens byggeklosser og eksplisitt sier hva som ikke er ANSI INCITS 359-2004.
  - Utvid admin-hjelp «User profile roles» med tabell over systemroller som ikke skal tildeles brukere.
  - Tender/security FAQ: standard formulering for RBAC-spørsmål (praksis ja, ANSI-nei).

## Risks and Limitations

- **ANSI INCITS 359-2004:** Risiko for poengtrekk i anbud hvis kravet tolkes som formell compliance. Anbefal ærlig avklaring; ikke bruk «RBAC-compliant» uten forbehold.
- **Profil vs. session:** Fra v4.0 er tilgang likt uavhengig av aktiv profil; dette kan avvike fra forventning om «kun én rolle aktiv om gangen».
- **All access / service roles:** Feil tildeling skaper full datatilgang; må fremheves i implementeringsveiledning.
- **Rettighetsmatrise vs. radtillatelser:** Endring av matrix gjelder ikke eksisterende objekter før regenerering eller redigering (ytelses-/driftsmessig viktig).

## References

- https://wiki.software-innovation.com/wiki/Access_control
- https://wiki.software-innovation.com/wiki/360%C2%B0_Online_Security_Specifications_customer_version
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/userprofileroles.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/creatingandregistering360users.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/accessgrouptypes.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/accessgroupauthorization.htm
- https://help.360online.com/6.8.0000/SIAdminHelp/1033/HH_Start.htm#!Documents/viewandconfigurecasepermissionspermissionstab.htm
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Linq.Meta/Code.cs#L81875
- https://github.com/te-industry-public360/core-bl/blob/master/Source/si-bl-core-build/SI.Biz.Core/Security/SecurityCore.cs
- https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/ANSI+INCITS+359-2004.pdf
