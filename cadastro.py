itens_inspecao = []
comando = ""
print("Bem-vindo ao Sistema de Cadastro. (Digite 'sair' para encerrar)")
print("--------------------------------------------------------------")
while comando != "sair":
    comando = input("Cadastre um item: ")
    if comando != "sair":
        itens_inspecao.append(comando)
        print(f" -> '{comando}' adicionado com sucesso! \n")
print("\n=== RELATÓRIO FINAL DE INSPEÇÃO ===")
for item in itens_inspecao:
    print(f" [X] {item}")