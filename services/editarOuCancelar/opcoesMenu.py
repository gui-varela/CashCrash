import sys
sys.path.append("edicao")
from edicao.editarOperacao import editarOperacaoController

tela = '''
----------------------------------
      EDITAR/CANCELAR OPERAÇAO
----------------------------------
'''

def menuEdicaoController():
  print(tela)

  acao = input("Deseja editar ou cancelar? [E/C]: ").upper().strip()
  id = input("Digite o ID da operação: ")

  print(acao)
  
  if acao == "E":
    editarOperacaoController(id)
  else:
    print("cancelar")
  