from datetime import datetime

from services.utils import exportar_relatorio


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

def resultadoConsultaController(operacoes):
    valorTotal = 0
    for operação in operacoes:
        valorTotal += operação["valor"]
    if len(operacoes) == 0:
      print(textoBuscaSemResultados)
    else:
      print(textoResultado)
      exibir_operacoes(operacoes, valorTotal)
      print(textoFim)
      escolhaExportar = input("Deseja exportar o relatório? (s/n)\n Sua escolha: ")
      if escolhaExportar.lower() == "s":
        exportar_relatorio(operacoes)

    exibirMenuAposConsulta()

def formatar_operacao(operacao):
    data_formatada = datetime.strptime(operacao['data'],'%Y-%m-%d %H:%M:%S')

    return f"""
==========  {data_formatada.strftime('%d/%m/%Y')}  ==========

    {int((26-len(operacao['tipo']))/2)*" "}{operacao['tipo'].upper()}
    --------------------------
        Valor: R$ {format(operacao['valor'], ".2f")}
        ID: {operacao['id']}
    """

    
def exibir_operacoes(operacoes, valorTotal):
    for operacao in operacoes:
        print(formatar_operacao(operacao))
    print("Valor total: R$", float(valorTotal))
    

def exibirMenuAposConsulta():
    while True:     
        entrada_usuario = input("\nDeseja Fazer outra consulta?\n\n  [1] Fazer outra consulta\n  [2] Voltar para o menu principal\n\nSua escolha: ")
        if entrada_usuario == '1':
            from services.extrato.filtro import consultarExtrato
            consultarExtrato()
            break
        elif entrada_usuario == '2':
            from services.menuPrincipal import menuPrincipalController
            menuPrincipalController()
            break
        else:
            print('\n\nValor inválido. Escreva um numero.\n\n')