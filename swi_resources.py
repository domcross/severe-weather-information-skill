'''
List of service for Severe Weather Information skill

taken from following resources as of 2019-08-13:
https://severe.worldweather.wmo.int/v2/sources.html
https://alerting.worldweather.org/atom.xml
http://meteoalarm.eu/ATOM/root.xml

Some services were excluded for one or more of the following reasons:
- providing test information only
- use not properly signed certificates
- send bogus http responses
- return malformed RSS, AtomPub or CAP data
- last entry is older than one year
- does not work at all
'''

SWI_SERVICES = {
    # ARG Argentina
    'ARG:es': {'country': 'ARG', 'lang': 'es', 'title': 'ARG - Argentina (es)', 'url': 'http://www3.smn.gov.ar/CAP/AR.php', 'hdr_feed': '', 'hdr_atom': ''},
    # AUT Austria
    'AUT:de': {'country': 'AUT', 'lang': 'de', 'title': 'AUT - Austria (de)', 'url': 'http://meteoalarm.eu/ATOM/AT.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'AUT:en': {'country': 'AUT', 'lang': 'en', 'title': 'AUT - Austria (en)', 'url': 'http://meteoalarm.eu/ATOM/AT.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #BEL Belgium
    'BEL:nl': {'country': 'BEL', 'lang': 'nl', 'title': 'BEL - Belgium (nl)', 'url': 'http://meteoalarm.eu/ATOM/BE.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'BEL:fr': {'country': 'BEL', 'lang': 'fr', 'title': 'BEL - Belgium (fr)', 'url': 'http://meteoalarm.eu/ATOM/BE.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #BGH Bulgaria
    'BGH:bg': {'country': 'BGH', 'lang': 'bg', 'title': 'BGH - Bulgaria (bg)', 'url': 'http://meteoalarm.eu/ATOM/BG.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #BIH Bosnia
    'BIH:bs': {'country': 'BIH', 'lang': 'bs', 'title': 'BIH - Bosnia-Herzigovina (bs)', 'url': 'http://meteoalarm.eu/ATOM/BA.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # BRA Brazil
    'BRA:pt': {'country': 'BRA', 'lang': 'pt', 'title': 'BRA - Brazil (pt)', 'url': 'http://alert-as.inmet.gov.br/cap_12/rss/alert-as.rss', 'hdr_feed': '', 'hdr_atom': ''},

    # BRB Barbados
    'BRB:en': {'country': 'BRB', 'lang': 'en', 'title': 'BRB - Barbados (en)', 'url': 'https://brb-primary.capews.com/capews/pvtbox', 'hdr_feed': '', 'hdr_atom': ''},

    # CAN Canada
    'CAN:en': {'country': 'CAN', 'lang': 'en', 'title': 'CAN - Canada (en)', 'url': 'http://emergencyalert.alberta.ca/aeapublic/feed.atom', 'hdr_feed': '', 'hdr_atom': ''},
    'CAN:fr': {'country': 'CAN', 'lang': 'fr', 'title': 'CAN - Canada (fr)', 'url': 'http://emergencyalert.alberta.ca/aeapublic/feed.atom', 'hdr_feed': '', 'hdr_atom': ''},

    #CHE Switzerland?
    #'CHE:de': {'country': 'CHE', 'lang': 'de', 'title': 'CHE - Switzerland (de)', 'url': 'http://meteoalarm.eu/ATOM/CH.xml', 'hdr_feed': '', 'hdr_atom': ''},
    #'CHE:fr': {'country': 'CHE', 'lang': 'fr', 'title': 'CHE - Switzerland (fr)', 'url': 'http://meteoalarm.eu/ATOM/CH.xml', 'hdr_feed': '', 'hdr_atom': ''},
    #'CHE:it': {'country': 'CHE', 'lang': 'it', 'title': 'CHE - Switzerland (it)', 'url': 'http://meteoalarm.eu/ATOM/CH.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #CYP Cyprus?

    # CZE Czech Republic
    'CZE:cs': {'country': 'CZE', 'lang': 'cs', 'title': 'CZE - Czech Republic (cs)', 'url': 'http://meteoalarm.eu/ATOM/CZ.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'CZE:en': {'country': 'CZE', 'lang': 'en', 'title': 'CZE - Czech Republic (en)', 'url': 'http://meteoalarm.eu/ATOM/CZ.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # DEU Germany
    'DEU:de': {'country': 'DEU', 'lang': 'de', 'title': 'DEU - Germany (de)', 'url': 'https://www.dwd.de/DWD/warnungen/cap-feed/de/atom.xml', 'hdr_feed': {"User-agent":"Mozilla/5.0/2.19.1 (Linux x86_64)"}, 'hdr_atom': {"User-agent":"Mozilla/5.0/2.19.1 (Linux x86_64)"}},
    'DEU:en': {'country': 'DEU', 'lang': 'en', 'title': 'DEU - Germany (en)', 'url': 'https://www.dwd.de/DWD/warnungen/cap-feed/en/atom.xml', 'hdr_feed': 'User-agent":"Mozilla/5.0/2.19.1 (Linux x86_64)', 'hdr_atom': 'User-agent":"Mozilla/5.0/2.19.1 (Linux x86_64)'},

    # DNK Denmark
    'DNK:en': {'country': 'DNK', 'lang': 'en', 'title': 'DNK - Denmark (en)', 'url': 'http://meteoalarm.eu/ATOM/DK.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # ESP Spain
    'ES1:en': {'country': 'ESP', 'lang': 'en', 'title': 'ESP - Spain (en)', 'url': 'http://meteoalarm.eu/ATOM/ES.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'ES1:es': {'country': 'ESP', 'lang': 'es', 'title': 'ESP - Spain (es)', 'url': 'http://meteoalarm.eu/ATOM/ES.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'ES2:es': {'country': 'ESP', 'lang': 'es', 'title': 'ESP - Spain2 (es)', 'url': 'http://www.aemet.es/documentos_d/eltiempo/prediccion/avisos/rss/CAP_AFAE_RSS.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #EST Estonia?

    #FIN Finland
    'FIN:bs': {'country': 'FIN', 'lang': 'fi', 'title': 'FIN - Finland (fi)', 'url': 'http://meteoalarm.eu/ATOM/FI.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'FIN:sv': {'country': 'FIN', 'lang': 'sv', 'title': 'FIN - Finland (sv)', 'url': 'http://meteoalarm.eu/ATOM/FI.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'FIN:en': {'country': 'FIN', 'lang': 'en', 'title': 'FIN - Finland (en)', 'url': 'http://meteoalarm.eu/ATOM/FI.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #FRA France
    'FRA:en': {'country': 'FRA', 'lang': 'en', 'title': 'FRA - France (en)', 'url': 'http://meteoalarm.eu/ATOM/FR.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'FRA:fr': {'country': 'FRA', 'lang': 'fr', 'title': 'FRA - France (fr)', 'url': 'http://meteoalarm.eu/ATOM/FR.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #GBR Great Britian
    'GBR:en': {'country': 'GBR', 'lang': 'en', 'title': 'GBR - Great Britian (en)', 'url': 'http://meteoalarm.eu/ATOM/UK.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #GRC Greece
    'GRC:en': {'country': 'GRC', 'lang': 'en', 'title': 'GRC - Greece (en)', 'url': 'http://meteoalarm.eu/ATOM/GR.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'GRC:el': {'country': 'GRC', 'lang': 'el', 'title': 'GRC - Greece (el)', 'url': 'http://meteoalarm.eu/ATOM/GR.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #HRV - Croatia
    'HRV:en': {'country': 'HRV', 'lang': 'en', 'title': 'HRV - Croatia (en)', 'url': 'http://meteoalarm.eu/ATOM/HR.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'HRV:hr': {'country': 'HRV', 'lang': 'hr', 'title': 'HRV - Croatia (hr)', 'url': 'http://meteoalarm.eu/ATOM/HR.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # HUN Hungary
    'HUN:en': {'country': 'HUN', 'lang': 'en', 'title': 'HUN - Hungary (en)', 'url': 'http://meteoalarm.eu/ATOM/HU.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'HUN:hu': {'country': 'HUN', 'lang': 'hu', 'title': 'HUN - Hungary (hu)', 'url': 'http://meteoalarm.eu/ATOM/HU.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # IND Indonesia
    'IDN:id': {'country': 'IDN', 'lang': 'id', 'title': 'IDN - Indonesia (id)', 'url': 'https://signature.bmkg.go.id/alert/public/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #IRL Ireland?

    #ISL Iceland

    #ITA - Italy
    'ITA:en': {'country': 'ITA', 'lang': 'en', 'title': 'ITA - Italy (en)', 'url': 'http://meteoalarm.eu/ATOM/IT.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'ITA:it': {'country': 'ITA', 'lang': 'it', 'title': 'ITA - Italy (it)', 'url': 'http://meteoalarm.eu/ATOM/IT.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # KEN Kenya
    'KEN:en': {'country': 'KEN', 'lang': 'en', 'title': 'KEN - Kenya (en)', 'url': 'http://www.meteo.go.ke/cap/en/alerts/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'KWT:en': {'country': 'KWT', 'lang': 'en', 'title': 'KWT - Kuwait (en)', 'url': 'http://www.met.gov.kw/rss_eng/kuwait_cap.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #LTU - Lithuania
    'LTU:en': {'country': 'LTU', 'lang': 'en', 'title': 'LTU - Lithuania (en)', 'url': 'http://meteoalarm.eu/ATOM/LT.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'LTU:lt': {'country': 'LTU', 'lang': 'lt', 'title': 'LTU - Lithuania (lt)', 'url': 'http://meteoalarm.eu/ATOM/LT.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #LUX - Luxembourg
    'LUX:en': {'country': 'LUX', 'lang': 'en', 'title': 'LUX - Luxembourg (en)', 'url': 'http://meteoalarm.eu/ATOM/LU.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'LUX:de': {'country': 'LUX', 'lang': 'de', 'title': 'LUX - Luxembourg (de)', 'url': 'http://meteoalarm.eu/ATOM/LU.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'LUX:fr': {'country': 'LUX', 'lang': 'fr', 'title': 'LUX - Luxembourg (fr)', 'url': 'http://meteoalarm.eu/ATOM/LU.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #LVA - Latvia
    'LVA:en': {'country': 'LVA', 'lang': 'en', 'title': 'LVA - Latvia (en)', 'url': 'http://meteoalarm.eu/ATOM/LV.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'LVA:lv': {'country': 'LVA', 'lang': 'lv', 'title': 'LVA - Latvia (lv)', 'url': 'http://meteoalarm.eu/ATOM/LV.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #MDA - Moldova
    'MDA:en': {'country': 'MDA', 'lang': 'en', 'title': 'MDA - Moldova (en)', 'url': 'http://meteoalarm.eu/ATOM/MD.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'MDA:ro': {'country': 'MDA', 'lang': 'ro', 'title': 'MDA - Moldova (ro)', 'url': 'http://meteoalarm.eu/ATOM/MD.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # MEX Mexico
    'MEX:es': {'country': 'MEX', 'lang': 'es-419', 'title': 'MEX - Mexico (es)', 'url': 'https://correo1.conagua.gob.mx/feedsmn/feedalert.aspx', 'hdr_feed': '', 'hdr_atom': ''},

    #MKD - North Macedonia
    'MKD:en': {'country': 'MKD', 'lang': 'en', 'title': 'MKD - North Macedonia (en)', 'url': 'http://meteoalarm.eu/ATOM/MK.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #MNE - Montenegro
    'MNE:en': {'country': 'MNE', 'lang': 'en', 'title': 'MNE - Montenegro (en)', 'url': 'http://meteoalarm.eu/ATOM/ME.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'MNE:sr': {'country': 'MNE', 'lang': 'sr', 'title': 'MNE - Montenegro (sr)', 'url': 'http://meteoalarm.eu/ATOM/ME.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #MLT Malta?

    #NLD Netherlands
    'NLD:pap': {'country': 'NLD', 'lang': 'pap', 'title': 'NLD - Netherlands (pap)', 'url': 'http://201.229.69.218/cap/pap/alerts/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'NLD:en': {'country': 'NLD', 'lang': 'pap', 'title': 'NLD - Netherlands (en)', 'url': 'http://meteoalarm.eu/ATOM/NL.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'NLD:nl': {'country': 'NLD', 'lang': 'pap', 'title': 'NLD - Netherlands (nl)', 'url': 'http://meteoalarm.eu/ATOM/NL.xml', 'hdr_feed': '', 'hdr_atom': ''},
    #'NLD:en': {'country': 'NLD', 'lang': 'pap', 'title': 'NLD - Netherlands (en)', 'url': 'http://201.229.69.218/cap/en/alerts/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},
    #'NLD:nl': {'country': 'NLD', 'lang': 'pap', 'title': 'NLD - Netherlands (nl)', 'url': 'http://201.229.69.218/cap/nl/alerts/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #NOR Norway
    'NO1:en': {'country': 'NOR', 'lang': 'en', 'title': 'NOR - Norway (en)', 'url': 'http://meteoalarm.eu/ATOM/NO.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'NO1:no': {'country': 'NOR', 'lang': 'no', 'title': 'NOR - Norway (no)', 'url': 'http://meteoalarm.eu/ATOM/NO.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'NO2:en': {'country': 'NOR', 'lang': 'en', 'title': 'NOR - Norway (en)', 'url': 'https://alert.met.no/feed?lang=en', 'hdr_feed': '', 'hdr_atom': ''},
    'NO2:no': {'country': 'NOR', 'lang': 'nb', 'title': 'NOR - Norway (no)', 'url': 'https://alert.met.no/feed?lang=no', 'hdr_feed': '', 'hdr_atom': ''},
    'NO3:no': {'country': 'NOR', 'lang': 'no', 'title': 'NOR - Norway (no)', 'url': 'http://cap.nve.no/', 'hdr_feed': '', 'hdr_atom': ''},

    # NZL New zealand
    'NZL:en': {'country': 'NZL', 'lang': 'en', 'title': 'NZL - New Zealand (en)', 'url': 'http://api.geonet.org.nz/cap/1.2/GPA1.0/feed/atom1.0/quake', 'hdr_feed': '', 'hdr_atom': ''},

    # PHL Phlippines
    'PHL:en': {'country': 'PHL', 'lang': 'en', 'title': 'PHL - Philippines (en)', 'url': 'https://publicalert.pagasa.dost.gov.ph/feeds/', 'hdr_feed': '', 'hdr_atom': ''},

    #POL - Poland
    'POL:en': {'country': 'POL', 'lang': 'en', 'title': 'POL - Poland (en)', 'url': 'http://meteoalarm.eu/ATOM/PL.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'POL:po': {'country': 'POL', 'lang': 'po', 'title': 'POL - Poland (po)', 'url': 'http://meteoalarm.eu/ATOM/PL.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #PRT Portugal?

    # ROU Romania
    'ROU:ro': {'country': 'ROU', 'lang': 'ro', 'title': 'ROU - Romania (ro)', 'url': 'http://meteoalarm.eu/ATOM/RO.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # RUS Russian Federation
    'RUS:en': {'country': 'RUS', 'lang': 'en', 'title': 'RUS - Russian Federation (en)', 'url': 'https://meteoinfo.ru/hmc-output/cap/cap-feed/en/atom.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'RUS:ru': {'country': 'RUS', 'lang': 'en', 'title': 'RUS - Russian Federation (ru)', 'url': 'https://meteoinfo.ru/hmc-output/cap/cap-feed/ru/atom.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #SRB Serbia
    'SRB:en': {'country': 'SRB', 'lang': 'en', 'title': 'SRB - Serbia (en)', 'url': 'http://meteoalarm.eu/ATOM/RS.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'SRB:sr': {'country': 'SRB', 'lang': 'sr', 'title': 'SRB - Serbia (sr)', 'url': 'http://meteoalarm.eu/ATOM/RS.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #SWE - Sweden
    'SWE:en': {'country': 'SWE', 'lang': 'en', 'title': 'SWE - Sweden (en)', 'url': 'http://meteoalarm.eu/ATOM/SE.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'SWE:sv': {'country': 'SWE', 'lang': 'sv', 'title': 'SWE - Sweden (sv)', 'url': 'http://meteoalarm.eu/ATOM/SE.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #SVK - Slovakia
    'SVK:en': {'country': 'SVK', 'lang': 'en', 'title': 'SVK - Slovakia (en)', 'url': 'http://meteoalarm.eu/ATOM/SK.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'SVK:sk': {'country': 'SVK', 'lang': 'sk', 'title': 'SVK - Slovakia (sk)', 'url': 'http://meteoalarm.eu/ATOM/SK.xml', 'hdr_feed': '', 'hdr_atom': ''},

    #SVN - Slovenia
    'SVN:en': {'country': 'SVN', 'lang': 'en', 'title': 'SVN - Slovenia (en)', 'url': 'http://meteoalarm.eu/ATOM/SI.xml', 'hdr_feed': '', 'hdr_atom': ''},
    'SVN:sl': {'country': 'SVN', 'lang': 'sl', 'title': 'SVN - Slovenia (sl)', 'url': 'http://meteoalarm.eu/ATOM/SI.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # THA Thailand
    'THA:th': {'country': 'THA', 'lang': 'th', 'title': 'THA - Thailand (th)', 'url': 'https://www.tmd.go.th/feeds/CAPfeeds.php', 'hdr_feed': '', 'hdr_atom': ''},

    # TZA Tanzania
    'TZA:en': {'country': 'TZA', 'lang': 'en', 'title': 'TZA - Tanzania, United Republic of (en)', 'url': 'http://tma.meteo.go.tz:8080/feeds/en/alerts/rss.xml', 'hdr_feed': '', 'hdr_atom': ''},

    # USA
    'US1:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - United States of America (en)', 'url': 'https://alerts.weather.gov/cap/us.php?x=0', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},
    'US2:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - USGS Volcano (en)', 'url': 'https://volcanoes.usgs.gov/hans2/cap/rss/', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},
    'US3:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - USGS Volcano (en)', 'url': 'http://feeds.enviroflash.info/cap/aggregate.xml', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},

    # ZZZ Custom
    'ZZZ:zz': {'country': 'ZZ', 'lang': 'zz', 'title': 'Custom configuration', 'url': 'custom', 'hdr_feed': '', 'hdr_atom': ''}
}
