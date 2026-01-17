import sqlite3


conexao= sqlite3.connect("conexaoBd/bd/bd.db")

cursor = conexao.cursor()

id=5
cursor.execute("""DELETE FROM filmes WHERE id in (?)""",
              ( id, )
               
               )
conexao.commit()
conexao.close()

print("dados excluidos com sucesso")