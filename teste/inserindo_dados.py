import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("C:\davi_ferreira\SQLite_python\SQLite\meu_primeiro_bd.db")

# Para operações no banco de dados, você também precisará de um cursos,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()

# Definição de uma tupla com os dados
dados_cliente = ('João Silva', 30)

# Placeholders (?, ?): Os pontos de interrogação s]ao usados como
# "espaços reservados". Eles serão substituídos pelos valores da
# tupla dados_cliente (ou seja, "João Silva" e 30).
# Por quyê: Usar placeholder é uma prática recomendada,
# pois previne ataques de injeção de SQL.
cursor.execute("INSERT INTO clientes (nome_cliente, idade_cliente) VALUES (?, ?)", dados_cliente)

