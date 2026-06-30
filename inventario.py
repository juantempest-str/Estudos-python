lista_compras = ["arroz", "feijão", "macarrão"]
print(f"Não esqueça de trazer o {lista_compras[2]}.")
lista_compras.append("azeite")
lista_compras.append("frutas")
for item in lista_compras:
    print(f" - {item}")