# %%
import pandas as pd

idades = [
    33, 44, 55, 33, 31,
    37, 23, 15, 23, 24
]

series_idades = pd.Series(idades)
series_idades
# %%

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades
# %%
