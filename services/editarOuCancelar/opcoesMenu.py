import sys
sys.path.append('.')
sys.path.append('services')
from despedida import despedidaController
from time import sleep
#import crud
from crud import deletar_registro
from crud import ler_dados
import json
import os
textoOpcoes = '''
----------------------------------
    EDITAR/CANCELAR OPERAÇÃO
----------------------------------
Deseja editar ou cancelar? [E/C]
Digite [1] para sair.
'''
def menuEditarOuCancelar():
  while True:
    editarOuCancelar = input(textoOpcoes)
  
    if editarOuCancelar in ['1', 'um', 'Um', 'UM', '[1]']:
      despedidaController()
      break
    elif editarOuCancelar in ['C', 'c']:
        id_change = input("Insira o ID da operação a ser cancelada")
        try:
            with open('database/registros.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
    
        deletar_registro(dados, id_change)
        with open('database/registros.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        os.remove('registros.json')
        break
    else:
      print("\nESCOLHA INVÁLIDA.\nDigite [E] para editar uma operação, [C] para cancelar uma operação ou [1] para sair.\n")
      sleep(4)
