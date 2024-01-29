import json
from os import path
import os
from faker import Faker
import random
from datetime import datetime, date, time
import functools

from services.utils import gerar_codigo

faker = Faker()
formato_data = "%Y-%m-%d %H:%M:%S"

def salvar_dados(dados):
    with open('database/registros.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


def criar_registro(id: str, codigo: str, tipo: str, valor: float, data: str, tipo_investimento: object):
    registro = {
        'id': id, 
        'codigo': codigo,
        'tipo': tipo, 
        'valor': valor, 
        'data': data,
    }

    if tipo == 'investimento':
        registro['tipo_investimento'] = tipo_investimento

    return registro

def gerar_data_aleatoria():
    data = faker.date_between_dates(date(2000, 1, 1), datetime.now())
    formato_data = "%Y-%m-%d %H:%M:%S"
    data_formatada = str(data.strftime(formato_data))
    return data_formatada


def populate():
    dados = []
    tipos = ["saque", "deposito", "investimento"] # tive que  tirar o acento pois estava dando bug
    tipos_investimento = [
        {
            'titulo': "CDB",
            'juros': 3.9e-04
        },
        {
            'titulo': "LCI",
            'juros': 3.8e-04
        },
        {
            'titulo': "LCA",
            'juros': 3.6e-04
        }
    ]

    if path.isfile('database/registros.json') is False:
        os.mkdir('database')
        with open('database/registros.json', 'w', encoding='utf-8') as registro:
            registro.write('[{}]')
     
    for _ in range(30):
        id = faker.random_int(min=1, max=10000000)
        data = gerar_data_aleatoria()
        tipo = random.choice(tipos)
        codigo = gerar_codigo(dados, tipo, data)
        valor = faker.unique.random_int()
        tipo_investimento = random.choice(tipos_investimento)
        
        if tipo == "saque":
            registro = criar_registro(id, codigo, tipo, -valor, data, tipo_investimento)
        else:
            registro = criar_registro(id, codigo, tipo, valor, data, tipo_investimento)
        dados.append(registro)
    
    salvar_dados(dados)

populate()

