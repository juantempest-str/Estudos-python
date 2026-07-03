import sqlite3
conexao = sqlite3.connect ("registro_treinos.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS treinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    distancia REAL NOT NULL,
    tempo TEX NOT NULL,
    pace REAL NOT NULL
)
""")
conexao.commit()
conexao.close()
print(" Base de dados e tabela de treinos estruturadas com sucesso!")