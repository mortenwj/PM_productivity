# Tender Response — KK — Krav 5.2.18.1

| Field | Value |
|-------|-------|
| **Krav ID** | 5.2.18.1 |
| **Titel** | Rapportering og dataoverførsel |
| **Type** | IK — Informationskrav |
| **Tender** | KK (Københavns Kommune) |
| **Sprog** | Dansk |
| **Status** | Udkast (efter review) |
| **Genereret** | 2026-08-17 |

## Svar på krav 5.2.18.1

**Kundens krav:** Beskrivelse af, hvordan data kan (1) opstilles via løsningens rapporteringsværktøjer og (2) overføres til ekstern behandling i tredjeparts rapporteringsværktøj/datawarehouse.

**Leverandørens besvarelse:**

Systemet giver Kunden to komplementære veje til rapportering og ledelsesinformation (LIS): **indbyggede rapporteringsværktøjer** til daglig opfølgning og **Management Reporting API** til avanceret analyse, datawarehouse og BI-værktøjer som Power BI. De to niveauer supplerer hinanden og dækker både operative behov hos sagsbehandlere og strategiske styringsbehov hos ledelse.

---

### 1. Opstilling via Systemets egne rapporteringsværktøjer

#### Gemte søgninger og avanceret søgning

Brugere og administratorer kan oprette **gemte søgninger** med egne kriterier og gemme dem til genbrug — personligt, afdelingsvis eller globalt. Systemet understøtter:

- **Dynamiske søgninger** — løbende opdaterede resultatlister baseret på søgekriterier (fx igangværende sager, sager uden dokumenter, sager der nærmer sig frist)
- **Statiske søgninger** — faste resultatsæt til faste rapporteringsgrundlag og modtagerlister

Avanceret søgning giver adgang til et bredt sæt felter koblet til databasen. Kriterier kan kombineres med operatorer (større end, mindre end, er lig, ELLER) og datofelter med automatiske betingelser (fx «i dag», «i går»). Resultater kan filtreres på tværs af **sagstyper, tidsperioder, status, enhed, sagsbehandler** og andre parametre.

Søgeresultater kan:

- vises som **lister og diagrammer** direkte i brugergrænsefladen
- gemmes som **gemte søgninger** til løbende opfølgning (inkl. funktionen «Følg gemte søgninger»)
- placeres på **skrivebord/arbejdsflade** som webdele til løbende overblik

#### Indbyggede rapporter

Systemet indeholder **færdige rapporter** til ledelsesinformation, herunder rapport over **sagsbehandlingstid**. Lederen kan bestille rapport for valgt tidsrum, organisatorisk enhed og sagstype og få resultatet genereret med det samme — uden systemudvikling.

For byggesagsprocesser (Plan & Build 360°) kan processdata — herunder faser, deadlines, tidsstempler og status — følges op direkte i Systemet og via processpecifikke oversigter.

#### Eksport fra brugergrænsefladen

Søgeresultater og lister kan **eksporteres til Excel** direkte fra brugergrænsefladen. Administratorer kan desuden konfigurere **XML-eksport** via gemte søgninger til struktureret dataudtræk til videre bearbejdning.

Rapporter og søgeresultater kan dermed eksporteres til **gængse formater (Excel, CSV via Excel/XML)** til efterbehandling uden for Systemet.

#### Konfiguration uden systemudvikling

Gemte søgninger, rapporteringskriterier, webdele og eksportindstillinger oprettes og vedligeholdes af **Kundens brugere og administratorer** gennem Systemets standardgrænseflader — uden kodeudvikling. Det giver Kunden fleksibilitet til løbende at tilpasse rapporteringsgrundlag til egne behov.

---

### 2. Overførsel til ekstern behandling og datawarehouse

#### Management Reporting API

For avanceret LIS, tværgående analyse og integration med datawarehouse tilbyder Systemet **360° Management Reporting API** (fra version 6.7, tilgængelig på tværs af hostingtyper).

API'et giver Kunden mulighed for at hente data om **alle relevante entiteter** i Systemet — sager, dokumenter, kontakter, processdata, tidsstempler, statusværdier, fasemålinger og deadline-registreringer — via definerede datasæt.

**Arkitektur:**

```
Systemet (metadata og data)
    ↓  Management Reporting API (POST, JSON/XML)
Kundens dataplatform (datawarehouse/data lake)
    ↓  transformation
Tredjeparts BI (fx Power BI, Excel)
```

API'et returnerer data i **JSON eller XML** og understøtter:

- **Filtrering, sortering og relationer** mellem entiteter
- **Delta-load** — kun ændrede data siden sidste udtræk (typisk dagligt), filtreret på ModifiedDate
- **Komplekse forespørgsler** med datatyper og relationer på tværs af objekter

Kunden definerer hvilke datasæt og felter der returneres, og har fuld kontrol over rapportstruktur, datakvalitet og adgangsstyring i det eksterne miljø.

#### Integration med Power BI og datawarehouse

Flere kunder anvender den anbefalede tilgang:

1. Data hentes via Management Reporting API
2. Data lagres i Kundens **dataplatform** (data lake/datawarehouse)
3. Data transformeres til rapportvenligt format
4. Visualisering i **Power BI** eller tilsvarende BI-værktøj

Leverandøren kan levere **Power BI-skabeloner** og reference-datasæt. API'et er designet til integration med moderne BI-værktøjer og giver Kunden mulighed for skalerbare dashboards tilpasset roller og behov.

#### Automatisering og planlagte udtræk

Dataudtræk kan **automatiseres og planlægges** uden manuel indgriben:

- **Delta-load via API** — planlagt daglig (eller efter Kundens valg) hentes kun ændrede data
- **Process Engine-jobs (WorkUnits)** — planlagte baggrundsjobs kan eksportere data til BI-miljø (fx natlig kørsel)
- **Kundens integrationsplatform** — Azure Data Factory, Power Automate eller tilsvarende kan orkestrere planlagte API-kald og indlæsning i datawarehouse

Kunden aktiverer og planlægger jobs i Systemets administrator (Monitoring → Jobs) eller via egen integrationsplatform.

#### Dækning af efterspurgte parametre

Via Management Reporting API og/eller gemte søgninger kan Kunden foretage udtræk filtreret på tværs af:

| Parameter | Mekanisme |
|-----------|-----------|
| **Sagstyper** | Søgning, gemte søgninger, API-datasæt |
| **Tidsperioder** | Datofiltre i søgning og API (ModifiedDate, CreatedDate m.fl.) |
| **Igangværende sager** | Dynamiske gemte søgninger / API-filtre på status |
| **Servicemålsoverholdelse** | Processdata fra Plan & Build 360° + BI-dashboards |
| **Tidsregistreringer** | Data i Systemet eksporteres via søgning/API til BI |

For servicemål og tidsregistrering kombineres **indbygget visning i Systemet** (enkeltsag, lister) med **BI-rapporter** til tværgående ledelsesoverblik — jf. også krav 5.2.16.x og 5.2.17.x.

---

### Demonstration af positivt vægtede forhold

| Kundens ønske | Systemets understøttelse |
|---------------|-------------------------|
| Data præsenteres direkte i egne rapporteringsværktøjer | Gemte søgninger, diagrammer, lister, webdele, sagsbehandlingstidsrapport |
| Rapporter tilpasses af Kunden uden systemudvikling | Gemte søgninger, avanceret søgning, webdele og XML-eksport konfigureres i standardgrænsefladen |
| Eksport til Excel, CSV | Excel-eksport fra søgning; CSV via Excel eller API-data (JSON/XML → CSV) |
| Integration til Power BI og datawarehouse | Management Reporting API + dataplatform + Power BI-skabeloner |
| Udtræk på tværs af sagstyper, perioder og parametre | Avanceret søgning + API med filtrering og relationer |
| Automatiserede, planlagte udtræk | Delta-load, WorkUnit-jobs, Kundens integrationsplatform |

---

### Implementering og ansvar

Management Reporting API kræver, at Kunden (evt. med Leverandørens implementeringsbistand i etableringsfasen):

1. Definerer ønskede datasæt (metadata-mapping)
2. Opsætter API-endpoints i Systemets administrator
3. Etablerer dataplatform og integrationsflow mod BI-værktøj
4. Vedligeholder datasæt ved ændringer i datamodel

Leverandøren tilbyder **implementeringsvejledning, produktdokumentation og reference-datasæt**. Ved brug af Management Reporting API vil der typisk være behov for **sparring med Leverandøren** i etableringsfasen.

For daglig LIS og operative rapporter dækker Systemets **indbyggede værktøjer** behovet uden ekstern BI. For strategisk ledelsesinformation, servicemålsanalyse på tværs af kategorier og datawarehouse-integration supplerer **Management Reporting API** med fuld fleksibilitet.
