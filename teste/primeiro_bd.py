import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("C:\davi_ferreira\SQLite_python\SQLite\meu_primeiro_bd.db")

# Para operações no banco de dados, você também precisará de um cursos,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        idade_cliente TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos(
        telefone INTEGER not null,
        email TEXT not null
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS endereco(
        estado TEXT not null,
        cidade TEXT not null,
        bairro TEXT not null,
        rua TEXT not null
    )
''')