# %%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

dfs = pd.read_html(html)

dfs[12]
# %%
