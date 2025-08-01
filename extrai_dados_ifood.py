"""
Este código apresenta a extração de dados do cardápio de uma loja hospedada na plataforma Ifood.

Para cada loja, foram coletadas informações detalhadas dos produtos, incluindo:
* Nome da loja
* Categoria do produto
* Nome do produto
* Descrição
* Preço
* Imagem (URL)
"""

import requests
import pandas as pd

# URL da API
url = "https://marketplace.ifood.com.br/v1/merchants/20d0c430-c2d7-483c-ad05-ed3b0e30cac5/catalog?latitude=-16.768919886217024&longitude=-49.31998891293492"

# Requisição à API
response = requests.get(url)
data = response.json()

# Lista para armazenar os dados
produtos = []

# Iterar pelas categorias e itens
for categoria in data['data']['menu']:
    categoria_nome = categoria['name']
    for item in categoria['itens']:
        nome = item.get('description', '').strip()
        detalhes = item.get('details', '').strip()
        preco = item.get('unitPrice', 0)
        imagem = item.get('logoUrl', '')
        if imagem:
            imagem = f"https://static.ifood-static.com.br/image/upload/t_medium/pratos/{imagem}"

        produtos.append({
            'categoria': categoria_nome,
            'nome': nome,
            'descricao': detalhes,
            'preco': preco,
            'imagem_url': imagem
        })

# Criar DataFrame
df = pd.DataFrame(produtos)

# Salvar em CSV
df.to_csv('Ifood.csv', index=False, encoding='utf-8-sig')

print("Arquivo Ifood.csv salvo com sucesso!")
