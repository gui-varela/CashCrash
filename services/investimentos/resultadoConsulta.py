from datetime import datetime



textoResultado = '''
----------------------------------
       RESULTADO DA BUSCA
----------------------------------
'''

textoFim = '''
----------------------------------
              FIM
----------------------------------
'''

def resultadoConsultaInvestimentoController(investimentos):
  print(textoResultado)
  exibir_investimentos(investimentos)
  print(textoFim)
      
  entrada_usuario = input("Deseja Fazer outra consulta?\n\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\n")
 
  exibirMenuAposConsulta(entrada_usuario)
  

def formatar_investimento(investimento):
    data_formatada = datetime.strptime(investimento['data'],'%Y-%m-%d %H:%M:%S')
    return f"""
==========  {data_formatada.strftime('%d/%m/%Y')}  ==========

        Valor: R$ {format(investimento['valor'], ".2f")}
        Montante: {format(investimento['valor'], ".2f")} 
        ID: {investimento['id']}
    """

    
def exibir_investimentos(investimentos):
    for investimento in investimentos:
        print(formatar_investimento(investimento))

def exibirMenuAposConsulta(entrada_usuario):
    while True:
      if entrada_usuario == '1':
          #from filtro import filtroInvestimentosController
          from services.investimentos.filtro import filtroInvestimentosController
          filtroInvestimentosController()
          break
      elif entrada_usuario == '2':
          from services.menuPrincipal import menuPrincipalController
          menuPrincipalController()
          break
      else:
          print('\n\nValor inválido. Escreva um numero.\n\n')
          entrada_usuario = input("\n\nDeseja Fazer outra consulta?\n\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\n")