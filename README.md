# Dati Covid-19 in Piemonte

![covid-piemonte-scraper](https://github.com/floatingpurr/covid-piemonte/workflows/covid-piemonte-scraper/badge.svg)

Dati sul Covid-19 dell'unità di crisi della Regione Piemonte.

## Perché esiste questo repository

Attualmente l'unità di crisi Covid della Regione Piemonte rilascia i dati dei "soggetti risultati positivi al test covid-19 che non risultano in data odierna deceduti o guariti". Questi dati sono disponibili su questa mappa: https://www.regione.piemonte.it/web/covid-19-mappa-piemonte.

Al fine di rendere più leggibile il dato, in questo repository viene mantenuto aggiornato [un unico file tabellare](data/covid-piemonte.csv) con l'ultima versione dei dati rilasciati (altre info nei [metadati](data/metadata.csv)).

E' possibile utilizzare l'ultimo snapshot dei dati puntando a questa url:

<https://raw.githubusercontent.com/floatingpurr/covid-piemonte/main/data/covid-piemonte.csv?token=ADRCJ6GIBN4IUG5RPFVI3HC7V25WM>

## Referenze & AoB

* [La mappa da cui provengono i dati](https://giscovid.sdp.csi.it/tiles/)

* Un altro [repository](https://github.com/to-mg/covid-19-piemonte) che raccoglie lo storico dei dati e altre informazioni.

* [geojson province piemontesi](https://giscovid.sdp.csi.it/tiles/data/province.geojson)

* [geojson comuni piemontesi](https://giscovid.sdp.csi.it/tiles/data/centroidi.geojson)

* [centroidi.js](https://giscovid.sdp.csi.it/tiles/js/centroidi.js) (centroidi comuni piemontesi)