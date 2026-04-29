# %% 
import pandas as pd
# %%
df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df
# %%

filter = (df["IdProduto"] == "5") | (df["IdProduto"] == "11")
df[filter]
# %%

filter = df["IdProduto"].isin(["5", "11"])
df[filter]
# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

filter = clientes["DtCriacao"].notna()
clientes[filter]
# %%

~clientes["DtCriacao"].isna()
clientes[filter]
# %%
