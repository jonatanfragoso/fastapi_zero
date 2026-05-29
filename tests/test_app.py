from http import HTTPStatus


def test_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_deve_retornar_html(client):
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.text == '<h1>Olá, Mundo!</h1>'


def test_deve_criar_usuario(client):
    user_data = {
        'name': 'João',
        'email': 'joao@example.com',
        'password': '123456',
    }
    response = client.post('/users', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['name'] == 'João'
    assert response.json()['email'] == 'joao@example.com'
    assert 'id' in response.json()
    assert 'password' not in response.json()


def test_deve_listar_usuarios(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'name': 'João',
                'email': 'joao@example.com',
                'id': 1,
            }
        ]
    }


def test_deve_atualizar_usuario(client):
    user_data = {
        'name': 'João Silva',
        'email': 'joao.silva@example.com',
        'password': '654321',
    }
    response = client.put('/users/1', json=user_data)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'João Silva'
    assert response.json()['email'] == 'joao.silva@example.com'
    assert 'id' in response.json()
    assert 'password' not in response.json()


def test_deve_retornar_erro_usuario_nao_encontrado(client):
    user_data = {
        'name': 'Maria',
        'email': 'maria@example.com',
        'password': '123456',
    }
    response = client.put('/users/999', json=user_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'Usuário não encontrado'


def test_deve_deletar_usuario(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'João Silva'
    assert response.json()['email'] == 'joao.silva@example.com'


def test_deve_retornar_erro_usuario_nao_encontrado_ao_deletar(client):
    response = client.delete('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'Usuário não encontrado'
