import pdfplumber
import pandas as pd

# Caminho dos PDFs
pdf_paths = [
    "downloads/extraido/Teste_Kiara/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "downloads/extraido/Teste_Kiara/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

# Função para extrair tabelas de um PDF
def extrair_tabelas_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        todas_as_tabelas = []
        for page in pdf.pages:
            tabela = page.extract_table()
            if tabela:
                todas_as_tabelas.append(tabela)
        return todas_as_tabelas

# Extrair dados e salvar no CSV
todas_as_tabelas = []

for pdf_path in pdf_paths:
    tabelas = extrair_tabelas_pdf(pdf_path)
    for tabela in tabelas:
        # Convertendo a tabela em DataFrame
        df = pd.DataFrame(tabela[1:], columns=tabela[0])
        todas_as_tabelas.append(df)

# Concatenando todas as tabelas extraídas em um único DataFrame e resetando os índices
df_final = pd.concat([df.reset_index(drop=True) for df in todas_as_tabelas], ignore_index=True)

# Salvando os dados extraídos em um arquivo CSV
df_final.to_csv("dados_extraidos.csv", index=False)

print("Dados extraídos e salvos com sucesso!")
