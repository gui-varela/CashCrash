import json
import sys
sys.path.append('../../.')
import crud
from datetime import datetime

textoMenu = '''
----------------------------------
             EXTRATO
----------------------------------
DICAS DE CONSULTA:

- Deixe vazio para ignorar
- Exemplo de data: 14/10/2017
- Depósito/Saque: D/S

Digite:
'''


def consultarExtrato():

    print(textoMenu)
    data_inicial = input('Data inicial (DD/MM/AAAA): ').strip()
    data_final = input('Data final (DD/MM/AAAA): ').strip()
    valor_inicial = float(input('Valor inicial: '))
    valor_final = float(input('Valor final: '))
    escolha_operacao = input('Tipo de operação [D/S]: ').lower().strip()

    # Lendo os dados do arquivo JSON
    dados_json = crud.ler_dados()

    # Converter as datas de string para objeto datetime
    for dado in dados_json:
        dado["data"] = datetime.strptime(dado["data"], "%Y-%m-%d %H:%M:%S")

    # Filtrar dados com base nas informações fornecidas pelo usuário
    dados_filtrados = []
    tipo_operacao = {'d': 'deposito', 's': 'saque'}
    for dado in dados_json:
        data_valida = (not data_inicial or dado["data"] >= datetime.strptime(data_inicial, "%d/%m/%Y")) and \
                    (not data_final or dado["data"] <= datetime.strptime(data_final, "%d/%m/%Y"))
        valor_valido = (not valor_inicial or dado["valor"] >= valor_inicial) and \
                    (not valor_final or dado["valor"] <= valor_final)

        tipo_valido = dado["tipo"] == tipo_operacao[escolha_operacao]
        if escolha_operacao in 'ds':
            if data_valida and valor_valido and tipo_valido:
                dados_filtrados.append(dado)

    # Imprimir os dados filtrados
    for dado in dados_filtrados:
        print(f"ID: {dado['id']}, Tipo: {dado['tipo']}, Valor: {dado['valor']}, Data: {dado['data']}")

