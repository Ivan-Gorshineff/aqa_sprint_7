import random

from faker import Faker
from string import ascii_letters, digits


fake = Faker('ru_RU')
class Helper:

    @staticmethod
    def random_string(length=10) -> str:
        return ''.join(random.choices(ascii_letters + digits, k=length))


    @staticmethod
    def credentials():
        login = fake.name()
        password = fake.password()
        firstname = fake.first_name()
        return {
            'login': login,
            'password': password,
            'firstname' : firstname
        }

