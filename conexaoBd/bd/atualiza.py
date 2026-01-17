import sqlite3


conexao= sqlite3.connect("conexaoBd/bd/bd.db")

cursor = conexao.cursor()
id = 1
cursor.execute("""
                      UPDATE filmes SET nome=?
                      WHERE id=?
                      """,
                      ('O Poderoso Chefinho ',id)
                      
                      
                      
                      
                      )
conexao.commit()
conexao.close()

print("dados atualizados com sucesso")

