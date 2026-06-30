nome = input("Hey, qual o seu nome? ")
distancia = float(input("Quantos metros você correu no simualado de 12 minutos? "))
if distancia >= 2400:
    print(f"Excelente, {nome}! ìndice batido.")
else:
    metros_faltantes = 2400 - distancia
    print(f"Atenção, {nome}. Faltaram {metros_faltantes} metros. Bora apertar o pace!")