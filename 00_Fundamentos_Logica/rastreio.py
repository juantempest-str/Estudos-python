import requests

print("=== SISTEMA DE RASTREIO ===")
cep_alvo = input("Informe o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep_alvo}/json/"

print(" Aguarde... ")
resposta = requests.get(url)

# 1. Blindagem de Conexão: Verifica se a internet e o site estão ok (Código 200)
if resposta.status_code == 200:
    dados = resposta.json()
    
    # 2. Blindagem de Dados: Verifica se o CEP realmente existe na base
    if "erro" in dados:
        print("\n[!] FALHA: CEP não localizado na base de dados.")
    else:
        print("\n[ DADOS INTERCEPTADOS COM SUCESSO ]")
        # O uso do .get() evita erros caso algum campo venha vazio da API
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')} - {dados.get('uf', 'N/A')}")
        print("=======================================")
else:
    print(f"\n[!] ERRO CRÍTICO: Falha na interceptação. Servidor retornou código {resposta.status_code}")