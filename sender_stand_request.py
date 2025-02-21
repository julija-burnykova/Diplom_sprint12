
import configuration

import requests

import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_ID_PATH,
                         json=body)
    

def get_id_order(track):
    new_order = post_new_order(data.creating_order)
    track = post_new_order.json()['track']
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + "track")
    
