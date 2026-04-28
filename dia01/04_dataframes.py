# %% 
import pandas as pd

idades = [
    33, 44, 55, 33, 31,
    37, 23, 15, 23, 24
]

nomes = ["Teo", "Maria", "Jose", "Luis",
         "Arthur", "Amanda", "Lucio", "Leonardo", "Julio", "Pedro"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_idades
# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

# %%

df.iloc[0]["nomes"]


# %%
