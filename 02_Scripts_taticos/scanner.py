import requests
def salvar_relatorio(nome, tipo, hp, ataque):
    with open("relatorio_capturas.txt", "a") as arquivo:
        arquivo.write(f"Alvo: {nome} | Tipo: {tipo} | HP: {hp} | ATK: {ataque}\n")
    print("[✓] Dados salvos no relatório local com sucesso!")
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
        nome_alvo = dados['name'].capitalize()
        tipo_principal = dados['types'][0]['type']['name']
        hp = dados['stats'][0]['base_stat']
        ataque = dados['stats'][1]['base_stat']
        
        print(f"\n[ REGISTRO LOCALIZADO: {nome_alvo} ]")
        print(f"Tipo Primário: {tipo_principal}")
        print(f"HP Base: {hp}")
        print(f"Ataque Base: {ataque}")
        salvar_relatorio(nome_alvo, tipo_principal, hp, ataque)
        print("-----------------------------------------\n")
        with open("relatorio_capturas.txt", "a") as arquivo:
            arquivo.write(f"Alvo: {dados['name'].capitalize()} | Tipo: {tipo_principal} | HP: {hp} | ATK: {ataque}\n")
            print("Dados salvos no relatório local com sucesso!")
    else:
       print("[ FALHA ] Alvo não localizado. Verifique a ortografia e tente novamente.\n")