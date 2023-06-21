import pandas as pd

# Carregando as tabelas clientes e produtos
clientes = pd.read_csv('clientes.csv', sep=';')
produtos = pd.read_csv('produtos.csv', sep=';')

def filtrar_tabela(clientes, produtos, nome=None, municipio=None, canal=None, acucar=None, categoria=None):
    """
    Esta função filtra as tabelas de clientes e produtos com base em valores de suas colunas. 
    É possível filtrar por nome, município, canal, açúcar e categoria.
    """
    # Filtro por nome
    if nome is not None:
        clientes = clientes[clientes['nome'].isin(nome)]
    # Filtro por município
    if municipio is not None:
        clientes = clientes[clientes['município'].isin(municipio)]
    # Filtro por canal
    if canal is not None:
        clientes = clientes[clientes['canal'].isin(canal)]
    # Filtro por açúcar
    if acucar is not None:
        produtos = produtos[~produtos['açúcar'].isin(acucar)]
    # Filtro por categoria
    if categoria is not None:
        produtos = produtos[produtos['categoria'].isin(categoria)]

    # renomear as colunas
    clientes = clientes.rename(columns={'id': 'cliente'})
    produtos = produtos.rename(columns={'id': 'produto'})

    # criar todas as combinações possíveis
    tabela_final = pd.merge(clientes.assign(key=0), produtos.assign(key=0), on='key').drop('key', axis=1)

    # Retorna apenas as colunas 'cliente' e 'produto'
    return tabela_final[['cliente', 'produto']]


def remover_descontos(cliente_desconto, clientes, produtos, nome=None, municipio=None, canal=None, acucar=None, categoria=None):
    """
    Esta função recebe uma tabela de descontos por cliente e produto, 
    filtra as tabelas de clientes e produtos com base em valores de suas colunas
    e remove os descontos aplicados aos produtos selecionados.
    """
    # Filtra a tabela com base nos parâmetros informados
    tabela_filtrada = filtrar_tabela(clientes, produtos, nome=nome, municipio=municipio, canal=canal, acucar=acucar, categoria=categoria)

    # Remove os descontos para os clientes e produtos selecionados
    cliente_desconto = cliente_desconto[~cliente_desconto.set_index(['cliente', 'produto']).index.isin(tabela_filtrada.set_index(['cliente', 'produto']).index)]

    # Retorna a tabela cliente_desconto sem os descontos aplicados aos produtos selecionados
    return cliente_desconto


cliente_desconto = pd.read_csv('cliente_desconto.csv', delimiter=';')
nova_tabela = remover_descontos(cliente_desconto, clientes, produtos, municipio=['BELÉM'], canal=['ESCOLA','UNIVERSIDADE'], acucar=['ALTO'])
