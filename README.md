# Dati Covid-19 in Piemonte

![piemonte-data-scraper](https://github.com/floatingpurr/covid-piemonte/workflows/piemonte-data-scraper/badge.svg)
[![GitHub commit](https://img.shields.io/github/last-commit/floatingpurr/covid-piemonte)](https://github.com/floatingpurr/covid-piemonte/commits/master)

Dati sul Covid-19 dell'unità di crisi della Regione Piemonte.

## Perché esiste questo repository

Attualmente l'unità di crisi Covid della Regione Piemonte rilascia i dati dei "soggetti risultati positivi al test covid-19 che non risultano in data odierna deceduti o guariti". Questi dati sono disponibili su questa mappa: https://www.regione.piemonte.it/web/covid-19-mappa-piemonte.

Al fine di rendere più leggibile il dato, in questo repository viene mantenuto aggiornato [un unico file tabellare](data/covid-piemonte.csv) con l'ultima versione dei dati rilasciati (altre info nei [metadati](data/metadata.txt)).

I dati relativi al _penultimo_ aggiornamento (tipicamente riferito al giorno precedente) sono disponibili in [data/previous](data/previous) e seguono il medesimo schema di quelli giornalieri.

**E' possibile utilizzare l'ultimo snapshot dei dati puntando a questa url**:

<https://raw.githubusercontent.com/floatingpurr/covid-piemonte/main/data/covid-piemonte.csv>

## Stato degli aggiornamenti

I dati vengono aggiornati ogni 10 minuti. Il [badge](#dati-covid-19-in-Piemonte) a inizio pagina è di colore verde se gli aggiornamenti stanno funzionando senza errori. Per ulteriori dettagli, verificare i log del [workflow di aggiornamento](https://github.com/floatingpurr/covid-piemonte/actions?query=workflow%3Apiemonte-data-scraper).

## Referenze & AoB

* [La mappa da cui provengono i dati](https://giscovid.sdp.csi.it/tiles/)

* Un altro [repository](https://github.com/to-mg/covid-19-piemonte) che raccoglie lo storico dei dati e altre informazioni.

* [geojson province piemontesi](https://giscovid.sdp.csi.it/tiles/data/province.geojson)

* [geojson comuni piemontesi](https://giscovid.sdp.csi.it/tiles/data/centroidi.geojson)

* [centroidi.js](https://giscovid.sdp.csi.it/tiles/js/centroidi.js) centroidi comuni piemontesi

* [istat-centroidi.csv](geodata/istat-centroidi.csv) centroidi comuni piemontesi (estratto)
