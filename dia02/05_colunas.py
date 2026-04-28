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
df

# %%
