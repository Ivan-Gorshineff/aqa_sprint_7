from urls import Urls
import requests


class UsersApi:

    @staticmethod
    def create_courier(body: str):
        return requests.post(Urls.create_courier_endpoint, json=body)

    @staticmethod
    def login_courier(body: str):
        return requests.post(Urls.login_courier_endpoint, json=body)

    @staticmethod
    def create_order(body: str):
        return requests.post(Urls.order_endpoint, json=body)

    @staticmethod
    def get_order():
        return requests.get(Urls.order_endpoint)

    @staticmethod
    def cancel_order(body: str):
        return requests.put(Urls.cancel_order_endpoint, json=body)

    @staticmethod
    def delete_courier(id):
        return requests.delete(Urls.create_courier_endpoint+"/"+id)

