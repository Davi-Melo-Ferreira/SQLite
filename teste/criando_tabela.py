import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("C:\davi_ferreira\SQLite_python\SQLite\meu_banco_de_dados.db")

# Para operações no banco de dados, você também precisará de um cursos,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
    ''')