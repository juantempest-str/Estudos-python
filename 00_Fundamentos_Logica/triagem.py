nome = input("Diga seu nome! ")
nota = float(input("Qual é a sua nota da prova teórica? "))
distancia = float(input("Qual a sua distância percorrida em metros? "))
if nota >= 7 and distancia >= 2400:
   print(f"Candidato APROVADO! Bem-vindo à equipe {nome}.")
else:
    nota < 7 or distancia < 2400
    print(f"Candidato REPROVADO.")