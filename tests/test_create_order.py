import pytest
from api_users import UsersApi
from conftest import create_and_cancel_order
from allure import title,description,step


class TestCreateOrder:
    @pytest.mark.parametrize('color', [
        ['BLACK', 'GREY'],
        ['BLACK'],
        ['GREY'],
        []
    ])
    @title('Создание заказа с указанием разных вариантов цвета')
    @description('Проверяем, что создался заказ с разными данными, и наличие в теле ответа "track"')
    def test_create_order_with_different_color_options(self, color, create_and_cancel_order):
        data_order, track_container = create_and_cancel_order
        data_order['color'] = color
        with step('Отправляем запрос на создание заказа'):
            response = UsersApi.create_order(data_order)
        with step('Проверяем код ответа и наличие "track"'):
            assert response.status_code == 201, response.json()
            assert "track" in response.json(), response.json()

