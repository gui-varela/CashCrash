import json
import sys
from datetime import datetime
sys.path.append('services\editarOuCancelar\cancelamento')
import cancelarOperacao
tipo_edit = {'D':'Despesa', 'R': 'Receita', 'I': 'Investimento'}
def ler_dados():
    try:
        with open('database/registros.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    
    return dados

def salvar_dados(dados):
    with open('database/registros.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def criar_registro(nome, idade):
    return {'nome': nome, 'idade': idade}

def listar_registros():
    dados = ler_dados()
    for i, registro in enumerate(dados, 1):
        print(f"{i}. Nome: {registro['nome']}, Idade: {registro['idade']}")

def adicionar_registro(nome, idade):
    dados = ler_dados()
    novo_registro = criar_registro(nome, idade)
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

