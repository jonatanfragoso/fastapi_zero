from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_deve_retornar_html():
    client = TestClient(app)
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Olá, Mundo!</h1>'
