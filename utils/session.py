import os

from utils.requests_helper import BaseSession


def reqres() -> BaseSession:
    reqres_url=os.getenv('reqres_url')
    return BaseSession(base_url=reqres_url)


def demowebshop() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    return BaseSession(base_url=demo_url)

