# 1 - imports
import csv
import json

import pytest

import requests
from requests import HTTPError

teste_dados_novos_usuarios = [
    (1, 'Juca', 'Pirama', 'juca@iterasys.com.br'),  # usuário 1
    (2, 'Agatha', 'Christie', 'agtha@iterasys.com.br')  # usuario 2
]
teste_dados_usuarios_atuais = [
    (1, 'George', 'Bluth', 'george.bluth@reqres.in'),  # usuário 1
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')  # usuario 2
]


# CRUD / ICAE
# APLICAÇÕES:                           APIs
# Create                                post    Incluir/Publicar
# Reach /                               Research get  Consultar/ Pegar
# Update                                put Atualizar
# delete                                delete Excluir

@pytest.mark.parametrize('id,nome,sobrenome,email', teste_dados_usuarios_atuais)
def testar_dados_usuarios(id, nome, sobrenome, email):  # função que testa o algo

    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')
        print(f'id: {id_obtido} \n  nome: {nome_obtido} \n  sobrenome: {sobrenome_obtido} \n  email: {email_obtido} \n')
        print('id:{} \n nome:{} \n sobrenome:{} \n email:{}'.format(id_obtido, nome_obtido, sobrenome_obtido,
                                                                    email_obtido))
        print(json.dumps(json_response, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email


    except HTTPError as http_fail:
        print(f' Falha inesperada: {http_fail}')

    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')


# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users/{id}


# Leitor do arquivo csv
def ler_dados_do_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
            print(f'Arquivo não encontrado:{nome_arquivo}')
    except Exception as fail:
        print(f' Falha imprevista: {fail}')



@pytest.mark.parametrize('id,nome,sobrenome,email', ler_dados_do_csv())
def teste_dados_csv (id, nome, sobrenome, email):  # função que testa o algo

    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        json_response = response.json()
        id_obtido = json_response['data']['id']
        nome_obtido = json_response['data']['first_name']
        sobrenome_obtido = json_response['data']['last_name']
        email_obtido = json_response['data']['email']

        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')
        print(f'id: {id_obtido} \n  nome: {nome_obtido} \n  sobrenome: {sobrenome_obtido} \n  email: {email_obtido} \n')
        print('id:{} \n nome:{} \n sobrenome:{} \n email:{}'.format(id_obtido, nome_obtido, sobrenome_obtido,
                                                                    email_obtido))
        print(json.dumps(json_response, indent=2, sort_keys=True))

        assert id_obtido == int(id)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email


    except HTTPError as http_fail:
        print(f' Um erro de HTTP aconteceu: {http_fail}')

    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')