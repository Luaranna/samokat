import data
import configuration
import requests


# Функция для создания нового заказа
def post_new_order_track(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


# Функция для получения заказа по номеру заказа
def get_order_by_track():
    response = post_new_order_track(data.order_body)
    new_order_track = str (response.json()['track'])
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + new_order_track)