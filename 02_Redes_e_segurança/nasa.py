import requests
import config
print("=== TERMINAL DE ACESSO RESTRITO ===")
chave_api = config.CHAVE_NASA
url = f"https://api.nasa.gov/planetary/apod?api_key={chave_api}"
print("Estabelecendo conexão segura com a Base de Dados da NASA...\n")
resposta = requests.get(url)
if resposta.status_code == 200:
    dados = resposta.json()
    titulo = dados['title']
    data = dados['date']
    explicacao = dados['explanation']
    print("[ ACESSO AUTORIZADO: DADOS RECEBIDOS ]")
    print(f"Data Estelar: {data}")
    print(f"Registro: {titulo}")
    print("-----------------------------------")
    print("Resumo do Relatório (Em Inglês):")
else:
    print(f"[ ACESSO NEGADO ] Código do Erro: {resposta.status_code}") 