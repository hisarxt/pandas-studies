# %%
import pandas as pd

idades = [
    33, 44, 55, 33, 31,
    37, 23, 15, 23, 24
]

series_idades = pd.Series(idades)
series_idades
# %%

idades[-1]
series_idades[0]

# %%
series_idades = series_idades.sort_values()
series_idades
series_idades[0]
# %%

series_idades.iloc[0]
# %%
series_idades.iloc[-1]
# %%

series_idades.iloc[:3]
series_idades.iloc[::-1]

# %%
idades = [
    33, 44, 55, 33, 31,
    37, 23, 15, 23, 24
]

index = ["Teo", "Maria", "Jose", "Luis, Gabriel",
         "Arthur", "Amanda", "Lucio", "Leonardo", "Julio", "Pedro"
         ]

series_idades = pd.Series(idades, index=index)
series_idades
# %%
series_idades.loc["Pedro"]

# %%
