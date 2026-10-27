# Builds translated 360 Flow demo decision (vedtak) document templates from Prosess_vedtak.dotm (Norwegian source).
# Only visible text / GBS display labels are replaced; VBA, structure, and field logic unchanged.

$ErrorActionPreference = 'Stop'
$srcOriginal = 'C:\Users\MortenJensen\Downloads\Prosess_vedtak.dotm'
if (-not (Test-Path -LiteralPath $srcOriginal)) { throw "Source not found: $srcOriginal" }
$src = Join-Path $env:TEMP 'prosess_vedtak_source.dotm'
Copy-Item -LiteralPath $srcOriginal -Destination $src -Force
$outDir = $PSScriptRoot
$utf8 = New-Object System.Text.UTF8Encoding $false

$xmlFiles = @(
    'word/document.xml',
    'word/footer1.xml',
    'word/footer2.xml',
    'word/glossary/document.xml',
    'customXml/item4.xml'
)

function Apply-Map([string]$text, [hashtable]$map) {
    foreach ($key in ($map.Keys | Sort-Object { $_.Length } -Descending)) {
        $text = $text.Replace($key, $map[$key])
    }
    return $text
}

function Fix-StillingstittelSplit([string]$text, [string]$replacement) {
    $pattern = '(<w:t[^>]*>)S(</w:t></w:r>[\s\S]{0,800}?<w:t[^>]*>)tillingstittel(</w:t>)'
    return [regex]::Replace($text, $pattern, "`${1}$replacement`${3}")
}

# Shared labels (keep in sync with Build-TranslatedTemplates.ps1)
$common = @{
    en = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'The document is electronically approved and has no signature'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Click or tap here to enter text.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Click or tap to enter a date.'
        'Unntatt offentlighet paragraf' = 'Exempt from public disclosure, section'
        'Saksbehandlers navn' = 'Case handler''s name'
        'Postnummer Poststed' = 'Postcode City'
        'Mottakers navn' = 'Recipient''s name'
        'Dokumenttittel' = 'Document title'
        'Kontaktperson' = 'Contact person'
        'Stillingstittel' = 'Job title'
        'Mottakerliste' = 'Recipient list'
        'Godkjenner' = 'Approver'
        'Saksbehandler' = 'Case handler'
        'Deres ref.' = 'Your ref.'
        'Deres ref' = 'Your ref'
        'Med hilsen' = 'Yours sincerely'
        'Besøksadresse' = 'Visiting address'
        'Besøkadresse' = 'Visiting address'
        'Postadresse' = 'Postal address'
        'MIN VIRKSOMHET' = 'MY ORGANISATION'
        'VIRKSOMHET' = 'ORGANISATION'
        'Saksnummer' = 'Case number'
        'Dokdato' = 'Doc. date'
        'Doknr' = 'Doc. no.'
        'Telefon' = 'Telephone'
        'Adresse' = 'Address'
        'E-post' = 'E-mail'
        'Org.nr' = 'Org. no.'
        'Orgnr' = 'Org. no.'
        'Poststed ' = 'City '
        'Poststed' = 'City'
        'og ' = 'and '
        'Vår ' = 'Our '
        'Vår ref.' = 'Our ref.'
        'Deres ' = 'Your '
        'Dato' = 'Date'
        'ref' = 'ref'
        'nummer' = 'number'
        'web' = 'web'
    }
    da = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Dokumentet er elektronisk godkendt og har ingen underskrift'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Klik eller tryk her for at skrive tekst.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Klik eller tryk for at indtaste en dato.'
        'Unntatt offentlighet paragraf' = 'Undtaget offentlighed, paragraf'
        'Saksbehandlers navn' = 'Sagsbehandlers navn'
        'Postnummer Poststed' = 'Postnummer By'
        'Mottakers navn' = 'Modtagers navn'
        'Dokumenttittel' = 'Dokumenttitel'
        'Kontaktperson' = 'Kontaktperson'
        'Stillingstittel' = 'Stillingstitel'
        'Mottakerliste' = 'Modtagerliste'
        'Godkjenner' = 'Godkender'
        'Saksbehandler' = 'Sagsbehandler'
        'Deres ref.' = 'Deres ref.'
        'Deres ref' = 'Deres ref'
        'Med hilsen' = 'Med venlig hilsen'
        'Besøksadresse' = 'Besøgsadresse'
        'Besøkadresse' = 'Besøgsadresse'
        'Postadresse' = 'Postadresse'
        'MIN VIRKSOMHET' = 'MIN VIRKSOMHED'
        'VIRKSOMHET' = 'VIRKSOMHED'
        'Saksnummer' = 'Sagsnummer'
        'Dokdato' = 'Dok.dato'
        'Doknr' = 'Dok.nr.'
        'Telefon' = 'Telefon'
        'Adresse' = 'Adresse'
        'E-post' = 'E-mail'
        'Org.nr' = 'CVR.nr.'
        'Orgnr' = 'CVR.nr.'
        'Poststed ' = 'By '
        'Poststed' = 'By'
        'og ' = 'og '
        'Vår ' = 'Vores '
        'Vår ref.' = 'Vores ref.'
        'Deres ' = 'Deres '
        'Dato' = 'Dato'
        'ref' = 'ref'
        'nummer' = 'nummer'
        'web' = 'web'
    }
    sv = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Dokumentet är elektroniskt godkänt och har ingen signatur'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Klicka eller tryck här för att skriva text.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Klicka eller tryck för att ange ett datum.'
        'Unntatt offentlighet paragraf' = 'Undantaget offentlighet, paragraf'
        'Saksbehandlers navn' = 'Handläggarens namn'
        'Postnummer Poststed' = 'Postnummer Ort'
        'Mottakers navn' = 'Mottagarens namn'
        'Dokumenttittel' = 'Dokumenttitel'
        'Kontaktperson' = 'Kontaktperson'
        'Stillingstittel' = 'Befattning'
        'Mottakerliste' = 'Mottagarlista'
        'Godkjenner' = 'Godkänner'
        'Saksbehandler' = 'Handläggare'
        'Deres ref.' = 'Ert ref.'
        'Deres ref' = 'Ert ref'
        'Med hilsen' = 'Med vänlig hälsning'
        'Besøksadresse' = 'Besöksadress'
        'Besøkadresse' = 'Besöksadress'
        'Postadresse' = 'Postadress'
        'MIN VIRKSOMHET' = 'MIN ORGANISATION'
        'VIRKSOMHET' = 'ORGANISATION'
        'Saksnummer' = 'Diarienummer'
        'Dokdato' = 'Dok.datum'
        'Doknr' = 'Dok.nr'
        'Telefon' = 'Telefon'
        'Adresse' = 'Adress'
        'E-post' = 'E-post'
        'Org.nr' = 'Org.nr'
        'Orgnr' = 'Org.nr'
        'Poststed ' = 'Ort '
        'Poststed' = 'Ort'
        'og ' = 'och '
        'Vår ' = 'Vårt '
        'Vår ref.' = 'Vårt ref.'
        'Deres ' = 'Ert '
        'Dato' = 'Datum'
        'ref' = 'ref'
        'nummer' = 'nummer'
        'web' = 'web'
    }
    fi = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Asiakirja on hyväksytty sähköisesti eikä siinä ole allekirjoitusta'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Napsauta tai napauta tähän kirjoittaaksesi tekstin.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Napsauta tai napauta syöttääksesi päivämäärän.'
        'Unntatt offentlighet paragraf' = 'Salassapitosäännös, pykälä'
        'Saksbehandlers navn' = 'Käsittelijän nimi'
        'Postnummer Poststed' = 'Postinumero Postitoimipaikka'
        'Mottakers navn' = 'Vastaanottajan nimi'
        'Dokumenttittel' = 'Asiakirjan otsikko'
        'Kontaktperson' = 'Yhteyshenkilö'
        'Stillingstittel' = 'Tehtävänimike'
        'Mottakerliste' = 'Vastaanottajaluettelo'
        'Godkjenner' = 'Hyväksyjä'
        'Saksbehandler' = 'Käsittelijä'
        'Deres ref.' = 'Viitteenne'
        'Deres ref' = 'Viitteenne'
        'Med hilsen' = 'Ystävällisin terveisin'
        'Besøksadresse' = 'Käyntiosoite'
        'Besøkadresse' = 'Käyntiosoite'
        'Postadresse' = 'Postiosoite'
        'MIN VIRKSOMHET' = 'OMISTAVA ORGANISAATIO'
        'VIRKSOMHET' = 'ORGANISAATIO'
        'Saksnummer' = 'Asianumero'
        'Dokdato' = 'Asiakirjan pvm'
        'Doknr' = 'Asiakirjan nro'
        'Telefon' = 'Puhelin'
        'Adresse' = 'Osoite'
        'E-post' = 'Sähköposti'
        'Org.nr' = 'Y-tunnus'
        'Orgnr' = 'Y-tunnus'
        'Poststed ' = 'Postitoimipaikka '
        'Poststed' = 'Postitoimipaikka'
        'og ' = 'ja '
        'Vår ' = 'Meidän '
        'Vår ref.' = 'Meidän viite'
        'Deres ' = 'Teidän '
        'Dato' = 'Päivämäärä'
        'ref' = 'viite'
        'nummer' = 'numero'
        'web' = 'web'
    }
}

$vedtak = @{
    en = @{
        'e-post' = 'e-mail'
        'Vi gjør oppmerksom på følgende krav til dokumentasjon, uten at dette kan anses som en fullstendig oppramsing:' = 'We draw your attention to the following documentation requirements, without this being regarded as a complete list:'
        'Vi ber om at dere betaler gebyrer og avgifter (jf. fakturaer) innen fristen. Ved en eventuell klage må også gebyrer og avgifter betales.' = 'We ask that you pay fees and charges (cf. invoices) by the deadline. If you appeal, fees and charges must still be paid.'
        'Alle parter kan klage på vedtaket innen 3 uker. Se orientering nedenfor om rett til å klage på forvaltningsvedtak.' = 'All parties may appeal the decision within 3 weeks. See the information below on the right to appeal administrative decisions.'
        'Klagen skal sendes skriftlig til den som har fattet vedtaket. Angi vedtaket det klages over, den eller de endringer som ønskes og de grunner du vil føre for klagen. Dersom du klager så sent at det kan være uklart for oss om du har klaget i rett tid, må du også oppgi når du mottok denne meldingen.' = 'The appeal must be sent in writing to the person who made the decision. State the decision appealed against, the change(s) requested, and the grounds for the appeal. If you appeal so late that it may be unclear whether you appealed in time, you must also state when you received this notice.'
        'Forvaltningsloven §28. Klagefristen er 3 uker regnet fra den dagen da brevet kom fram til påført adressat. Det er tilstrekkelig at klagen er postlagt innen fristens utløp.' = 'Administrative Act § 28. The appeal deadline is 3 weeks from the day the letter was delivered to the addressee. It is sufficient that the appeal is posted before the deadline expires.'
        'Enkeltvedtak kan påklages til kommunen av en part eller annen med rettslig klageinteresse, jf.' = 'Individual decisions may be appealed to the municipality by a party or others with legal standing to appeal, cf.'
        'Orientering om rett til å klage på forvaltningsvedtak' = 'Information on the right to appeal administrative decisions'
        'Saksbehandling med begrunnelse for vedtak' = 'Case processing with grounds for the decision'
        'Vedtaket har følgende oppfølgingspunkter:' = 'The decision has the following follow-up points:'
        'Vedtaket har følgende vilkår:' = 'The decision has the following conditions:'
        'Gebyrer og videre oppfølging' = 'Fees and further follow-up'
        'Krav til dokumentasjon' = 'Documentation requirements'
        'Oppfølgingspunkter' = 'Follow-up points'
        'Gebyrer og avgifter' = 'Fees and charges'
        'Vedtak' = 'Decision'
        'Vilkår' = 'Conditions'
    }
    da = @{
        'e-post' = 'e-mail'
        'Vi gjør oppmerksom på følgende krav til dokumentasjon, uten at dette kan anses som en fullstendig oppramsing:' = 'Vi gør opmærksom på følgende krav til dokumentation, uden at dette kan anses for en fuldstændig opregning:'
        'Vi ber om at dere betaler gebyrer og avgifter (jf. fakturaer) innen fristen. Ved en eventuell klage må også gebyrer og avgifter betales.' = 'Vi beder om, at I betaler gebyrer og afgifter (jf. fakturaer) inden fristen. Ved en eventuel klage skal gebyrer og afgifter også betales.'
        'Alle parter kan klage på vedtaket innen 3 uker. Se orientering nedenfor om rett til å klage på forvaltningsvedtak.' = 'Alle parter kan klage over afgørelsen inden for 3 uger. Se orientering nedenfor om ret til at klage over forvaltningsafgørelser.'
        'Klagen skal sendes skriftlig til den som har fattet vedtaket. Angi vedtaket det klages over, den eller de endringer som ønskes og de grunner du vil føre for klagen. Dersom du klager så sent at det kan være uklart for oss om du har klaget i rett tid, må du også oppgi når du mottok denne meldingen.' = 'Klagen skal sendes skriftlig til den, der har truffet afgørelsen. Angiv den afgørelse, der klages over, den eller de ændringer, der ønskes, og de grunde, du vil føre for klagen. Klager du så sent, at det kan være uklart for os, om du har klaget rettidigt, skal du også angive, hvornår du modtog denne meddelelse.'
        'Forvaltningsloven §28. Klagefristen er 3 uker regnet fra den dagen da brevet kom fram til påført adressat. Det er tilstrekkelig at klagen er postlagt innen fristens utløp.' = 'Forvaltningsloven § 28. Klagefristen er 3 uger regnet fra den dag, brevet kom frem til adressaten. Det er tilstrækkeligt, at klagen er postlagt inden fristens udløb.'
        'Enkeltvedtak kan påklages til kommunen av en part eller annen med rettslig klageinteresse, jf.' = 'Enkeltafgørelser kan påklages til kommunen af en part eller andre med retlig klageinteresse, jf.'
        'Orientering om rett til å klage på forvaltningsvedtak' = 'Orientering om ret til at klage over forvaltningsafgørelser'
        'Saksbehandling med begrunnelse for vedtak' = 'Sagsbehandling med begrundelse for afgørelse'
        'Vedtaket har følgende oppfølgingspunkter:' = 'Afgørelsen har følgende opfølgingspunkter:'
        'Vedtaket har følgende vilkår:' = 'Afgørelsen har følgende vilkår:'
        'Gebyrer og videre oppfølging' = 'Gebyrer og videre opfølgning'
        'Krav til dokumentasjon' = 'Krav til dokumentation'
        'Oppfølgingspunkter' = 'Opfølgingspunkter'
        'Gebyrer og avgifter' = 'Gebyrer og afgifter'
        'Vedtak' = 'Afgørelse'
        'Vilkår' = 'Vilkår'
    }
    sv = @{
        'Vi gjør oppmerksom på følgende krav til dokumentasjon, uten at dette kan anses som en fullstendig oppramsing:' = 'Vi uppmärksammar följande krav på dokumentation, utan att detta kan anses som en fullständig förteckning:'
        'Vi ber om at dere betaler gebyrer og avgifter (jf. fakturaer) innen fristen. Ved en eventuell klage må også gebyrer og avgifter betales.' = 'Vi ber er att betala avgifter (jf. fakturor) inom fristen. Vid en eventuell överklagan ska avgifterna också betalas.'
        'Alle parter kan klage på vedtaket innen 3 uker. Se orientering nedenfor om rett til å klage på forvaltningsvedtak.' = 'Alla parter kan överklaga beslutet inom 3 veckor. Se informationen nedan om rätten att överklaga förvaltningsbeslut.'
        'Klagen skal sendes skriftlig til den som har fattet vedtaket. Angi vedtaket det klages over, den eller de endringer som ønskes og de grunner du vil føre for klagen. Dersom du klager så sent at det kan være uklart for oss om du har klaget i rett tid, må du også oppgi når du mottok denne meldingen.' = 'Överklagandet ska skickas skriftligt till den som fattat beslutet. Ange det beslut som överklagas, den eller de ändringar som önskas och de skäl du vill föra för överklagandet. Om du överklagar så sent att det kan vara oklart om du överklagat i rätt tid, ska du också ange när du mottog detta meddelande.'
        'Forvaltningsloven §28. Klagefristen er 3 uker regnet fra den dagen da brevet kom fram til påført adressat. Det er tilstrekkelig at klagen er postlagt innen fristens utløp.' = 'Förvaltningslagen § 28. Överklagandefristen är 3 veckor från den dag brevet kom fram till adressaten. Det räcker att överklagandet postläggs före fristens utgång.'
        'Enkeltvedtak kan påklages til kommunen av en part eller annen med rettslig klageinteresse, jf.' = 'Enskilda beslut kan överklagas till kommunen av en part eller annan med rättsligt överklagandeintresse, jfr.'
        'Orientering om rett til å klage på forvaltningsvedtak' = 'Information om rätten att överklaga förvaltningsbeslut'
        'Saksbehandling med begrunnelse for vedtak' = 'Handläggning med motivering för beslut'
        'Vedtaket har følgende oppfølgingspunkter:' = 'Beslutet har följande uppföljningspunkter:'
        'Vedtaket har følgende vilkår:' = 'Beslutet har följande villkor:'
        'Gebyrer og videre oppfølging' = 'Avgifter och vidare uppföljning'
        'Krav til dokumentasjon' = 'Krav på dokumentation'
        'Oppfølgingspunkter' = 'Uppföljningspunkter'
        'Gebyrer og avgifter' = 'Avgifter'
        'Vedtak' = 'Beslut'
        'Vilkår' = 'Villkor'
    }
    fi = @{
        'Vi gjør oppmerksom på følgende krav til dokumentasjon, uten at dette kan anses som en fullstendig oppramsing:' = 'Kiinnitämme huomion seuraaviin dokumentointivaatimuksiin, vaikka tätä ei voidakaan pitää täydellisenä luettelona:'
        'Vi ber om at dere betaler gebyrer og avgifter (jf. fakturaer) innen fristen. Ved en eventuell klage må også gebyrer og avgifter betales.' = 'Pyydämme teitä maksamaan maksut ja kulut (ks. laskut) määräajan mennessä. Valitukseen liittyen maksut on myös maksettava.'
        'Alle parter kan klage på vedtaket innen 3 uker. Se orientering nedenfor om rett til å klage på forvaltningsvedtak.' = 'Kaikki osapuolet voivat valittaa päätöksestä 3 viikon kuluessa. Katso alla olevat tiedot oikeudesta valittaa hallintopäätöksestä.'
        'Klagen skal sendes skriftlig til den som har fattet vedtaket. Angi vedtaket det klages over, den eller de endringer som ønskes og de grunner du vil føre for klagen. Dersom du klager så sent at det kan være uklart for oss om du har klaget i rett tid, må du også oppgi når du mottok denne meldingen.' = 'Valitus on lähetettävä kirjallisesti päätöksen tehneelle. Ilmoita valitettu päätös, pyydetyt muutokset ja valituksen perusteet. Jos valitat niin myöhään, ettei ole selvää, valititko ajallaan, ilmoita myös milloin sait tämän ilmoituksen.'
        'Forvaltningsloven §28. Klagefristen er 3 uker regnet fra den dagen da brevet kom fram til påført adressat. Det er tilstrekkelig at klagen er postlagt innen fristens utløp.' = 'Hallintolaki § 28. Valitusaika on 3 viikkoa päivästä, jona kirje saapui vastaanottajalle. Riittää, että valitus on postitettu ennen määräajan päättymistä.'
        'Enkeltvedtak kan påklages til kommunen av en part eller annen med rettslig klageinteresse, jf.' = 'Yksittäispäätöksestä voi valittaa kunnalle osapuoli tai muu, jolla on oikeudellinen valitusoikeus, ks.'
        'Orientering om rett til å klage på forvaltningsvedtak' = 'Tiedotus oikeudesta valittaa hallintopäätöksestä'
        'Saksbehandling med begrunnelse for vedtak' = 'Asian käsittely päätöksen perusteluineen'
        'Vedtaket har følgende oppfølgingspunkter:' = 'Päätöksessä on seuraavat seurantakohdat:'
        'Vedtaket har følgende vilkår:' = 'Päätöksessä on seuraavat ehdot:'
        'Gebyrer og videre oppfølging' = 'Maksut ja jatkoseuranta'
        'Krav til dokumentasjon' = 'Dokumentointivaatimukset'
        'Oppfølgingspunkter' = 'Seurantakohdat'
        'Gebyrer og avgifter' = 'Maksut ja kulut'
        'Vedtak' = 'Päätös'
        'Vilkår' = 'Ehdot'
    }
}

function Merge-Maps($a, $b) {
    $m = @{}
    foreach ($k in $a.Keys) { $m[$k] = $a[$k] }
    foreach ($k in $b.Keys) { $m[$k] = $b[$k] }
    return $m
}

$stillingByLang = @{
    en = 'Job title'
    da = 'Stillingstitel'
    sv = 'Befattning'
    fi = 'Tehtävänimike'
}

$outputs = @(
    @{ Lang = 'no'; File = 'prosess_vedtak.dotm'; Map = $null }
    @{ Lang = 'en'; File = 'process_decision.dotm'; Map = (Merge-Maps $common.en $vedtak.en) }
    @{ Lang = 'da'; File = 'proces_vedtagelse.dotm'; Map = (Merge-Maps $common.da $vedtak.da) }
    @{ Lang = 'sv'; File = 'process_beslut.dotm'; Map = (Merge-Maps $common.sv $vedtak.sv) }
    @{ Lang = 'fi'; File = 'prosessi_paatos.dotm'; Map = (Merge-Maps $common.fi $vedtak.fi) }
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

foreach ($out in $outputs) {
    $dest = Join-Path $outDir $out.File
    $work = Join-Path $env:TEMP ("dotm_vedtak_" + $out.Lang)
    if (Test-Path $work) { Remove-Item $work -Recurse -Force }
    New-Item -ItemType Directory -Path $work | Out-Null

    [System.IO.Compression.ZipFile]::ExtractToDirectory($src, $work)

    if ($null -ne $out.Map) {
        foreach ($rel in $xmlFiles) {
            $path = Join-Path $work $rel
            if (-not (Test-Path $path)) { continue }
            $content = [System.IO.File]::ReadAllText($path, $utf8)
            $content = Apply-Map $content $out.Map
            if ($stillingByLang.ContainsKey($out.Lang)) {
                $content = Fix-StillingstittelSplit $content $stillingByLang[$out.Lang]
            }
            [System.IO.File]::WriteAllText($path, $content, $utf8)
        }
    }

    if (Test-Path $dest) { Remove-Item $dest -Force }
    [System.IO.Compression.ZipFile]::CreateFromDirectory($work, $dest, [System.IO.Compression.CompressionLevel]::Optimal, $false)
    Write-Host "Created: $dest"
}

Write-Host 'Done.'
