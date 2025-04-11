from urls import main_url,cancel_order_url,create_courier_url,login_courier_url,order_url
import requests


class UsersApi:

    @staticmethod
    def create_courier(body: str):
        return requests.post(f'{main_url}{create_courier_url}', json=body)

    @staticmethod
    def login_courier(body: str):
        return requests.post(f'{main_url}{login_courier_url}', json=body)

    @staticmethod
    def create_order(body: str):
        return requests.post(f'{main_url}{order_url}', json=body)

    @staticmethod
    def get_order():
        return requests.get(f'{main_url}{order_url}')

    @staticmethod
    def cancel_order(body: str):
        return requests.put(f'{main_url}{cancel_order_url}', json=body)

    @staticmethod
    def delete_courier(id):
        return requests.delete(f'{main_url}{create_courier_url}'+"/"+id)

