import sqlite3

# Use a relative path with .db or .sqlite extension instead
conexao = sqlite3.connect('conexaoBd/bd/bd.db')  # or use 'bd.sqlite'

cursor = conexao.cursor()  # First create the cursor

# Then execute the SQL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        ano VARCHAR(4) NOT NULL,
        nota VARCHAR(3) NOT NULL
    );
""")

conexao.commit()  # Don't forget to commit changes
conexao.close()
print('Tabela criada')