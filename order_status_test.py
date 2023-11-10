import sender_stand_request


# Функция для позитивной проверки: по треку заказа можно получить данные о заказе
def test_get_order_by_track_success():
    order_track = sender_stand_request.post_new_order_track().json()['track']
    order_response = sender_stand_request.get_order_by_track(order_track)

    assert order_response.status_code == 200

# Анна Левицкая, 10-я когорта — Финальный проект. Инженер по тестированию плюс
