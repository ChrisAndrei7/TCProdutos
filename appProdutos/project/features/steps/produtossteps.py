from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8003'

@given('que eu tenho os detalhes do produto')
def step_impl(context):
    context.product_data = {
        'nome': 'Batata pequena',
        'descricao': 'Batata frita pequena',
        'ingredientes': 'Batata, sal',
        'categoria': 'Acompanhamentos',
        'preco': '11.47'
    }

@given('que eu tenho os detalhes atualizados do produto')
def step_impl(context):
    context.updated_product_data = {
        'nome': 'Batata media',
        'descricao': 'Batata frita media',
        'ingredientes': 'Batata, sal',
        'categoria': 'Acompanhamentos',
        'preco': '13.25'
    }

@when('eu faço o cadastro de um produto')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/produtos/create", json=context.product_data)

@when('eu faço uma atualização de um produto')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/produtos/update/1", json=context.updated_product_data)

@when('eu faço a consulta dos produtos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/produtos")

@when('eu faço a exclusão de um produto')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/produtos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
