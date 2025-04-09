from api_users import UsersApi


class TestGetOrders:
    def test_get_orders(self):
        response = UsersApi.get_order()
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()["orders"], list)

