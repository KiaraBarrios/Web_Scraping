import os
import requests

# URLs dos repositórios públicos
url_demonstracoes = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
url_operadoras = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"

# Pasta onde os arquivos serão salvos
download_folder = "dados"

# Criação da pasta para salvar os arquivos
os.makedirs(download_folder, exist_ok=True)

# Função para baixar arquivos de um diretório
def baixar_arquivos(url, pasta_destino):
    response = requests.get(url)
    if response.status_code == 200:
        # Aqui, o conteúdo HTML da página é analisado para encontrar os links dos arquivos
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os links (anchor tags) na página
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and href.endswith('.csv'):  # Baixa apenas arquivos .csv
                arquivo_url = url + href
                print(f"Baixando {href}...")
                arquivo_path = os.path.join(pasta_destino, href)
                
                # Fazendo o download do arquivo
                with requests.get(arquivo_url, stream=True) as r:
                    with open(arquivo_path, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                print(f"Arquivo {href} baixado com sucesso!")
    else:
        print(f"Erro ao acessar a URL: {url}")

# Baixando os arquivos dos dois repositórios
baixar_arquivos(url_demonstracoes, download_folder)
baixar_arquivos(url_operadoras, download_folder)
