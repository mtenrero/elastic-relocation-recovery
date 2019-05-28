import requests

def rGetJSON(url: str):
    """GET the contents of an URL and return its response as a JSON object"""
    response = requests.get(url)
    return response.json()

def rPostJSON(url: str, body: object):
    """POST body json and get json response also"""
    response = requests.post(url, json=body)
    return response.json()