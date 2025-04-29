import os
import sqlite3

conn = sqlite3.connect('insercao_muitos_bd.db')

cursor = conn.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente para excluir: ')

# Executa a exclusão com base no nome fornecido pelo usuário
cursor.execute('DELETE FROM clientes WHERE nome_cliente = ?', (nome_cliente,))
conn.commit()

print('Cliente deletado com sucesso!')

# Fecha a connexão
conn.close()