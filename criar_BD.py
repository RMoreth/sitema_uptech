import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Leitura do arquivo setup.sql
with open('setup.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Execução do script SQL
cursor.executescript(sql_script)

# Fechando a conexão
conn.commit()
conn.close()

print("Banco de dados configurado com sucesso!")
