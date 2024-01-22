import json

textoMenu = '''
----------------------------------
       FILTRO - INVESTIMENTOS
----------------------------------
Bem-vindo! O que deseja fazer?

[1] - Consultar extrato
[2] - Depositar
[3] - Sacar
[4] - Acessar investimentos
[5] - Editar/Cancelar operação
[6] - Sair
'''


def filtro():
    with open('../../database/registros.json') as registro:
        dados = registro.read()
        
    print(dados)

filtro()