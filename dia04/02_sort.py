# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes["qtdePontos"].sort_values()
# %%
