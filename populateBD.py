import json
from faker import Faker
from crud import criar_registro
import random
from datetime import datetime

faker = Faker()
formato_data = "%Y-%m-%d %H:%M:%S"

def salvar_dados(dados):
    with open('database/registros.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def criar_registro(id: str, tipo: str, valor: float, data: str):
    return {'id': id, 'tipo': tipo, 'valor': valor, 'data': data}

def populate():
    dados = []
    tipos = ["saque", "depósito", "investimento"]
    for i in range(10):
        tipo = random.choice(tipos)
        valor = faker.unique.random_int()
        data = str(datetime.now().strftime(formato_data))
        id = tipo[0] + str(i) + "-" + data.split(".")[0].split(" ")[0]

        registro = criar_registro(id, tipo, valor, data)
        dados.append(registro)
    
    salvar_dados(dados)

populate()
