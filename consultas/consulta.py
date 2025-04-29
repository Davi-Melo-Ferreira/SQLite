import os 
import sqlite3

# conexão com o banco de dados
conn = sqlite3.connect("C:\davi_ferreira\SQLite_python\SQLite\insercao_muitos_bd.db")

# Para operações no banco de dados, você também precisará de um cursor,
# objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conn.close()
