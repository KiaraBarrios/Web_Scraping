import pandas as pd

# Carregar os dados
df = pd.read_csv("dados_extraidos.csv")

# Substituir abreviações
df['OD'] = df['OD'].replace({
    'HCO': 'Hospitais',
    'AMB': 'Ambulatorial',
    # Adicione outras substituições conforme necessário
})

# Salvar os dados limpos
df.to_csv("dados_limpos.csv", index=False)
print("✅ Dados limpos e salvos em 'dados_limpos.csv'")
