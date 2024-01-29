import json
import sys
from datetime import datetime

from services.utils import gerar_codigo
sys.path.append('services\editarOuCancelar\cancelamento')
import services.editarOuCancelar.cancelamento.cancelarOperacao
from faker import Faker


fake = Faker()
dicionario_tipos = {'S':'saque', 'D': 'deposito', 'I': 'investimento', 's':'saque', 'd': 'deposito', 'i': 'investimento'}
tipos_investimento = [
        {
            'titulo': "CDB",
            'juros': 3.9e-05
        },
        {            
            'titulo': "LCI",
            'juros': 3.8e-05
        },
        {
            'titulo': "LCA",
            'juros': 3.6e-05
        }
    ]


def ler_dados():
    try:
        with open('database/registros.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    
    return dados

def salvar_dados(dados):
    with open('database/registros.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

def criar_registro(valor, tipo):
    dados = ler_dados()
    cont = ""
    for x in dados[-1]['codigo'][1:]:
        if x != '-':
            cont = cont + x
        else:
            break
    cont = int(cont) + 1
    id_ficticio = fake.random_int(min=1, max=10000000) # gera um id aleatório
    formato_data = "%Y-%m-%d %H:%M:%S"
    data = str(datetime.now().strftime(formato_data))
    if tipo == "deposito":
        return {'id': id_ficticio,'codigo': f"d{cont}-{data[:10]}", 'tipo': tipo, 'valor': float(valor), 'data': data}
    if tipo == "saque":
        if float(valor) < 0:
            return {'id': id_ficticio,'codigo': f"d{cont}-{data[:10]}", 'tipo': tipo, 'valor': float(valor), 'data': data}
        else:
            return {'id': id_ficticio,'codigo': f"d{cont}-{data[:10]}", 'tipo': tipo, 'valor': -float(valor), 'data': data}
    
def criarInvestimento(valor, titulo):
    dados = ler_dados()
    cont = ""
    for x in dados[-1]['codigo'][1:]:
        if x != '-':
            cont = cont + x
        else:
            break
    cont = int(cont) + 1
    id_ficticio = fake.random_int(min=1, max=10000000) # gera um id aleatório
    formato_data = "%Y-%m-%d %H:%M:%S"
    data = str(datetime.now().strftime(formato_data))
    if titulo == "CDB":
        return {'id': id_ficticio, 'tipo': 'investimento','codigo': f"i{cont}-{data[:10]}", \
                    'valor': float(valor), 'montante': float(valor), 'data': data, 'tipo_investimento': {"titulo": titulo, "juros": 0.00039}}
    elif titulo == "LCI":
        return {'id': id_ficticio, 'tipo': 'investimento','codigo': f"i{cont}-{data[:10]}", \
                    'valor': float(valor), 'montante': float(valor), 'data': data, 'tipo_investimento': {"titulo": titulo, "juros": 0.00038}}
    else:
        return {'id': id_ficticio, 'tipo': 'investimento','codigo': f"i{cont}-{data[:10]}", \
                    'valor': float(valor), 'montante': float(valor), 'data': data, 'tipo_investimento': {"titulo": titulo, "juros": 0.00036}}

def listar_registros():
    dados = ler_dados()
    for i, registro in enumerate(dados, 1):
        print({'id': {registro['id']}, 'tipo': {registro['tipo']}, 'valor': {registro['valor']}, 'data': {registro['data']}})

def listar_registros_por_tipo(tipo):
    dados = ler_dados()
    dados_por_tipo = [ dado for dado in dados if dado['tipo'] == tipo ]
    return dados_por_tipo

def listar_registros_por_data_e_valor(dados, data_inicial, data_final, valor_inicial, valor_final):
    dados_filtrados = []
    valorTotal = 0
    for dado in dados:
        data_formatada = datetime.strptime(dado["data"], '%Y-%m-%d %H:%M:%S')

        data_valida = (not data_inicial or (data_formatada >= data_inicial if data_inicial != "" else True) ) and \
                    (not data_final or (data_formatada <= data_final if data_final != "" else True))
        
        valor_valido = (not valor_inicial or (dado["valor"] >= valor_inicial if valor_inicial != "" else True)) and \
                    (not valor_final or (dado["valor"] <= valor_final if valor_final != "" else True))
        
        if data_valida and valor_valido:
            dados_filtrados.append(dado)
            valorTotal += dado["valor"]

    return dados_filtrados, valorTotal


def adicionar_registro(tipo, valor):
    dados = ler_dados()
    novo_registro = criar_registro(valor, tipo)
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Registro adicionado com sucesso!")


def editar_registro(dados, id_change):
        index_change = None
        for i, item in enumerate(dados):
            if item.get('codigo') == id_change:
                index_change = i
                break

        if index_change is not None:
            registro_edit = dados[index_change]
            print (f"\nRegistro a ser editado: \n {registro_edit}\n")
            registro_novo_tipo = input("Insira [S] para transformar em saque, [D] para transformar em deposito e [I] para transformar em investimento.\nDeixe em branco para não alterar tipo\n")
            
            if registro_novo_tipo in dicionario_tipos:
                registro_novo_tipo = dicionario_tipos[registro_novo_tipo]
            else:
                registro_novo_tipo = registro_edit['tipo']

            if registro_edit['tipo'] == "investimento":
                del registro_edit['tipo_investimento']
            if registro_novo_tipo == "investimento":
                while True:
                    try:
                        registro_edit_titulo = int(input("Insira o titulo atualizado:\n[1] - CDB (0,039%/dia)\n[2] - LCI (0,038%/dia)\n[3] - LCA (0,036%/dia)\n" ))
                        registro_edit['tipo_investimento'] = tipos_investimento[registro_edit_titulo-1]
                        break
                    except:
                        print("Titulo invalido")

            registro_edit['tipo'] = registro_novo_tipo

            try:
                registro_edit_valor = float(input("Insira o valor atualizado do registro.\nDeixe em branco para não alterar\n"))
            except:
                registro_edit_valor = registro_edit['valor'] 
            if (registro_novo_tipo == "saque" and (registro_edit_valor > 0 or None)) or (registro_novo_tipo != "saque" and registro_edit_valor < 0):
                registro_edit['valor'] = -registro_edit_valor
            else:
                registro_edit['valor'] = registro_edit_valor      
                         
            formato_data = "%Y-%m-%d %H:%M:%S"
            new_date = str(datetime.now().strftime(formato_data))
            registro_edit['data'] = new_date
            registro_edit['codigo'] = gerar_codigo(dados, registro_novo_tipo, new_date)
            dados[index_change] = registro_edit
            salvar_dados(dados)
            print(f"""----------------------------------
        EDITADO COM SUCESSO!
----------------------------------
A operação de id {id} foi editada com sucesso! Resultado após a edição:

{dados[index_change]}""")

def deletar_registro(dados, id_change):
        index_change = None
        for i, item in enumerate(dados):
            if item.get('codigo') == id_change:
                index_change = i
                break
        # If the element is found, delete it
        if index_change is not None:
            del dados[index_change]
            print(f'''
----------------------------------
        CANCELADO COM SUCESSO!
----------------------------------
A operação de ID {id_change} foi cancelada e não será realizada!
''')
        else:
            print(f"Elemento com ID {id_change} não encontrado.")
        salvar_dados(dados)

