import requests
import time
import csv

# 1. Abre (ou cria) o arquivo final que será entregue ao cliente
# O 'w' é para escrever. O 'utf-8' garante que acentos em nomes de empresas não fiquem bugados.
with open('fornecedores_extraidos.csv', 'w', newline='',encoding='utf-8') as arquivo_csv:

    # Cria o "escritor", a ferramenta que vai preencher as linhas
    escritor = csv.writer(arquivo_csv)

    # Escreve a linha de cabeçalho da planilha
    escritor.writerow(['CNPJ_Consultado', 'Razao_Social', 'Telefone'])

    # 2. Lê a lista de alvos originais
    with open('alvos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # 3. Motor de repetição
    for linha in linhas:
        cnpj_limpo = linha.strip()
        print(f'Investigando o CNPJ: {cnpj_limpo}...')

        url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            nome_empresa = dados.get('razao_social')
            telefone = dados.get('ddd_telefone_1')

            print(f'Sucesso: {nome_empresa} | Tel: {telefone}\n')

            # Salva os dados reais como uma nova linha na planilha
            escritor.writerow([cnpj_limpo, nome_empresa, telefone])
        else:
            print(f'Falha na extração. Código de status: {resposta.status_code}')
            print(f'Motivo relatado pela API: {resposta.text}\n')
        
         # Se der erro, salva na planilha também para o cliente saber qual CNPJ falhou
            escritor.writerow([cnpj_limpo, 'FALHA NA BUSCA', 'N/A'])
            
        # Fôlego de 15 segundos para evitar bloqueios do servidor
        time.sleep(15)

print('\nProcesso finalizado! A planilha fornecedores_extraidos.csv foi gerada com sucesso.')