#Юлия Бурныкова, 26-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration

import requests

import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
    

def test_get_order_by_track():
    new_order = post_new_order(data.creating_order)
    track = new_order.json()['track']
    id_respons=requests.get(configuration.URL_SERVICE + configuration.ORDER_ID_PATH + str(track))
    assert id_respons.status_code == 200
    
