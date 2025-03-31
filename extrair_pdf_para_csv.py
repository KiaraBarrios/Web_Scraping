import pdfplumber
import csv

# Caminho para o PDF
pdf_path = "downloads/extraido/Teste_Kiara/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Abrir o PDF
with pdfplumber.open(pdf_path) as pdf:
    with open("dados_extraidos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for page in pdf.pages:
            # Extrair a tabela de cada página
            tabelas = page.extract_tables()
            for tabela in tabelas:
                writer.writerows(tabela)

print("Dados extraídos e salvos com sucesso em 'dados_extraidos.csv'")
