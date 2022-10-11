import pytest
from pytest_voluptuous import S
from schemas import validation_user
from utils.session import reqres


def test_list_users():
    response = reqres().get(url='/users', params={'page': 2})
    assert response.status_code == 200
    assert response.json()['total'] == 12


def test_single_user():
    response = reqres().get(url='/users/2')
    assert response.status_code == 200
    assert len(response.json()['support']['text']) == 72
    assert response.json()['support']['text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!'


def test_single_user_not_found():
    response = reqres().get(url='/users/23')
    assert response.status_code == 404
    assert response.json() == {}


def test_user_schema_validation():
      response = reqres().get(url='/users/2')
      assert S(validation_user.schema) == response.json()


@pytest.mark.parametrize('create_user', [('morpheus', 'leader')], indirect=True)
def test_create_post(create_user):
    response = reqres().post(
         url='/users',
         json=create_user
      )
    assert response.status_code == 201


@pytest.mark.parametrize('create_user', [('morpheus', 'zion resident')], indirect=True)
def test_update_put(create_user):
    response = reqres().put(
         url='/users/2',
         json=create_user
      )
    assert response.status_code == 200


@pytest.mark.parametrize('create_user', [('morpheus', 'zion resident')], indirect=True)
def test_update_patch(create_user):
    response = reqres().patch(
         url='/users/2',
         json=create_user
      )
    assert response.status_code == 200


def test_user_delete():
    response = reqres().delete(url='/users/2')
    assert response.status_code == 204





