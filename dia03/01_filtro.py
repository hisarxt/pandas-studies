# %%
import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%

filter = df["QtdePontos"] >= 50
df[filter]
# %%

# valores entre 50 e 100
filter = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filter] 

# %%

filter = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filter]
# %%
