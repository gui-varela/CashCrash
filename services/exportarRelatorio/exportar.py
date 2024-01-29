import os
import shutil

def exportar_relatorio(caminho_database):
    arquivo_json = "registros.json"
    caminho_destino = os.path.join(os.path.expanduser("~"), "Downloads", arquivo_json)

    shutil.copy(caminho_database, caminho_destino)
    print(f"Relatório exportado para: {caminho_destino}")

caminho_database = "database/registros.json"

exportar_relatorio(caminho_database)
