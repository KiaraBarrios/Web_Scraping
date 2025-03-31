import sqlite3
import pandas as pd

# Conectar ao banco SQLite
conn = sqlite3.connect("ans_db.sqlite")
cursor = conn.cursor()

# Ler o CSV
df = pd.read_csv("downloads/extraido/Rol_Procedimentos.csv")

# Inserir os dados na tabela operadoras
for _, row in df.iterrows():
    cursor.execute("INSERT INTO operadoras (cnpj, nome_operadora, status, categoria) VALUES (?, ?, ?, ?)", 
                   (row['CNPJ'], row['Nome da Operadora'], row['Status'], row['Categoria']))

# Salvar e fechar conexão
conn.commit()
conn.close()

print("✅ Dados importados com sucesso!")
