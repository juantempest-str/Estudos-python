nome = input("Olá, qual é o seu nome? ")
saldo = float(input("Qual é o saldo atual do seu cartão? "))
passagem = float(input("Qual é o valor da passagem? "))
if saldo >= passagem:
    novo_saldo = saldo - passagem
    print(f"Catraca liberada, seu novo saldo é R$ {novo_saldo} ")
elif saldo == 0:
    print(f"Cartão zerado {nome}. Recarregue imediatamnete!")
else:
    falta = passagem - saldo
    print(f"Saldo insuficiente. Faltam R$ {falta} para a passagem.")