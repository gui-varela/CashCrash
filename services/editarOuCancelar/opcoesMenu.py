import sys
sys.path.append('.')
sys.path.append('services')
#from menuPrincipal import menuPrincipalController
from despedida import despedidaController
from time import sleep
#import crud
from crud import deletar_registro
from crud import ler_dados
from crud import editar_registro
import json
import os

textoOpcoes = '''
----------------------------------
    EDITAR/CANCELAR OPERAÇÃO
----------------------------------
Deseja editar ou cancelar? [E/C]
Digite [1] para voltar ao menu principal
'''
def menuEditarOuCancelar():
  while True:
    editarOuCancelar = input(textoOpcoes)
    if editarOuCancelar in ['1', 'um', 'Um', 'UM', '[1]']:
       import menuPrincipal
       menuPrincipal.menuPrincipalController()
       break
    elif editarOuCancelar in ['C', 'c']:
        id_change = input("Insira o codigo da operação a ser cancelada: ")
        try:
            with open('database/registros.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
    
        deletar_registro(dados, id_change)
        with open('database/registros.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        #os.remove('registros.json')
        break
    elif editarOuCancelar in ['E', 'e']:
        id_change = input("Insira o codigo da operação a ser editada: ")
        try:
            with open('database/registros.json', 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        editar_registro(dados, id_change)
        
    else:
      print("\nESCOLHA INVÁLIDA.\nDigite [E] para editar uma operação, [C] para cancelar uma operação ou [1] para sair.\n")
      sleep(4)
