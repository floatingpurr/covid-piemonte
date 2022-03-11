import requests


def get_token(login_url, username, password):

    r = requests.post(
        login_url,
        headers={"Content-Type": "application/json"},
        json={"email": username, "password": password},
    )

    return r.json()["token"]


def fetch_data(data_url, proxy_url="", jwt=""):

    if not proxy_url:
        print('no proxy')
        return requests.get(data_url)

    print('proxy')
    return requests.post(
        proxy_url,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {jwt}"},
        json={"url": data_url},
    )
