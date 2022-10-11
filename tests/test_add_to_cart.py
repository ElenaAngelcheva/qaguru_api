import os
from uuid import uuid4

import requests

from utils.session import demowebshop


def test_add_to_cart_unauthorized(demoqa):
    response=demoqa.post('/addproducttocart/catalog/31/1/1',
                           cookies={'Nop.customer': 'a271be64-c0d9-4494-aefb-7bae1ebfa546;'})
    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_two_product():
    uid = str(uuid4())
    demowebshop().post('/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )
    response = demowebshop().post('/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_authorized(demoqa_authorized_user_one):
    response = demoqa_authorized_user_one.post('/addproducttocart/catalog/31/1/1',
    )

    assert response.status_code == 200
    assert response.json()['success'] is True
    assert response.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert response.json()['updatetopcartsectionhtml'] == "(1)"