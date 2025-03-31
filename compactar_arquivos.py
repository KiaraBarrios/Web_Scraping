import zipfile
import os

# Arquivos para compactar
arquivos = [
    "dados_limpos.csv",
    "downloads/extraido/Teste_Kiara/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "downloads/extraido/Teste_Kiara/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

# Criar o arquivo ZIP
with zipfile.ZipFile('Teste_Kiara.zip', 'w') as zipf:
    for arquivo in arquivos:
        zipf.write(arquivo, os.path.basename(arquivo))

print("✅ Arquivos compactados com sucesso em 'Teste_Kiara.zip'")
