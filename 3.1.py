# Para veriicar as tabelas renomear cliente_desconto.csv para cliente_desconto_verifica.csv

import pandas as pd

# Carregar arquivos CSV
descontos_df = pd.read_csv('descontos.csv', delimiter=';')
clientes_df = pd.read_csv('clientes.csv', delimiter=';')

# Criar tabela com todas as combinações possíveis de clientes e descontos
produtos_df = pd.read_csv('produtos.csv', delimiter=';')
produtos_descontos_df = pd.merge(produtos_df, descontos_df, left_on='id', right_on='produto')
produtos_descontos_df = produtos_descontos_df.drop('produto', axis=1) # remover coluna duplicada
cliente_desconto_df = pd.merge(clientes_df.assign(key=1), produtos_descontos_df.assign(key=1), on='key').drop('key', axis=1)

# Renomear coluna id para clientes
cliente_desconto_df = cliente_desconto_df.rename(columns={'id_x': 'cliente', 'id_y': 'produto'})

# Salvar resultado em um arquivo CSV com delimiter ';'
cliente_desconto_df.to_csv('cliente_desconto.csv', columns=['cliente', 'produto', 'caixas', 'desconto'], index=False, sep=';')

# Ler arquivos para verificar se são iguais
verifica_df = pd.read_csv('cliente_desconto_verifica.csv', delimiter=';')
cliente_desconto_verificado_df = pd.read_csv('cliente_desconto.csv', delimiter=';')

# Verificar se as tabelas são iguais linha por linha
for i, row in verifica_df.iterrows():
    if not row.equals(cliente_desconto_verificado_df.iloc[i]):
        print(f'Linha {i} é diferente:')
        print(f'cliente_desconto_verificado_df: {cliente_desconto_verificado_df.iloc[i]}')

print(verifica_df.equals(cliente_desconto_verificado_df))
