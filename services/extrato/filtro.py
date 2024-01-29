import json
from datetime import datetime

from services.extrato.resultadoConsulta import resultadoConsultaController

informacoes = '''
----------------------------------
         FILTRO - EXTRATO
----------------------------------
DICAS DE CONSULTA:

- Deixe vazio para ignorar
- Exemplo de data: 30/09/2021
- Depósito/Saque = D/S

'''

def tratarInputData(mensagem):
     while True:
        try:
            data = input(mensagem)
            if not data:
                return ""
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
            return data_formatada
        except:
            print("Por favor, escreva uma data no formato DD/MM/AAAA.")

def tratarInputValor(mensagem):
    while True:
        try:
            valor = input(mensagem)
            if not valor:
                return ""
            return float(valor.replace(',','.'))
        except:
            print("Por favor, escreva um numero no formato XXXX.XX")

def tratarInputTipo(mensagem):
    while True:
        try:
            tipo = input(mensagem)
            if tipo.lower() not in ["d", "s",""]:
                raise
            return tipo
        except:
            print("Favor escreva um filtro apropriado ou deixe em branco")

def consultarExtrato():
    print(informacoes)
    # Solicitar entradas do usuário
    data_inicial = tratarInputData("Data inicial (DD/MM/AAAA): ")
    data_final = tratarInputData("Data final (DD/MM/AAAA): ")
    print("\n")
    valor_inicial = tratarInputValor("Valor inicial: ")
    valor_final = tratarInputValor("Valor final: ")
    print("\n")
    tipo_filtro = tratarInputTipo('''Filtrar por deposito [D] ou saque [S]\n(Deixe em branco para qualquer)\n\nSua escolha: ''')
    
    # Lendo os dados do arquivo JSON
    with open('database/registros.json', 'r') as arquivo:
        dados_json = json.load(arquivo)

    # Filtrar dados com base nas informações fornecidas pelo usuário
    dados_filtrados = []
    for dado in dados_json:
        data_formatada = datetime.strptime(dado["data"], "%Y-%m-%d %H:%M:%S")

        data_valida = (not data_inicial or (data_formatada >= data_inicial if data_inicial != "" else True)) and \
                    (not data_final or (data_formatada <= data_final  if data_final != "" else True))
        valor_valido = (not valor_inicial or dado["valor"] >= valor_inicial if valor_inicial != "" else True) and \
                    (not valor_final or (dado["valor"] <= valor_final if valor_final != "" else True))

        if data_valida and valor_valido:
            if tipo_filtro.lower() == "d" and dado["tipo"] == "deposito":
                dados_filtrados.append(dado)
            elif tipo_filtro.lower() == "s" and dado["tipo"] == "saque":
                dados_filtrados.append(dado)
            elif tipo_filtro.lower() == "" and dado['tipo'] != 'investimento':
                dados_filtrados.append(dado)

    resultadoConsultaController(dados_filtrados)
