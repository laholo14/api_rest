import json
import requests

base_url = "https://dummyapi.io/data/api/"
app_id = "609c5b8de76976812c3d84af"

headers = {'Content-Type': 'application/json',
           'app-id': app_id
           }


def appel_data(data, limite):
    url = '{}{}?limit={}'.format(base_url, data, limite)
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.json()
    else:
        return 'erreur {}'.format(reponse.status_code)


def appel_data_byId(data, idd):
    url = '{}{}/{}'.format(base_url, data, idd)
    reponse = requests.get(url, headers=headers)
    if reponse.status_code == 200:
        return reponse.json()
    else:
        return 'erreur {}'.format(reponse.status_code)

