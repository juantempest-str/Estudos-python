import sqlite3
conexao = sqlite3.connect("registro_treinos.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM treinos")
registros = cursor.fetchall()
print("=== RELATÓRIO DE TREINOS ===")
for linha in registros:
    # Cada 'linha' é uma lista com os dados na ordem em que foram criados na tabela
    id_treino = linha[0]
    data = linha[1]
    distancia = linha[2]
    tempo = linha[3]
    pace = linha[4]
    
    print(f"Treino #{id_treino} | Data: {data}")
    print(f"Distância: {distancia} km | Tempo: {tempo} | Pace médio: {pace}")
    print("---------------------------------")
conexao.close()