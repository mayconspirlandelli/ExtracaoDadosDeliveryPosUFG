"""
Extrator de Produtos de Lojas Goomer

Este script realiza a extração automatizada de dados de três lojas virtuais hospedadas na plataforma Goomer.

Lojas analisadas:
- Ana Formiga Doces
- Chocolatria
- Flakes

Para cada loja, o script coleta os seguintes dados de cada produto:
- Nome da loja
- Categoria do produto
- Nome do produto
- Descrição do produto
- Preço
- URL da imagem

Os dados coletados são armazenados em um DataFrame do pandas e salvos em um arquivo CSV chamado "Goomer.csv".

Dependências:
- requests
- pandas

Saída:
- Um arquivo CSV com todos os produtos extraídos e suas informações organizadas.

Uso típico:
- Análise comparativa de cardápios
- Visualização de preços por loja
- Processamento posterior (ex: geração de relatórios, exportação para PDF/TXT)

Autor: Maycon Spirlandelli
Data: 15/06/2025
"""

import requests
import pandas as pd

# Lista de URLs e nomes das lojas
lojas = {
    "Ana Formiga Doces": "https://www.goomer.app/webmenu/anaformigadoces/menu/1750463338997?provider=ggo",
    "Chocolatria": "https://www.goomer.app/webmenu/chocolatria-1/menu/1750362019152?provider=ggo",
    "Flakes": "https://www.goomer.app/webmenu/flakes/menu/1749676579107?provider=ggo"
}

# Lista para armazenar todos os produtos
todos_produtos = []

# Iterar sobre cada loja e sua URL
for nome_loja, url in lojas.items():
    response = requests.get(url)
    data = response.json()

    for item in data.get("products", []):
        categoria = item.get("group_name", "")
        nome = item.get("name", "").strip()
        descricao = item.get("description", "").strip()
        preco = item["prices"][0]["price"] if item.get("prices") else None
        imagem = item["images"].get("medium", "") if item.get("images") else ""

        todos_produtos.append({
            "loja": nome_loja,
            "categoria": categoria,
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
            "imagem": imagem
        })

# Criar DataFrame
df = pd.DataFrame(todos_produtos)

# Salvar como CSV
df.to_csv("Goomer_3Lojas.csv", index=False, encoding="utf-8-sig")

# Exibir os primeiros registros
print(df.head())
