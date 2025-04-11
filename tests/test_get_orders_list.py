from api_users import UsersApi
from allure import title,description,step


class TestGetOrdersList:
    @title('Получение списка заказов')
    @description('Проверяем,что запрос возвращает список заказов')
    def test_get_orders(self):
        with step('Отправляем запрос на получение списка заказов'):
            response = UsersApi.get_order()
        with step('Проверяем код ответа и наличие "orders", а также проверяем, что "orders" - список'):
            assert response.status_code == 200
            assert 'orders' in response.json(), response.json()
            assert isinstance(response.json()["orders"], list), response.json()

