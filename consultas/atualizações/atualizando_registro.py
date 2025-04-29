import os
import sqlite3

conn = sqlite3.connect('insercao_muitos_bd.db')

cursor = conn.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente: ')
idade_cliente = int(input('Digite a idade do cliente: '))

# Executa a exclusão com base no nome fornecido pelo usuário
cursor.execute('UPDATE clientes SET idade_cliente = ? WHERE nome_cliente = ?', (idade_cliente, nome_cliente))

# Salva as alterações no banco de dados
conn.commit()
print('Dados atualizados com sucesso!')
conn.close()
