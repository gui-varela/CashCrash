import json
from faker import Faker
from crud import criar_registro

# Criar uma instância do Faker
faker = Faker()

dados = []

def ler_dados():
    try:
        with open('registros.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    
    return dados

def salvar_dados(dados):
    with open('registros.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def populate():
    registros = ler_dados()
    for registro in registros:
        criar_registro
    