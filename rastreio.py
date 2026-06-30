import requests
print("=== SISTEMA DE RASTREIO TÁTICO ===")
cep_alvo = input("Informe o CEP do alvo (apenas números): ")
url = f"https://viacep.com.br/ws/{cep_alvo}/json/"
print("Enviando sinal para o servidor ddos Correios...")
resposta = requests.get(url)
dados = resposta.json()
print("\n[ DADOS INTERCEPTADOS COM SUCESSO]")
print(f"Logradouro:{dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']} - {dados['uf']}")
print("=======================================")