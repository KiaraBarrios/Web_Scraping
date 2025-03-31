import requests
from bs4 import BeautifulSoup
import os
import zipfile

# URL da página da ANS
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Faz a requisição para obter o HTML da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Página acessada com sucesso!")
else:
    print("Erro ao acessar a página:", response.status_code)
    exit()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Encontra todos os links na página
links = soup.find_all("a")

# Filtra os links que levam a PDFs
pdf_links = [link["href"] for link in links if "pdf" in link.get("href", "").lower()]

if not pdf_links:
    print("Nenhum link de PDF encontrado!")
    exit()

# Criar pasta para salvar os arquivos
os.makedirs("downloads", exist_ok=True)

# Fazer o download dos PDFs
for i, pdf_url in enumerate(pdf_links[:2]):  # Pegamos apenas os dois primeiros
    pdf_response = requests.get(pdf_url)

    file_name = f"downloads/Anexo_{i+1}.pdf"
    
    with open(file_name, "wb") as file:
        file.write(pdf_response.content)

    print(f"Download concluído: {file_name}")

# Criar um arquivo ZIP
zip_file = "downloads/anexos.zip"

with zipfile.ZipFile(zip_file, "w") as zipf:
    zipf.write("downloads/Anexo_1.pdf", "Anexo_1.pdf")
    zipf.write("downloads/Anexo_2.pdf", "Anexo_2.pdf")

print(f"Arquivo ZIP criado: {zip_file}")
