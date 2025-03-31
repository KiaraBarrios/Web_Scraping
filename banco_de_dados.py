import sqlite3

# Conectar ao banco SQLite (se não existir, será criado)
conn = sqlite3.connect("ans_db.sqlite")
cursor = conn.cursor()

# Criar a tabela operadoras
cursor.execute("""
CREATE TABLE IF NOT EXISTS operadoras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj TEXT,
    nome_operadora TEXT,
    status TEXT,
    categoria TEXT
);
""")

# Salvar e fechar conexão
conn.commit()
conn.close()

print("✅ Banco de dados criado com sucesso!")
