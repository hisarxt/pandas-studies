# %%

import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv")
df
# %%

df.shape
# %%

df.info(memory_usage='deep')
# %%
df.dtypes
# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")

renamed_columns={
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}

df = df.rename(columns=renamed_columns)
# %%
df[["IdCliente", "qtPontos"]]

# %%

df[["IdCliente", "qtPontos"]].tail(5)
# %%
df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)
# %%

colunas = df.columns.to_list()
colunas.sort()
colunas

df = df[colunas]
df
# %%
