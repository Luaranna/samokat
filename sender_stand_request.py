import data
import configuration
import requests


# Функция для создания нового заказа
def post_new_order_track():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


# Функция для получения заказа по номеру заказа
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))