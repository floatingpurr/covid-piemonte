import requests
import json


def get_token(login_url, username, password):

    r = requests.post(
        login_url,
        headers={"Content-Type": "application/json"},
        json={"email": username, "password": password},
    )

    return r.json()["token"]


def fetch_data(data_url, proxy_url="", jwt=""):

    if not proxy_url:
        return requests.get(data_url)

    return requests.post(
        proxy_url,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {jwt}"},
        json={"url": data_url},
    )


def jsonify(data):
    """Takes a string, returns a parsed JSON.
    Takes ancoding problems into account

    Args:
        string (str): original data
    """

    try:
        return data.json()
    except json.JSONDecodeError:
        # Catch the Unexpected UTF-8 BOM error
        data.encoding='utf-8-sig'
        return data.json()
