import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o JSON no arquivo {nome_arquivo}.")

operacoes = ler_arquivo_json("database/registros.json")


def obterOperacaoMaiorValor():
    valores = []
    for op in operacoes:
        valores.append(op['valor'])

    maior = max(valores)
    return maior

maior = obterOperacaoMaiorValor()
print(maior)