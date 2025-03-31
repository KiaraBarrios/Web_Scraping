import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("ans_db.sqlite")
cursor = conn.cursor()

# Realizar uma consulta
cursor.execute("SELECT * FROM procedimentos LIMIT 5")
resultados = cursor.fetchall()

# Exibir resultados
for linha in resultados:
    print(linha)

conn.close()
