import sqlite3
conexao = sqlite3.connect("registro_treinos.db")
cursor = conexao.cursor()
data_treino = "2026-01-15"
distancia_km = 2.85
tempo_total = "25:13"
pace_medio = 8.50
cursor.execute("""
INSERT INTO treinos (data, distancia, tempo, pace)
VALUES (?, ?, ?, ?)
""", (data_treino, distancia_km, tempo_total, pace_medio))
conexao.commit()
conexao.close()
print(" Registro de treino inserido na base de dados com sucesso!")
