from datetime import datetime

from services.utils import calcular_montante, exportar_relatorio



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

textoBuscaSemResultados = '''
----------------------------------
    A busca não retornou
    resultados.

    Tente tornar sua busca mais
    abrangente.
----------------------------------
'''

def resultadoConsultaInvestimentoController(investimentos, valor):
    if len(investimentos) == 0:
      print(textoBuscaSemResultados)
    else:
        print(textoResultado)
        exibir_investimentos(investimentos)
        print("Valor Total Investido: R$",float(valor))
        print(textoFim)
        escolhaExportar = input("Deseja exportar o relatório? (s/n)\n Sua escolha: ")
        dataString = datetime.now().strftime('%d-%m-%Y_%I:%M%p')
        if escolhaExportar.lower() == "s":
            exportar_relatorio(investimentos, f"investimentos_{dataString}")

    entrada_usuario = input("\n\nDeseja Fazer outra consulta?\n\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\n")
    exibirMenuAposConsulta(entrada_usuario)
  

def formatar_investimento(investimento):
    data_formatada = datetime.strptime(investimento['data'],'%Y-%m-%d %H:%M:%S')
    data_atual = datetime.now() 
    dias_passados = (data_atual - data_formatada).days
    montante = calcular_montante(investimento['valor'], investimento['tipo_investimento']['juros'], dias_passados)

    return f"""
==========  {data_formatada.strftime('%d/%m/%Y')}  ==========

    Título: {investimento['tipo_investimento']['titulo']}

    Valor: R$ {format(investimento['valor'], ".2f")}
    Montante: R$ {format(montante, ".2f")} 
    
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
          print('\n\nValor inválido. Escreva um número.\n\n')
          entrada_usuario = "\nEscreva [1] para fazer outra consulta\nEscreva [2] para voltar para o menu principal\n\nSua escolha: "
          