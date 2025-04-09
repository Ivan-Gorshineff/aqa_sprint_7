import pytest
import requests
import random
import string
import data_users
from helper import Helper
from api_users import UsersApi
from urls import create_courier_url, main_url


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture()
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{main_url}{create_courier_url}', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


#  фикстурa на создание и удаление курьера
@pytest.fixture
def courier_credentials():
    body = Helper.credentials()
    yield body

    response = UsersApi.login_courier(body)
    if response.status_code == 200:
        id_courier = str(response.json()['id'])
        UsersApi.delete_courier(id_courier)


@pytest.fixture
def create_and_cancel_order():
    data_order = data_users.ORDER
    track_container = {}
    yield data_order, track_container

    if "track" in track_container:
        UsersApi.cancel_order(track_container)