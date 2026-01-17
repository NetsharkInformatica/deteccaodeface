

import sqlite3

conexao = sqlite3.connect('conexaoBd/bd/bd.db')
cursor = conexao.cursor()

filmes = [
    ("O Poderoso Chefão", 1972, 9.2),
    ("Um Sonho de Liberdade", 1994, 9.3),
    ("Batman: O Cavaleiro das Trevas", 2008, 9.0),
    ("12 Homens e uma Sentença", 1957, 8.9),
    ("A Lista de Schindler", 1993, 8.9),
    ("Pulp Fiction: Tempo de Violência", 1994, 8.9),
    ("O Senhor dos Anéis: O Retorno do Rei", 2003, 8.9),
    ("Clube da Luta", 1999, 8.8),
    ("Forrest Gump: O Contador de Histórias", 1994, 8.8),
    ("Matrix", 1999, 8.7)
]

cursor.executemany("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", filmes)

conexao.commit()
conexao.close()

print("Dados inseridos com sucesso!")