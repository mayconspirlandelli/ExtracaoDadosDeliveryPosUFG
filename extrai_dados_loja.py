# Extraçao de dados de apenas uma loja do Goomer
import requests
import pandas as pd

# URL do JSON da Goomer
# Problema, quando o cardápio é atualizado, uma nova URL é gerada, no caso o código da página é alterado.
#url = "https://www.goomer.app/webmenu/anaformigadoces/menu/1750013787498?provider=ggo"
#url = "https://www.goomer.app/webmenu/anaformigadoces/menu/1750463338997?provider=ggo"
url = "https://www.goomer.app/webmenu/anaformigadoces/menu/1750463413265?provider=ggo"


# Requisição
response = requests.get(url)
data = response.json()

# Lista para armazenar os dados dos produtos
produtos = []

# Iterar sobre a lista de produtos
for item in data["products"]:
    categoria = item.get("group_name", "")
    nome = item.get("name", "").strip()
    descricao = item.get("description", "").strip()
    preco = item["prices"][0]["price"] if item.get("prices") else None
    imagem = item["images"].get("medium", "") if item.get("images") else ""

    produtos.append({
        "categoria": categoria,
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "imagem": imagem
    })

# Criar DataFrame
df = pd.DataFrame(produtos)

# Salvar CSV
df.to_csv("goomer.csv", index=False, encoding="utf-8-sig")

# Visualizar os primeiros dados
print(df.head())
