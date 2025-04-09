import allure
import pytest
import data_users
from api_users import UsersApi
from helper import Helper
from conftest import register_new_courier_and_return_login_password


class TestLoginCourier:
    def test_login_courier_return_id(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        response = UsersApi.login_courier(payload)
        assert response.status_code == 200
        assert 'id' in response.json()


    @pytest.mark.parametrize('modified_field', ['login', 'password'])
    def test_cant_login_courier_without_password_and_login(self, modified_field, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        payload[modified_field] = ''
        response = UsersApi.login_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @pytest.mark.parametrize('modified_field', ['login', 'password'])
    def test_cant_login_courier_with_incorrect_login(self, modified_field, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        payload[modified_field] = Helper.random_string()
        response = UsersApi.login_courier(payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'


    def test_cant_login_courier_has_not_credentials(self):
        payload = data_users.NON_EXISTENT_COURIER_CREDENTIALS
        response = UsersApi.login_courier(payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'