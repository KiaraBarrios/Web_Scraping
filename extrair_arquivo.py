import zipfile
import os

# Nome do arquivo ZIP
zip_path = "downloads/Teste_Kiara.zip"  # Ajuste esse caminho se necessário
extract_folder = "downloads/extraido"   # Pasta onde os arquivos serão extraídos

# Criar a pasta se não existir
os.makedirs(extract_folder, exist_ok=True)

# Extrair os arquivos
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_folder)

print(f"✅ Arquivos extraídos para: {extract_folder}")
