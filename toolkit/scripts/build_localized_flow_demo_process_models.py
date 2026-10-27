"""Build DA/NO/SV/FI process model JSON from English 6.12 master (string replace)."""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEMO = REPO / "projects/process-platform/flow/manuscripts/Demo setup"
EN_FILE = DEMO / "Handle application with right of appeal (English).json"

# Longest keys first when applying (handled via sort by -len(key))
TRANSLATIONS: dict[str, dict[str, str]] = {
    "da": {
        "Process application with right of appeal": "Behandle ansøgning m. klageret",
        "Request for additional documentation - Significant deficiency": "Anmodning om supplerende dokumentation - Væsentlig mangel",
        "*Additional documentation requested - significant deficiency": "*Anmodning om supplerende dokumentation - væsentlig mangel",
        "*Additional documentation requested - minor deficiency": "*Supplerende oplysninger anmodet - mindre mangel",
        "Additional documentation requested - significant deficiency": "Supplerende dokumentation anmodet - væsentlig mangel",
        "Additional information requested - minor deficiency": "Supplerende oplysninger anmodet - mindre mangel",
        "Automatic confirmation of received application": "Automatisk bekræftelse af modtaget ansøgning",
        "Verify all checklist items are completed": "Verificer at alle tjeklistepunkter er udfyldt",
        "Register/update date for received application": "Registrer/opdater dato for modtaget ansøgning",
        "Reminder deadline before case is closed": "Påmindelsesfrist før sagen afsluttes",
        "Write email - Obtain information - minor deficiency": "Skriv e-mail - Indhent oplysninger - mindre mangel",
        "Register date - Application complete": "Registrer dato - Ansøgning komplet",
        "Additional information received": "Modtaget supplerende oplysninger",
        "Additional documentation received": "Modtaget supplerende dokumentation",
        "Case processing completed": "Sagsbehandling afsluttet",
        "Complete application": "Komplet ansøgning",
        "Application completed": "Ansøgning komplet",
        "*Decision made": "*Afgørelse truffet",
        "Appeal deadline": "Klagefrist",
        "Appeal processing": "Klagebehandling",
        "Appeal received": "Klage modtaget",
        "Application received": "Ansøgning modtaget",
        "Review application": "Kontroller ansøgning",
        "Decision made": "Afgørelse truffet",
        "Close case processing": "Afslut sagsbehandling",
        "Write letter - Application received": "Skriv brev - Ansøgning modtaget",
        "Write email - Application received": "Skriv e-mail - Ansøgning modtaget",
        "Write letter - Decision": "Skriv brev - Afgørelse",
        "Write letter - Significant deficiency": "Skriv brev - Væsentlig mangel",
        "Write letter - Case is being closed": "Skriv brev - Sagen afsluttes",
        "Write letter - Appeal received": "Skriv brev - Klage modtaget",
        "Receipt for application": "Kvittering for ansøgning",
        "Reminder - Significant deficiency": "Påmindelse - Væsentlig mangel",
        "Decision": "Afgørelse",
        "Case is closed": "Sagen er afsluttet",
        "Application": "Ansøgning",
    },
    "no": {
        "Process application with right of appeal": "Behandle søknad m/klagerett",
        "Request for additional documentation - Significant deficiency": "Forespørsel om tilleggsdokumentasjon - Vesentlig mangel",
        "*Additional documentation requested - significant deficiency": "*Tilleggsdokumentasjon etterspurt - vesentlig mangel",
        "*Additional documentation requested - minor deficiency": "*Tilleggsinformasjon etterspurt - mindre mangel",
        "Additional documentation requested - significant deficiency": "Tilleggsdokumentasjon etterspurt - vesentlig mangel",
        "Additional information requested - minor deficiency": "Tilleggsinformasjon etterspurt - mindre mangel",
        "Automatic confirmation of received application": "Automatisk bekreftelse på mottatt søknad",
        "Verify all checklist items are completed": "Verifiser at alle sjekklistepunkter er fullført",
        "Register/update date for received application": "Registrer/oppdater dato for mottatt søknad",
        "Reminder deadline before case is closed": "Påminnelsesfrist før saken avsluttes",
        "Write email - Obtain information - minor deficiency": "Skriv e-post - Innhent informasjon - mindre mangel",
        "Register date - Application complete": "Registrer dato - Søknad komplett",
        "Additional information received": "Mottatt tilleggsinformasjon",
        "Additional documentation received": "Tilleggsdokumentasjon mottatt",
        "Case processing completed": "Saksbehandling avsluttet",
        "Complete application": "Komplett søknad",
        "Application completed": "Søknad komplett",
        "*Decision made": "*Vedtak fattet",
        "Appeal deadline": "Klagefrist",
        "Appeal processing": "Klagebehandling",
        "Appeal received": "Mottatt klage",
        "Application received": "Mottatt søknad",
        "Review application": "Kontroller søknad",
        "Decision made": "Vedtak fattet",
        "Close case processing": "Avslutt saksbehandling",
        "Write letter - Application received": "Skriv brev - Mottatt søknad",
        "Write email - Application received": "Skriv e-post - Mottatt søknad",
        "Write letter - Decision": "Skriv brev - Vedtak",
        "Write letter - Significant deficiency": "Skriv brev - Vesentlig mangel",
        "Write letter - Case is being closed": "Skriv brev - Saken avsluttes",
        "Write letter - Appeal received": "Skriv brev - Mottatt klage",
        "Receipt for application": "Kvittering for søknad",
        "Reminder - Significant deficiency": "Påminnelse - Vesentlig mangel",
        "Decision": "Vedtak",
        "Case is closed": "Saken er avsluttet",
        "Application": "Søknad",
    },
    "sv": {
        "Process application with right of appeal": "Behandla ansökan med överklaganderätt",
        "Request for additional documentation - Significant deficiency": "Begäran om kompletterande handlingar - Väsentlig brist",
        "*Additional documentation requested - significant deficiency": "*Begäran om kompletterande handlingar - väsentlig brist",
        "*Additional documentation requested - minor deficiency": "*Begäran om kompletterande uppgifter - mindre brist",
        "Additional documentation requested - significant deficiency": "Begäran om kompletterande handlingar - väsentlig brist",
        "Additional information requested - minor deficiency": "Ytterligare uppgifter begärda - mindre brist",
        "Automatic confirmation of received application": "Automatisk bekräftelse av mottagen ansökan",
        "Verify all checklist items are completed": "Verifiera att alla checklistepunkter är slutförda",
        "Register/update date for received application": "Registrera/uppdatera datum för mottagen ansökan",
        "Reminder deadline before case is closed": "Påminnelsefrist innan ärendet avslutas",
        "Write email - Obtain information - minor deficiency": "Skriv e-post - Inhämta uppgifter - mindre brist",
        "Register date - Application complete": "Registrera datum - Ansökan komplett",
        "Additional information received": "Ytterligare information mottagen",
        "Additional documentation received": "Kompletterande handlingar mottagna",
        "Case processing completed": "Ärendebehandling avslutad",
        "Complete application": "Komplett ansökan",
        "Application completed": "Ansökan komplett",
        "*Decision made": "*Beslut fattat",
        "Appeal deadline": "Överklagandefrist",
        "Appeal processing": "Överklagandehantering",
        "Appeal received": "Överklagande mottaget",
        "Application received": "Ansökan mottagen",
        "Review application": "Granska ansökan",
        "Decision made": "Beslut fattat",
        "Close case processing": "Avsluta ärendebehandling",
        "Write letter - Application received": "Skriv brev - Ansökan mottagen",
        "Write email - Application received": "Skriv e-post - Ansökan mottagen",
        "Write letter - Decision": "Skriv brev - Beslut",
        "Write letter - Significant deficiency": "Skriv brev - Väsentlig brist",
        "Write letter - Case is being closed": "Skriv brev - Ärendet avslutas",
        "Write letter - Appeal received": "Skriv brev - Överklagande mottaget",
        "Receipt for application": "Kvitto på ansökan",
        "Reminder - Significant deficiency": "Påminnelse - Väsentlig brist",
        "Decision": "Beslut",
        "Case is closed": "Ärendet är avslutat",
        "Application": "Ansökan",
    },
    "fi": {
        "Process application with right of appeal": "Käsittele hakemus valitusoikeudella",
        "Request for additional documentation - Significant deficiency": "Pyyntö toimittaa lisäasiakirjoja - Olennainen puute",
        "*Additional documentation requested - significant deficiency": "*Pyyntö toimittaa lisäasiakirjoja - olennainen puute",
        "*Additional documentation requested - minor deficiency": "*Pyyntö toimittaa lisätietoja - vähäinen puute",
        "Additional documentation requested - significant deficiency": "Pyyntö toimittaa lisäasiakirjoja - olennainen puute",
        "Additional information requested - minor deficiency": "Lisätietoja pyydetty - vähäinen puute",
        "Automatic confirmation of received application": "Automaattinen vahvistus vastaanotetusta hakemuksesta",
        "Verify all checklist items are completed": "Varmista, että kaikki tarkistuslistan kohdat on tehty",
        "Register/update date for received application": "Rekisteröi/päivitä vastaanotetun hakemuksen päivämäärä",
        "Reminder deadline before case is closed": "Muistutuksen määräaika ennen asian sulkemista",
        "Write email - Obtain information - minor deficiency": "Kirjoita sähköposti - Hanki tiedot - vähäinen puute",
        "Register date - Application complete": "Rekisteröi päivämäärä - Hakemus valmis",
        "Additional information received": "Lisätiedot vastaanotettu",
        "Additional documentation received": "Lisäasiakirjat vastaanotettu",
        "Case processing completed": "Asian käsittely päättynyt",
        "Complete application": "Valmis hakemus",
        "Application completed": "Hakemus valmis",
        "*Decision made": "*Päätös tehty",
        "Appeal deadline": "Valitusmääräaika",
        "Appeal processing": "Valituskäsittely",
        "Appeal received": "Valitus vastaanotettu",
        "Application received": "Hakemus vastaanotettu",
        "Review application": "Tarkista hakemus",
        "Decision made": "Päätös tehty",
        "Close case processing": "Sulje asian käsittely",
        "Write letter - Application received": "Kirjoita kirje - Hakemus vastaanotettu",
        "Write email - Application received": "Kirjoita sähköposti - Hakemus vastaanotettu",
        "Write letter - Decision": "Kirjoita kirje - Päätös",
        "Write letter - Significant deficiency": "Kirjoita kirje - Olennainen puute",
        "Write letter - Case is being closed": "Kirjoita kirje - Asia suljetaan",
        "Write letter - Appeal received": "Kirjoita kirje - Valitus vastaanotettu",
        "Receipt for application": "Kuitti hakemuksesta",
        "Reminder - Significant deficiency": "Muistutus - Olennainen puute",
        "Decision": "Päätös",
        "Case is closed": "Asia on suljettu",
        "Application": "Hakemus",
    },
}

OUTPUT_FILES = {
    "da": "Behandle ansøgning m. klageret (Danish).json",
    "no": "Behandle søknad m_klagerett.json",
    "sv": "Behandla ansökan med överklaganderätt (Swedish).json",
    "fi": "Käsittele hakemus valitusoikeudella (Finnish).json",
}


def apply_map(text: str, mapping: dict[str, str]) -> str:
    for key in sorted(mapping, key=len, reverse=True):
        text = text.replace(key, mapping[key])
    return text


def sanity(text: str, lang: str, expected_title: str, forbidden: str) -> None:
    if expected_title not in text:
        raise SystemExit(f"{lang}: expected title missing: {expected_title}")
    if forbidden in text:
        raise SystemExit(f"{lang}: still contains English marker: {forbidden}")
    if "EmailMessageTemplateRecno1" not in text:
        raise SystemExit(f"{lang}: missing EmailMessageTemplateRecno1")
    if "EmailMessageTemplateRecno1" in text and ">#null#</argument>" not in text:
        raise SystemExit(f"{lang}: EmailMessageTemplateRecno1 should be #null#")


def main() -> None:
    en_text = EN_FILE.read_text(encoding="utf-8")
    if "EmailMessageTemplateRecno1" not in en_text:
        raise SystemExit("English master missing 6.12 email template argument")

    for lang, out_name in OUTPUT_FILES.items():
        out_path = DEMO / out_name
        translated = apply_map(en_text, TRANSLATIONS[lang])
        out_path.write_text(translated, encoding="utf-8")
        sanity(
            translated,
            lang,
            TRANSLATIONS[lang]["Process application with right of appeal"],
            "Process application with right of appeal",
        )
        print(f"Wrote {out_path.name}")



if __name__ == "__main__":
    main()
