import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("meu_banco_de_dados.bd")

# Para operações no banco de dados, você também precisará de um cursos,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()
