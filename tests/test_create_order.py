import pytest
from api_users import UsersApi
from conftest import create_and_cancel_order


class TestCreateOrder:
    @pytest.mark.parametrize('color', [
        ['BLACK', 'GREY'],
        ['BLACK'],
        ['GREY'],
        []
    ])
    def test_create_order_with_different_color_options(self, color, create_and_cancel_order):
        data_order, track_container = create_and_cancel_order
        data_order['color'] = color
        response = UsersApi.create_order(data_order)
        assert response.status_code == 201
        assert "track" in response.json()

