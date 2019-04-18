import requests
from utils import *


def get_headers():
    # метод в зависимости от енвайрмента возвращает нужные хедеры
    headers = {'Content-Type': 'application/json'}
    return headers


# метод делает пост запрос и возвращает полностью весь респонс
def post_request(url, data, headers):
    response = requests.post(url=url, data=data, headers=headers)
    return response


def standard_body():
    body = {
        "clientApplicationIdentifier": {
            "DeviceIdentifier": "b5a18f51-162b-4a93-887b-df7f9762321e",
            "MobilePhoneNumber": "dubinaanatolii@gmail.com",
            "Language": "ru",
            "Platform": 2,
            "SecurityKey": "6d8f7c53077f748d8a380048fbbb8919",
            "Version": "3.2.3"
        }
    }
    standard_body = default_dict_to_json(body)
    return standard_body