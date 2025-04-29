import os 
import sqlite3
from prettytable import PrettyTable

# conexão com o banco de dados
conn = sqlite3.connect("insercao_muitos_bd.db")

# Para operações no banco de dados, você também precisará de um cursor,
# objeto que permite executar comandos SQL.
cursor = conn.cursor()

cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()

os.system('cls')

# Cria a tabela prettytable e define os nomes das colunas
tabela = PrettyTable()
# Obtém os nomes das colunas a partir de cursor.description
colunas = [descricao[0] for descricao in cursor.description]
# Define os nomes das colunas na tabela PrettyTable
tabela.field_names = colunas

# Adiciona as linhas à tabela
for row in resultados:
    tabela.add_row(row)
    
print(tabela)
conn.close()