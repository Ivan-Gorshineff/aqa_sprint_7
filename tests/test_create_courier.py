import  pytest
from api_users import UsersApi
import data_users
from conftest import courier_credentials
from allure import title,description,step,attach


class TestCreateCourier:
    @title('Позитивный сценарий: создание курьера')
    @description('Проверяем, что после создания курьера возвращается статус код 201 и тело ответа "{"ok":True}"')
    def test_create_courier_return_status_code_201_and_message_ok(self, courier_credentials):
        payload = courier_credentials
        with step('Отправляем запрос на создание курьера'):
            response = UsersApi.create_courier(payload)
        with step('Проверяем код ответа и статус'):
            assert response.status_code == 201, response.json()
            assert response.json() == {"ok":True}, response.json()


    @title('Негативный сценарий: создание два одинаковых курьера')
    @description('Проверяем, что нельзя создать курьера с одинаковыми данными')
    def test_cant_create_courier_twice(self, courier_credentials):
        payload = courier_credentials
        with step('Отправляем запрос на создание курьера'):
            UsersApi.create_courier(payload)
        with step('Снова отправляем тот же запрос'):
            response = UsersApi.create_courier(payload)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 409, response.json()
            assert response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.', response.json()


    @title('Негативный сценарий: создание курьера без логина/пароля')
    @description('Проверяем, что нельзя создать курьера без логина и пароля')
    @pytest.mark.parametrize('data',[data_users.CREDENTIALS_WITHOUT_LOGIN, data_users.CREDENTIALS_WITHOUT_PASSWORD])
    def test_cant_create_courier_without_login_and_password(self, data):
        payload = data
        with step('Отправляем запрос с незаполненным полем'):
            response = UsersApi.create_courier(payload)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 400, response.json()
            assert response.json()["message"] == 'Недостаточно данных для создания учетной записи', response.json()

    @title('Негативный сценарий: создание курьера с уже существующим логином')
    @description('Проверяем,что нельзя создать курьера с существующим логином')
    def test_cant_create_courier_with_login_already_exists(self, courier_credentials):
        payload = courier_credentials
        with step('Отправляем запрос на создание курьера'):
            UsersApi.create_courier(payload)
        courier_with_duplicate_login = data_users.COURIER_CREDENTIALS_DATA
        courier_with_duplicate_login['login'] = payload['login']
        with step('Отправляем запрос повторно с тем же логином'):
            response = UsersApi.create_courier(courier_with_duplicate_login)
        with step('Проверяем наличие текста об ошибке и статус'):
            assert response.status_code == 409, response.json()
            assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.', response.json()
