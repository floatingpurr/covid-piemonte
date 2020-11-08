import requests
import struct
import re
import csv



URLS = {
    'province' : 'https://giscovid.sdp.csi.it/tiles/data/province.geojson', # not used anymore
    'comuni': 'https://giscovid.sdp.csi.it/tiles/data/centroidi.geojson',
    'indexes' : 'https://giscovid.sdp.csi.it/tiles/data/va.dat',
    'data': 'https://giscovid.sdp.csi.it/tiles/data/in.dat',
    'meta': 'https://giscovid.sdp.csi.it/tiles/data/config.json'
}


PROV = {
    '001': 'Torino',
    '002': 'Vercelli',
    '003': 'Novara',
    '004': 'Cuneo',
    '005': 'Asti',
    '006': 'Alessandria',
    '096': 'Biella',
    '103': 'Verbano-Cusio-Ossola',
}




def get_geo_data():
    """
    Returns geographical data.
    """

    r = requests.get(URLS['comuni'])

    return_dict = {}

    for item in r.json()['features']:
        return_dict[item['properties']['COMUNE_IST']] = {
            'comune': item['properties']['COMUNE_NOM'],
            'provincia': PROV[item['properties']['ID_PV']] # rougly the first 3 chars of codice_istat
        }

    return return_dict




def get_indexes():
    """
    Returns a list of data indexes (e.g., ['1182', 'istat', '1105', 'r1105']).
    """
    r = requests.get(URLS['indexes'])
    return r.text.split(';')




def get_covid_data(indexes):
    """
    Returns actual data, processing raw bytes; a real pain in the ass.
    """
    r = requests.get(URLS['data'])

    # data are in binary format (i.e., JavaScript ArrayBuffer https://javascript.info/arraybuffer-binary-arrays)

    # The first data collection comes from a Uint32Array (treats every 4 bytes as an integer)
    # See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array/Uint32Array
    index = int(indexes[0]) - 1
    start = 0
    upper_bound = index * 4
    int_data = [int.from_bytes(r.content[i:i+4], byteorder='little', signed=False) for i in range(start, upper_bound, 4)]
    
    # A second data collection comes from a Float32Array (treats every 4 bytes as a floating point number)
    # See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array
    cols = len(indexes) - 2
    start = upper_bound
    upper_bound = start + index * cols * 4
    float_data = [struct.unpack('<f', r.content[i:i+4])[0] for i in range(start , upper_bound, 4)]

    return {'int_data': int_data, 'float_data': float_data}




def get_metadata():
    """
    Gets metadata of the retrieved collection
    """
    r = requests.get(URLS['meta'])
    meta_string = r.json()['ultimo_aggiornamento']
    date = re.search(r'\d{2}.\d{2}.\d{4}', meta_string)
    time = re.search(r'\d{2}:\d{2}', meta_string)

    meta = [{
        'aggiornamento' : f'Dati aggiornati al {date.group()} ore {time.group()}'
    }]

    return meta


def process_data(geo_data, covid_data):
    """
    Processes geo and covid data and returns the final resultset.
    """
    codici_istat = covid_data['int_data']
    positivi = covid_data['float_data'][::2]
    tasso_positivi = covid_data['float_data'][1::2]

    # serialize the resultset
    resulset = []

    for c, p, t in zip(codici_istat, positivi, tasso_positivi):

        codice_istat = str(c).zfill(6)
        comune = geo_data[codice_istat]

        resulset.append({
            'comune': comune['comune'].title(),
            'codice_istat': codice_istat,
            'provincia': comune['provincia'],
            'positivi': int(p), 
            'positivi_per_1000_abitanti': float(f"{t:.2f}")
        })

    return sorted(resulset, key=lambda k: k['comune']) 




def write_2_file(csv_file, data):
    """
    Writes data to file
    """
    csv_columns = data[0].keys()

    try: 
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for d in data:
                writer.writerow(d)
    except IOError:
        print("I/O error")





def main():

    # get geo data (almost static throughout time, at least, I guess that...)
    geo_data = get_geo_data()

    # get covid data
    indexes = get_indexes() # indexes for binary data segregation
    covid_data = get_covid_data(indexes)

    # get metadata
    metadata = get_metadata()

    # Data Processing
    final_data = process_data(geo_data, covid_data)

    # Write to files
    write_2_file("data/metadata.txt", metadata)
    write_2_file("data/covid-piemonte.csv", final_data)




if __name__ == "__main__":
    main()