import os
import shutil

def exportar_relatorio(caminho_database):
    nome_relatorio = "relatorio.json"
    caminho_destino = os.path.join(os.path.expanduser("~"), "Downloads", nome_relatorio)

    shutil.copy(caminho_database, caminho_destino)
    print(f"Relatório exportado para: {caminho_destino}")

caminho_database = "database/registros.json"

exportar_relatorio(caminho_database)
