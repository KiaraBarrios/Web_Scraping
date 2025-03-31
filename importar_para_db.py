import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite (ou criar o banco se não existir)
conn = sqlite3.connect("ans_db.sqlite")
cursor = conn.cursor()

# Criar tabela no banco (caso não exista)
cursor.execute('''
CREATE TABLE IF NOT EXISTS procedimentos (
    id INTEGER PRIMARY KEY,
    procedimento TEXT,
    OD TEXT,
    AMB TEXT,
    HCO TEXT,
    REF TEXT,
    PAC TEXT,
    DUT TEXT,
    SUBGRUPO TEXT,
    GRUPO TEXT,
    CAPITULO TEXT
)
''')

# Carregar os dados limpos
df = pd.read_csv("dados_limpos.csv")

# Inserir dados no banco
df.to_sql('procedimentos', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("✅ Dados importados para 'ans_db.sqlite' com sucesso!")
