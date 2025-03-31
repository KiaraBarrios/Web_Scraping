import pdfplumber
import pandas as pd
import os
import zipfile

# Nome do arquivo PDF que baixamos na parte 1
pdf_path = "downloads/Anexo_1.pdf"

# Criando uma lista para armazenar os dados extraídos
data = []

# Abrindo o PDF com pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()  # Extrai todas as tabelas da página

        for table in tables:
            for row in table:
                data.append(row)  # Adiciona cada linha da tabela na lista

# Criando um DataFrame do Pandas para organizar os dados
df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
csv_path = "downloads/Rol_Procedimentos.csv"
df.to_csv(csv_path, index=False, encoding="utf-8")

print(f"Arquivo CSV salvo em: {csv_path}")

# Compactando o CSV em um ZIP
zip_path = f"downloads/Teste_Kiara.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    zipf.write(csv_path, "Rol_Procedimentos.csv")

print(f"Arquivo ZIP criado em: {zip_path}")
