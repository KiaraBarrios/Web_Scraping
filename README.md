# Web Scraping - Teste de Nivelamento

Este repositório contém a solução para o teste de nivelamento da área de desenvolvimento, com foco em Web Scraping, Transformação de Dados, Banco de Dados, e integração com API. 

## Descrição

O projeto abrange as seguintes etapas:

1. **Web Scraping**: 
   - Acesso ao site da ANS.
   - Download dos anexos I e II.
   - Extração de informações dos PDFs.
   - Salvar os dados extraídos em formato CSV.

2. **Transformação de Dados**:
   - Limpeza dos dados extraídos.
   - Substituição de abreviações por descrições completas.
   - Salvamento dos dados limpos em CSV.

3. **Banco de Dados**:
   - Criação de banco de dados SQLite.
   - Importação dos dados para o banco.
   - Consultas para verificar os dados importados.

4. **Compactação**:
   - Compactação de todos os arquivos e dados extraídos em um único arquivo `.zip`.

## Tecnologias Usadas

- Python
  - pdfplumber
  - pandas
  - sqlite3
  - zipfile
  - GitHub
  - Git

## Como Rodar

### Requisitos

- Python 3.x
- Biblioteca `pdfplumber`, `pandas` (Instalar com `pip install pdfplumber pandas`)

### Rodando o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/KiaraBarrios/Web_Scraping.git

2. Navegue até o diretório do projeto
   cd Web_Scraping

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   python -m venv .venv
   source .venv/bin/activate  # Para Windows, use .venv\Scripts\activate

4. Instale as dependências:
   pip install -r requirements.txt
   
5. Execute os scripts conforme a ordem abaixo:
- extrair_pdf_para_csv.py: Extrai dados dos PDFs e salva em CSV.
- limpar_dados.py: Limpa e estrutura os dados.
- importar_para_db.py: Importa os dados para um banco de dados SQLite.
- compactar_arquivos.py: Compacta os arquivos em um arquivo ZIP.

6. Verifique os resultados:
   Os arquivos serão gerados nas pastas apropriadas, incluindo os dados limpos em CSV e o arquivo ZIP.

### Licença
Este projeto é de uso pessoal e não possui uma licença específica.


### Como adicionar ao seu repositório:
1. Crie um arquivo chamado `README.md` no diretório raiz do seu projeto.
2. Copie e cole o conteúdo acima no arquivo.
3. Salve e suba para o repositório:
   ```bash
   git add README.md
   git commit -m "Adiciona README"
   git push
