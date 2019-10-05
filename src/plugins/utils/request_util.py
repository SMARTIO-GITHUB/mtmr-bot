import requests
import json


CONTENT_TYPE_JSON = {'Content-Type': 'application/json'}


def do_get(endpoint, parameter):
    responce = requests.get(endpoint, params=parameter)
    
    return dict(responce.json())


def do_post(endpoint, parameter):
    responce = requests.post(endpoint, parameter, headers=CONTENT_TYPE_JSON)

    return dict(responce.json())