from datetime import datetime

from crud import listar_registros_por_tipo, listar_registros_por_data_e_valor
from services.investimentos.resultadoConsulta import resultadoConsultaInvestimentoController


informacoes = '''
----------------------------------
      FILTRO - INVESTIMENTOS
----------------------------------
DICAS DE CONSULTA:

- Deixe vazio para ignorar
- Exemplo de data: 30/09/2021
- Valor = Valor investido

'''

def filtroInvestimentosController():
    print(informacoes)
    
    data_inicial, data_final = validarInputsDeData()
    print("\n")
    valor_inicial, valor_final = validarInputsDeValor()
    
    dados_investimento = listar_registros_por_tipo("investimento")
    
    dados_filtrados = listar_registros_por_data_e_valor(
        dados_investimento,
        data_inicial,
        data_final,
        valor_inicial,
        valor_final
    )

    resultadoConsultaInvestimentoController(dados_filtrados[0], dados_filtrados[1])


def validarInputsDeData():
    datas_validas = False

    while not datas_validas:
        data_inicial = tratarInputData("Digite a data inicial: ")
        data_final = tratarInputData("Digite a data final: ")

        if not data_inicial and not data_final and data_inicial > data_final:
            print("Data final deve ser posterior à data inicial. Insira as datas novamente.")
        else:
            datas_validas = True
    
        return data_inicial, data_final


def validarInputsDeValor():
    valores_validos = False
    
    while not valores_validos:
        valor_inicial = tratarInputValor("Digite o valor mínimo: ")
        valor_final = tratarInputValor("Digite o valor máximo: ")

        if valor_inicial != "" and valor_final != "" and valor_inicial > valor_final:
            print("Valor máximo deve ser maior que o valor mínimo. Insira os valores novamente.")
        else:
            valores_validos = True

        return valor_inicial, valor_final


def tratarInputData(mensagemInput):
    while True:
        try:
            data = input(mensagemInput)
            if not data:
                return ""
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
            return data_formatada
        except:
            print("Digite formato correto de data. (Exemplo: 09/12/2021)")


def tratarInputValor(mensagemInput):
    while True:
        try:
            valor = input(mensagemInput)
            if not valor:
                return ""
            return float(valor.replace(",", "."))
        except:
            print("Digite um formato correto de valor. (Exemplo: 1000.00)")


