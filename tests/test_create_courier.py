import  pytest
from api_users import UsersApi
import data_users
from conftest import courier_credentials
from allure import title,description,step


class TestCreateCourier:
    def test_create_courier(self, courier_credentials):
        payload = courier_credentials
        response = UsersApi.create_courier(payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    def test_cant_create_courier_twice(self, courier_credentials):
        payload = courier_credentials
        UsersApi.create_courier(payload)
        response = UsersApi.create_courier(payload)
        assert response.status_code == 409
        assert response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @pytest.mark.parametrize('data',[data_users.CREDENTIALS_WITHOUT_LOGIN, data_users.CREDENTIALS_WITHOUT_PASSWORD])
    def test_cant_create_courier_without_login_and_password(self, data):
        payload = data
        response = UsersApi.create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == 'Недостаточно данных для создания учетной записи'

    def test_cant_create_courier_with_duplicate_login(self, courier_credentials):
        payload = courier_credentials
        UsersApi.create_courier(payload)
        courier_with_duplicate_login = data_users.COURIER_CREDENTIALS_DATA
        courier_with_duplicate_login['login'] = payload['login']
        response = UsersApi.create_courier(courier_with_duplicate_login)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
