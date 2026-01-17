import sqlite3




def conecta_db():
    conexao= sqlite3.connect('C:/Users/SingSCS/Documents/PythonProjects/deteccaodeface/streamlitSite/bDados/filmes.db')
    return conexao

def inserir_dados(nome,ano,nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
        );
    """)
    cursor.execute('INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)', (nome,ano, nota))

    conexao.commit()
    conexao.close()
    
def lista_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(""" SELECT * FROM FILMES""")
    dados = cursor.fetchall()
    
    cursor.close()
    return dados
    
    
