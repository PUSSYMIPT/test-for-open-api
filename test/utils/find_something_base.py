import requests


def find_something(category: str, host: str = 'http://localhost:3030', item_name: str = "New Product"):
    url = host + "/" + category
    name = item_name
    url += "?name[$like]={}".format(name)

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()