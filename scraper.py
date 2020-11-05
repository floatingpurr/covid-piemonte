import requests

URLS = {
    'indexes' : 'https://giscovid.sdp.csi.it/tiles/data/va.dat',
    'data' : 'https://giscovid.sdp.csi.it/tiles/data/in.dat', # Returned as a JavaScript ArrayBuffer (binary data)
}

PROV = {}


def get_indexes():
    """
    Returns a list of data indexes (e.g., ['1182', 'istat', '1105', 'r1105'])
    """
    r = requests.get(URLS['indexes'])
    return r.text.split(';')

def get_data(indexes):
    """
    Returns actual data from a binary response
    """
    r = requests.get(URLS['data'])

    # data are in a binary format

    # A first collection of chunks is a Uint32Array (treats every 4 bytes as an integer)
    index = int(indexes[0]) - 1
    int_data = [int.from_bytes(r.content[0:4], byteorder='little', signed=False) for i in range(0, index, 4)]

    return r



def main():
    indexes = get_indexes()
    get_data(indexes)


if __name__ == "__main__":
    main()