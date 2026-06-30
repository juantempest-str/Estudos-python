import requests
print("=== TERMINAL DE CONSULTA DE DADOS CONTÍNUO ===")
print("(Digite 'sair' para encerrar o programa)")
print("=========================================")
alvo = ""
while alvo!= "sair":
    alvo = input("Digite o nome da criatura e ingês:").lower()
    if alvo =="sair":
        print("\nDesconectando do banco de dados global.. Até a próxima!")
        print("=======================================================")
        break
    url = f"https://pokeapi.co/api/v2/pokemon/{alvo}"
    print("\nAcessando o banco de dados global...\n")
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        tipo_principal = dados['types'][0]['type']['name']
        hp = dados['stats'][0]['base_stat']
        ataque = dados['stats'][1]['base_stat']
        print(f"[ REGISTRO LOCALIZADO: {dados['name'].capitalize()} ]")
        print(f"Tipo Primário: {tipo_principal}")
        print(f"HP Base: {hp}")
        print(f"Ataque Base: {ataque}")
        print("==================================================")
    else:
        print("[ FALHA ] Alvo não localizado. Verifique a ortografia e tente novamente.")