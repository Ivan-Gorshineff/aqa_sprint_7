from allure import step, description, title
import pytest
import data_users
from api_users import UsersApi
from helper import Helper
from conftest import register_new_courier_and_return_login_password


class TestLoginCourier:
    @title('Позитивный сценарий: логин курьера')
    @description('Проверяем, что можно авторизоваться и возвращаем id')
    def test_login_courier_return_id(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        with step('Отправляем запрос на авторизацию курьера'):
            response = UsersApi.login_courier(payload)
        with step('Проверяем код ответа и наличие id'):
            assert response.status_code == 200, response.json()
            assert 'id' in response.json(), response.json()


    @title('Негативный сценарий: авторизация с незаполненными обязательными полями')
    @description('Проверяем,что нельзя авторизоваться с незаполненным логином/паролем')
    @pytest.mark.parametrize('modified_field', ['login', 'password'])
    def test_cant_login_courier_without_password_and_login(self, modified_field, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        payload[modified_field] = ''
        with step('Отправляем запрос на авторизацию с незаполненным полем'):
            response = UsersApi.login_courier(payload)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 400, response.json()
            assert response.json()['message'] == 'Недостаточно данных для входа', response.json()


    @title('Негативный сценарий: авторизация с некорректными обязательными полями')
    @description('Проверяем,что нельзя авторизоваться с некорректным логином/паролем')
    @pytest.mark.parametrize('modified_field', ['login', 'password'])
    def test_cant_login_courier_with_incorrect_login(self, modified_field, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        payload[modified_field] = Helper.random_string()
        with step('Отправляем запрос на авторизацию с некорректным полем'):
            response = UsersApi.login_courier(payload)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 404, response.json()
            assert response.json()['message'] == 'Учетная запись не найдена', response.json()

    @title('Негативный сценарий: авторизация под несуществующим пользователем')
    @description('Проверяем,что нельзя авторизоваться под несуществующим пользователем')
    def test_cant_login_courier_has_not_credentials(self):
        payload = data_users.NON_EXISTENT_COURIER_CREDENTIALS
        with step('Отправляем запрос на авторизацию под несуществующим пользователем'):
            response = UsersApi.login_courier(payload)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 404, response.json()
            assert response.json()['message'] == 'Учетная запись не найдена', response.json()