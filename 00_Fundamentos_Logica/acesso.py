# Sistema de senhas, desenvolvi pra aprender o uso de while, if e else

senha_digitada = ""
while senha_digitada != "777":
    senha_digitada = input("Digite a senha de acesso ao sistema:  ")
    if senha_digitada != "777":
        print(f"Acesso negado. Tente novamente!")
        print(f"-------------------------------------")
    else:
        print(f"Acesso concedido! Bem-vindo ao sistema.")