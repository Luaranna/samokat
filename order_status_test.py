import sender_stand_request


# Функция для позитивной проверки: по треку заказа можно получить данные о заказе
def test_positive_assert():
    order_response = sender_stand_request.get_order_by_track()
    assert order_response.status_code == 200
