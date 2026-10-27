# Builds translated 360 Flow demo document templates from prosess_mangelbrev (Norwegian source).
# Only visible text / GBS display labels are replaced; VBA, structure, and field logic unchanged.

$ErrorActionPreference = 'Stop'
$srcOriginal = 'C:\Users\MortenJensen\Downloads\prosess_mangelbrev_020626.dotm'
$src = Join-Path $env:TEMP 'prosess_mangelbrev_source.dotm'
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

# Norwegian source strings (longest / most specific first when applied via length sort)
$maps = @{
    en = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'The document is electronically approved and has no signature'
        'Frist for innsendelse av tilleggsinformasjon:' = 'Deadline for submission of additional information:'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Click or tap here to enter text.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Click or tap to enter a date.'
        'Henvendelser kan gjøres til sa' = 'Inquiries can be made to the '
        'ksbehandler ' = 'case handler '
        'Mangler ved søknaden ' = 'Deficiencies in the application '
        'Unntatt offentlighet paragraf' = 'Exempt from public disclosure, section'
        ' som kan treffes på telefon ' = ' who can be reached by telephone '
        ' ved alle henvendelser.' = ' for all inquiries.'
        '. Vennligst oppgi saksnummer ' = '. Please provide the case number '
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
        'og ' = 'and '
        'Vår ' = 'Our '
        'Deres ' = 'Your '
        'Dato' = 'Date'
    }
    da = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Dokumentet er elektronisk godkendt og har ingen underskrift'
        'Frist for innsendelse av tilleggsinformasjon:' = 'Frist for indsendelse af supplerende oplysninger:'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Klik eller tryk her for at skrive tekst.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Klik eller tryk for at indtaste en dato.'
        'Henvendelser kan gjøres til sa' = 'Henvendelser kan rettes til '
        'ksbehandler ' = 'sagsbehandler '
        'Mangler ved søknaden ' = 'Mangler ved ansøgningen '
        'Unntatt offentlighet paragraf' = 'Undtaget offentlighed, paragraf'
        ' som kan treffes på telefon ' = ' som kan træffes på telefon '
        ' ved alle henvendelser.' = ' ved alle henvendelser.'
        '. Vennligst oppgi saksnummer ' = '. Angiv venligst sagsnummer '
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
        'og ' = 'og '
        'Vår ' = 'Vores '
        'Deres ' = 'Deres '
        'Dato' = 'Dato'
    }
    sv = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Dokumentet är elektroniskt godkänt och har ingen signatur'
        'Frist for innsendelse av tilleggsinformasjon:' = 'Frist för inlämning av kompletterande information:'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Klicka eller tryck här för att skriva text.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Klicka eller tryck för att ange ett datum.'
        'Henvendelser kan gjøres til sa' = 'Frågor kan ställas till '
        'ksbehandler ' = 'handläggare '
        'Mangler ved søknaden ' = 'Brister i ansökan '
        'Unntatt offentlighet paragraf' = 'Undantaget offentlighet, paragraf'
        ' som kan treffes på telefon ' = ' som kan nås per telefon '
        ' ved alle henvendelser.' = ' vid alla förfrågningar.'
        '. Vennligst oppgi saksnummer ' = '. Vänligen ange diarienummer '
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
        'og ' = 'och '
        'Vår ' = 'Vårt '
        'Deres ' = 'Ert '
        'Dato' = 'Datum'
    }
    fi = @{
        'Dokumentet er elektronisk godkjent og har ingen signatur' = 'Asiakirja on hyväksytty sähköisesti eikä siinä ole allekirjoitusta'
        'Frist for innsendelse av tilleggsinformasjon:' = 'Määräaika lisätietojen toimittamiselle:'
        'Klikk eller trykk her for å skrive inn tekst.' = 'Napsauta tai napauta tähän kirjoittaaksesi tekstin.'
        'Klikk eller trykk for å skrive inn en dato.' = 'Napsauta tai napauta syöttääksesi päivämäärän.'
        'Henvendelser kan gjøres til sa' = 'Yhteydenotot voi tehdä '
        'ksbehandler ' = 'käsittelijälle '
        'Mangler ved søknaden ' = 'Puutteet hakemuksessa '
        'Unntatt offentlighet paragraf' = 'Salassapitosäännös, pykälä'
        ' som kan treffes på telefon ' = ' joka tavoitetaan puhelimitse '
        ' ved alle henvendelser.' = ' kaikissa yhteydenotoissa.'
        '. Vennligst oppgi saksnummer ' = '. Ilmoittakaa asianumero '
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
        'og ' = 'ja '
        'Vår ' = 'Meidän '
        'Deres ' = 'Teidän '
        'Dato' = 'Päivämäärä'
    }
}

$stillingByLang = @{
    en = 'Job title'
    da = 'Stillingstitel'
    sv = 'Befattning'
    fi = 'Tehtävänimike'
}

$outputs = @(
    @{ Lang = 'no'; File = 'prosess_mangelbrev.dotm'; Map = $null }
    @{ Lang = 'en'; File = 'process_deficiency_letter.dotm'; Map = $maps.en }
    @{ Lang = 'da'; File = 'proces_mangelbrev.dotm'; Map = $maps.da }
    @{ Lang = 'sv'; File = 'process_bristbrev.dotm'; Map = $maps.sv }
    @{ Lang = 'fi'; File = 'prosessi_puutekirje.dotm'; Map = $maps.fi }
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

foreach ($out in $outputs) {
    $dest = Join-Path $outDir $out.File
    $work = Join-Path $env:TEMP ("dotm_build_" + $out.Lang)
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
