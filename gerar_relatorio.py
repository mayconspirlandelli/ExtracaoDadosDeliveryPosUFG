"""
Este relatório em PDF apresenta uma análise comparativa dos cardápios de três lojas virtuais hospedadas na plataforma Goomer, com base em dados extraídos diretamente da API pública de cada estabelecimento.

As lojas analisadas foram:
- Ana Formiga Doces
- Chocolatria
- Flakes

Para cada loja, foram coletadas informações detalhadas dos produtos, incluindo:
* Nome da loja
* Categoria do produto
* Nome do produto
* Descrição
* Preço
* Imagem (URL)

A seguir, são apresentados os seguintes indicadores por loja:
✅ Quantidade total de produtos
💰 Preço médio dos produtos
🔝 Produto mais caro
🔻 Produto mais barato
"""

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Ler o CSV
df = pd.read_csv("Goomer_3Lojas.csv")
df = df.dropna(subset=["preco"])
df["preco"] = df["preco"].astype(float)

# Calcular dados
qtd_produtos = df["loja"].value_counts()
preco_medio = df.groupby("loja")["preco"].mean().round(2)
mais_caros = df.loc[df.groupby("loja")["preco"].idxmax()]
mais_baratos = df.loc[df.groupby("loja")["preco"].idxmin()]

# Criar o PDF
pdf_path = "resumo_lojas_goomer.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)
largura, altura = A4

y = altura - 50
c.setFont("Helvetica-Bold", 16)
c.drawString(50, y, "Resumo das Lojas - Goomer")

y -= 40
c.setFont("Helvetica", 12)
c.drawString(50, y, "📦 Quantidade de produtos por loja:")
for loja, qtd in qtd_produtos.items():
    y -= 20
    c.drawString(70, y, f"- {loja}: {qtd} produtos")

y -= 30
c.drawString(50, y, "💰 Preço médio por loja:")
for loja, media in preco_medio.items():
    y -= 20
    c.drawString(70, y, f"- {loja}: R$ {media:.2f}")

y -= 30
c.drawString(50, y, "🔝 Produto mais caro por loja:")
for _, row in mais_caros.iterrows():
    y -= 20
    c.drawString(70, y, f"- {row['loja']}: {row['nome']} (R$ {row['preco']:.2f})")

y -= 30
c.drawString(50, y, "🔻 Produto mais barato por loja:")
for _, row in mais_baratos.iterrows():
    y -= 20
    c.drawString(70, y, f"- {row['loja']}: {row['nome']} (R$ {row['preco']:.2f})")

# Salvar o PDF
c.save()

print(f"✅ PDF gerado com sucesso: {pdf_path}")
