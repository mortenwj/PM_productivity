# UIM ESDH — Compliance mapping: MK-6

**Source:** `source/UIM ESDH Tender tool.xlsx` (sheet *Production Plan*)  
**Generated:** 2026-07-07  
**Responsible (tool):** Morten  
**Tool status:** `3. Not able to meet` · Not Started (0%)

---

## Requirement (verbatim)

**MK-6** · Bilag 1.b · Generelle krav · **Håndtering af sletteregler** · Mindstekrav · **Verify**

> ESDH-løsningen skal understøtte håndtering af sletteregler, herunder bevaringskoder, for både midlertidig og permanent sletning. ESDH-løsningen skal understøtte, at sletning alene kan foretages af Brugere med de nødvendige rettigheder, herunder at rettigheder til permanent sletning og midlertidig sletning kan adskilles. Sletteregler skal kunne anvendes på **alle Entiteter** i Løsningen.

**Internal comment (ADN):** *«Sletteregler for alle entiteter» — kan vi sige at vi har det på kontakter?*

---

## Executive summary

| Assessment | **Partial / gap on «alle Entiteter»** |
|------------|----------------------------------------|
| Tool rating | 3. Not able to meet |
| Working compliance | **Met / Partial** for arkivkernen (sag, dokument, fil); **Not met** for bred «alle entiteter»-fortolkning |
| Bid risk | **High** (Risk sheet: «No bid» / ny modul) |
| Recommended action | Afklar «Entiteter» med ordregiver; do **not** bruge MK-62 (kontaktsletning) som dækning for sletteregler |

---

## Sub-requirement decomposition

| # | Buyer sub-requirement | Draft compliance | Confidence | Notes |
|---|------------------------|------------------|------------|-------|
| 1 | Sletteregler inkl. bevaringskoder | **Met** (sag/dokument/fil) | Verified | Klassifikation → kassasjonskode + bevaringstid; administrator konfigurerer BK-plan |
| 2 | Midlertidig sletning | **Met** (primært filer) | Verified | «Midlertidig sletting» / soft delete; fil kan genskabes |
| 3 | Permanent sletning | **Met** (filer + metadata via purge) | Verified | Permanent slet fil / slet alt permanent; purge af sag/dokument-metadata |
| 4 | Sletning kun med rettigheder | **Met** | Verified | Rolle + rettighedsmatrix (Læs/Rediger/Slet); dedikerede brugerlister for disposal/purge |
| 5 | Adskil rettighed: midlertidig vs permanent | **Met / Partial** | Verified | Separate «Users who can perform disposal» vs «User who can perform purge»; indstilling *Delete File Permanently* skjuler permanent sletning for sagsbehandlere |
| 6 | Sletteregler på **alle Entiteter** | **Not met** (streng) · **Partial** (smal) | Lead | Stærkt på sag/dokument/fil; kontakter har sletning (MK-62) men **ikke** bevaringskode/sletteregel-model; øvrige entitetstyper uafklaret |

---

## Evidence ledger

| Claim | Source | Type |
|-------|--------|------|
| Bevarings-/kassasjonsregler via klassifikation på sag, dokument, fil | HSØ Bilag 2 (kassasjon/bevaring); Ratatoskr *Disposal*, *Retention (Disposal)* | Verified |
| Tre kassasjonstyper: midlertidig, permanent fil, permanent fil+metadata | HSØ Bilag 2 § kassasjon | Verified |
| Kunden konfigurerer slettepolitikker i administrator (MK-7) | UIM tool · MK-7 = Fully met | Verified |
| Administrator konfigurerer slettepolitikker, bevaringskoder, klassifikationskoder (MK-117) | UIM tool · MK-117 = Fully met | Verified |
| Midlertidig + permanent sletning af sager (MK-14) | UIM tool · MK-14 = Fully met | Verified |
| Permanent sletning kan begrænses til arkivarrolle | Ratatoskr *File* → *Delete File Permanently* | Verified |
| Purge vs disposal er adskilte privilegier | Ratatoskr *Retention (Disposal)*, *Purge*, *Disposal* | Verified |
| Kontaktsletning med advisering (MK-62) — **ikke** sletteregler | UIM tool · MK-62 = Fully met (anderledes krav) | Verified |
| «Alle entiteter» — hull i produktet | UIM tool kommentar; Risk: unable to meet | Lead |

---

## Related requirements (UIM)

| Req ID | Title | Can meet | Relevance to MK-6 |
|--------|-------|----------|-------------------|
| MK-5 | Anmodninger fra registrerede (indsigt/slet/berigtigelse) | Fully met | GDPR-proces; supplerer ikke sletteregler på alle entiteter |
| MK-7 | Opsætning af slettepolitikker | Fully met | Kundekonfiguration i admin — overlapper MK-6 delkrav 1 |
| MK-117 | Slettepolitikker (administrator) | Fully met | Bevaringskoder + klassifikation — overlapper MK-6 delkrav 1 |
| MK-14 | Sletning af sager | Fully met | Midlertidig/permanent på sagsniveau |
| MK-62 | Sletning af kontakter | Fully met | **Ikke** evidens for sletteregler/bevaringskoder på kontakter |

---

## Gap analysis

### What is strong

Public 360° / eArchive 360° har en moden **disposal/retention**-model for **sager, dokumenter og filer**:

- Bevaringskoder og bevaringstid arves fra klassifikation (BK-plan).
- Kassasjon initieres manuelt af autoriserede brugere; udførelse via jobs med log.
- **Midlertidig** vs **permanent** sletning er eksplicit (soft delete vs permanent fil vs permanent alt).
- **Rettighedsadskillelse:** disposal-brugere, purge-brugere, og skjulning af «slet permanent» for sagsbehandlere.

Dette understøtter MK-7 og MK-117, som begge er «Fully met» i værktøjet.

### Where MK-6 breaks

Kravets sidste sætning — **«Sletteregler skal kunne anvendes på alle Entiteter i Løsningen»** — er bredere end arkivkernen:

| Entitetstype | Sletteregel / bevaringskode | Vurdering |
|--------------|----------------------------|-----------|
| Sag | Ja (klassifikation, kassasjon, purge) | Met |
| Dokument / journalpost | Ja | Met |
| Fil | Ja (disposal-typer) | Met |
| Kontakt | Sletning + soft delete (API); **ikke** samme sletteregel-model | **Gap** — MK-62 dækker andet krav |
| Aktivitet, projekt, opgave, skrivebord, … | Ikke dokumenteret som samme model | **Ukendt / sandsynlig gap** |

ADN-spørgsmålet (*«kan vi sige at vi har det på kontakter?»*) bør besvares **nej** for MK-6: MK-62 handler om advisering ved kontaktsletning, ikke bevaringskoder og midlertidig/permanent sletteregel på alle entiteter.

### Tool / risk position

- **Production Plan:** `3. Not able to meet`
- **Risk Management:** Severity High · «We are unable to meet requirement» · Mitigation: «We build a new module» · Decision: **No bid**
- **Cost Drivers:** High severity · included in pricing = Yes (placeholder)

---

## Draft compliance statement (Verify — Danish)

*Til brug hvis I vælger «Met / Partial» og afklarer entitetsomfang med køber. Tilpas ikke til «Fully met» uden beslutning om «alle Entiteter».*

> **MK-6 — Håndtering af sletteregler**  
> Løsningen understøtter sletteregler og bevaringskoder for arkivrelaterede entiteter (sager, dokumenter og filer). Bevaringskode og bevaringstid konfigureres af Administrator i klassifikationssystemet og anvendes automatisk ved klassificering; kassasjonsdato beregnes ved sagens afslutning. Kunden kan selv konfigurere slettepolitikker og standardværdier i 360° Administrator (jf. MK-7 og MK-117).
>
> Sletning kan kun udføres af brugere med de nødvendige rettigheder. Løsningen skelner mellem midlertidig sletning (soft delete, hvor filen kan genskabes) og permanent sletning af fil og/eller metadata. Rettigheder til permanent sletning kan begrænses til udvalgte roller (fx arkivar), mens øvrige brugere kun kan midlertidigt slette eller slette uden permanent fjernelse — styret via rettighedsmatrix og administratorindstillinger for disposal og purge.
>
> **Afgrænsning:** Sletteregler i ovenstående forstand gælder arkivprocessens kernentiteter (sag, dokument, fil). Kontakter og øvrige støtteentiteter håndteres med særskilte sletnings- og deaktiveringsfunktioner (jf. MK-62). Hvis Ordregiver med «alle Entiteter» forstår en entydig sletteregel-model på samtlige objekttyper i løsningen, bedes det præciseres i en skriftlig afklaring.

---

## Recommended next actions

1. **Buyer clarification (prioritet):** Hvilke «Entiteter» skal have bevaringskode + midlertidig/permanent sletteregel? Er kontakter, aktiviteter, projekter, opgaver, skrivebords-elementer inkluderet?
2. **Internal alignment:** Reconcile tool «Not able to meet» / Risk «No bid» med produktteam — er gap reelt eller konservativ vurdering?
3. **Do not conflate** MK-62 (kontaktsletning) med MK-6 (sletteregler alle entiteter).
4. **Verify one-liner** (hvis Met/Partial accepteres): peg på MK-7 + MK-117 + disposal/purge-dokumentation; undgå «vedlagte bilag» uden fil i `source/`.
5. **Morten:** Ejer Verify-svar; koordinér med Anton (MK-7, MK-117, MK-14) før endelig compliance-klassifikation.

---

## Bid decision hook

| Scenario | Compliance label | Bid implication |
|----------|------------------|-----------------|
| «Alle Entiteter» = sag + dokument + fil | **Met** | Kan harmoniseres med MK-7/MK-117; opdatér tool fra 3 → 1 |
| «Alle Entiteter» = inkl. kontakter m.fl. | **Not met** | Behold tool-rating; eskalér commitment / no-bid |
| Afventer svar | **Clarify** | Foreslå spørgsmål i Q&A-runde |
