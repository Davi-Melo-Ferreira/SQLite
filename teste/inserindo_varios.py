import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("C:\davi_ferreira\SQLite_python\SQLite\insercao_muitos_bd.db")

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

dados_varios_clientes = [
    ('Maria Souza', 25),
    ('Carlos Pereira', 35),
    ('Pedro José', 28),
    ('Ana Costa', 28),
    ('Luís Gomes', 30),
    ('Fernanda Lima', 22),
    ('Roberto Silva', 40),
    ('Juliana Almeida', 33),
    ('Lucas Martins', 27),
    ('Sofia Ferreira', 31),
    ]
cursor.executemany(
    "INSERT INTO clientes (nome_cliente, idade_cliente) VALUES (?, ?)", dados_varios_clientes)
conn.commit()

conn.close()