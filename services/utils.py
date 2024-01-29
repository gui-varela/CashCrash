import os
import shutil
import json

def calcular_montante(capital: float, taxa: float, dias_passados: int):
  """
    Calcula o montante de um investimento aplicado em juros compostos.

    Args:
        capital (float): O capital (valor inicial do investimento).
        taxa (float): A taxa de juros diária.
        dias_passados (int): O número de dias de capitalização.

    Returns:
        float: O montante total (incluindo o capital e os juros compostos).
    """
  montante = capital * (1 + taxa) ** dias_passados
  return montante

def gerar_codigo(dados, tipo, data):
    dados_por_tipo = [ dado for dado in dados if dado['tipo'] == tipo ]
    cont_dados_por_tipo = len(dados_por_tipo)+1
    codigo = f"{tipo[0]}{cont_dados_por_tipo}-{data[:10]}"
    return codigo


def exportar_relatorio(dados):
    nome_relatorio = "relatorio.json"
    caminho_destino = os.path.join(os.path.expanduser("~"), "Downloads", nome_relatorio)
    with open(f'{caminho_destino}', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)
        
    print(f"Relatório exportado para: {caminho_destino}")