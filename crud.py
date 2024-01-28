import json
import sys
from datetime import datetime
sys.path.append('services\editarOuCancelar\cancelamento')
import services.editarOuCancelar.cancelamento.cancelarOperacao


tipo_edit = {'D':'Despesa', 'R': 'Receita', 'I': 'Investimento'}
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
    for x in dados[-1]['id'][1:]:
        if x != '-':
            cont = cont + x
        else:
            break
    cont = int(cont) + 1
    formato_data = "%Y-%m-%d %H:%M:%S"
    data = str(datetime.now().strftime(formato_data))
    if tipo == "deposito":
        return {'id': f"d{cont}-{data[:11]}", 'tipo': tipo, 'valor': int(valor), 'data': data}
    if tipo == "saque":
        return {'id': f"s{cont}-{data[:11]}", 'tipo': tipo, 'valor': int(valor), 'data': data}

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
    
    for dado in dados:
        data_formatada = datetime.strptime(dado["data"], '%Y-%m-%d %H:%M:%S')

        data_valida = (not data_inicial or data_formatada >= data_inicial) and \
                    (not data_final or data_formatada <= data_final)
        
        valor_valido = (not valor_inicial or dado["valor"] >= valor_inicial) and \
                    (not valor_final or dado["valor"] <= valor_final)
        
        if data_valida and valor_valido:
            dados_filtrados.append(dado)

    return dados_filtrados   


def adicionar_registro(tipo, valor):
    dados = ler_dados()
    novo_registro = criar_registro(valor, tipo)
    dados.append(novo_registro)
    salvar_dados(dados)
    print("Registro adicionado com sucesso!")


def editar_registro(dados, id_change):
        index_change = None
        for i, item in enumerate(dados):
            if item.get('id') == id_change:
                index_change = i
                break

        if index_change is not None:
            registro_edit = dados[index_change]
            print (f"\nRegistro a ser editado: \n {registro_edit}\n")
            registro_edit_tipo = input("Insira [D] para transformar em despesa, [R] para transformar em receita e [I] para transformar em investimento.\nDeixe em branco para não alterar tipo\n")
            if registro_edit_tipo in tipo_edit:
                registro_edit['tipo'] = tipo_edit[registro_edit_tipo]
            if registro_edit['tipo'] == "Investimento":
                registro_edit_titulo = input("Insira o titulo atualizado:\n[1] - CDB (0,039%/dia)\n[2] - LCI (0,038%/dia)\n[3] - LCA (0,036%/dia)\n")
            try:
                registro_edit_valor = int(input("Insira o valor atualizado do registro.\nDeixe em branco para não alterar\n"))
            except:
                print("Valor invalido!")
            if isinstance(registro_edit_valor, int):
                registro_edit['valor'] = registro_edit_valor
            new_date = str(datetime.now())
            registro_edit['data'] = new_date
            dados[index_change] = registro_edit
            salvar_dados(dados)
            print(f"""----------------------------------
        EDITADO COM SUCESSO!
----------------------------------
A operação de id {id} foi editada com sucesso! Resultado após a edição:

Tipo: {tipo_edit[registro_edit_tipo]}
Valor: {registro_edit_valor}
Data: {new_date}""")

def deletar_registro(dados, id_change):
        index_change = None
        for i, item in enumerate(dados):
            if item.get('id') == id_change:
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

