import os

import pytest
from dotenv import load_dotenv

from utils.requests_helper import BaseSession


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()

@pytest.fixture(scope='session')
def demoqa() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    with BaseSession(base_url=demo_url) as session:
        yield session


@pytest.fixture(scope='session')
def demoqa_authorized_user_one() -> BaseSession:
    demo_url = os.getenv('demo_shop_url')
    auth_cookie_name = 'NOPCOMMERCE.AUTH'
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    with BaseSession(base_url=demo_url) as session:
        response = session.post(
            '/login',
            data={'Email': login, 'Password': password},
            allow_redirects=False
        )
        auth_cookie_value = response.cookies.get(auth_cookie_name)
        session.cookies.set(auth_cookie_name, auth_cookie_value)
        yield session

@pytest.fixture()
def create_user(request):
    return {
        "name": str(request.param[0]),
        "job": str(request.param[1])
    }
