import json
import csv

from processamento_dados import Dados

# Leitura dos arquivos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinado = 'data_processed/dados_combinados.csv'


def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

dados_json = leitura_json(path_json)

def leitura_csv(path_csv):
    dados_csv = [] 
    with open(path_csv, 'r', newline='') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

dados_csv = leitura_csv(path_csv)

def get_columns(dados):
    return list(dados[-1].keys())

def leitura_dados (path, tipo_arquivo):
    dados = []
    
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
        
    return dados

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
        
    return new_dados_csv

def size_data(dados):
    return len(dados)

def join(dadosA,dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

#Extract
dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)

#Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto' : 'Categoria do Produto',
               'Valor em Reais (R$)' : 'Preço do Produto (R$)',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja' : 'Filial',
               'Data da Venda' : 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)


# dados_json = leitura_dados(path_json, 'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)
# print(f"Colunas Json: {nome_colunas_json}")
# print(f"Dados Json: {tamanho_dados_json}")

# dados_csv = leitura_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)
# print(f"Colunas CSV: {nome_colunas_csv}")
# print(f"Dados CSV: {tamanho_dados_csv}")



# # Transformação dos Dados

# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)

# dados_fusao = join(dados_csv, dados_json)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(f"Colunas CSV: {nome_colunas_fusao}")
# print(f"Dados CSV: {tamanho_dados_fusao}")

# #Salvando dados

# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# salvando_dados(dados_fusao_tabela, path_dados_combinado)
# print(path_dados_combinado)

