import json
from datetime import datetime

informacoes = '''
----------------------------------
           FILTRO - EXTRATO
----------------------------------
DICAS DE CONSULTA:

- Deixe vazio para ignorar
- Exemplo de data: 30/09/2021
- Valor = Valor investido

'''

def consultarExtrato():
    print(informacoes)
    # Solicitar entradas do usuário
    data_inicial = input("Data inicial (DD/MM/AAAA): ")
    data_final = input("Data final (DD/MM/AAAA): ")
    valor_inicial = float(input("Valor inicial: "))
    valor_final = float(input("Valor final: "))

    # Lendo os dados do arquivo JSON
    with open('database/registros.json', 'r') as arquivo:
        dados_json = json.load(arquivo)

    # Converter as datas de string para objeto datetime
    for dado in dados_json:
        dado["data"] = datetime.strptime(dado["data"], "%Y-%m-%d %H:%M:%S")

    # Filtrar dados com base nas informações fornecidas pelo usuário
    dados_filtrados = []
    for dado in dados_json:
        data_valida = (not data_inicial or dado["data"] >= datetime.strptime(data_inicial, "%d/%m/%Y")) and \
                    (not data_final or dado["data"] <= datetime.strptime(data_final, "%d/%m/%Y"))
        valor_valido = (not valor_inicial or dado["valor"] >= valor_inicial) and \
                    (not valor_final or dado["valor"] <= valor_final)

        if data_valida and valor_valido:
            dados_filtrados.append(dado)

    # Imprimir os dados filtrados
    for dado in dados_filtrados:
        print(f"ID: {dado['id']}, Tipo: {dado['tipo']}, Valor: {dado['valor']}, Data: {dado['data']}")
    respostaUser = input("Deseja Fazer outra consulta?\n\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\n")
    while True:
        if respostaUser == '1':
            consultarExtrato()
            break
        elif respostaUser == '2':
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break
        else:
            print('\n\nvalor inválido. Escreva um numero.\n\n')
            respostaUser = input("\n\nDeseja Fazer outra consulta?\n\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\n")

