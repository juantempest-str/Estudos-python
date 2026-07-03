import os
import requests
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

print('Buscando a inspiração do dia...\n')

url = 'https://zenquotes.io/api/random'
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()[0]
    frase = dados.get('q')
    autor = dados.get('a')
    mensagem_final = f'"{frase}"\n- {autor}'
    print('Sucesso! A mensagem de hoje será:')
    print(mensagem_final)

else:
    print('Erro ao buscar a frase. Usando frase de backup.')
    mensagem_final = '"A disciplina é a ponte entre metas e realizações."\n- Jim Rohn'

EMAIL_ORIGEM = os.getenv('MEU_EMAIL')
SENHA_APP = os.getenv('MINHA_SENHA')
EMAIL_DESTINO = os.getenv('EMAIL_DESTINO')

# TESTE: Mostra o que o Python conseguiu ler (depois apague isso!)
print(f'Email lido: {EMAIL_ORIGEM}')
print(f'Senha lida: {SENHA_APP}')

msg = EmailMessage()
msg['Subject'] = 'Sua dose de motivação diária! '
msg['From'] = EMAIL_ORIGEM
msg['To'] = EMAIL_DESTINO
msg.set_content(mensagem_final)

print('\nConectando aoservidor do Google...')

try:
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(EMAIL_ORIGEM, SENHA_APP)
    servidor.send_message(msg)
    servidor.quit()
    print('O Bot acabou de enviar a mensagem para a caixa de entrada.')

except Exception as erro:
    print(f'Houve uma falha no envio: {erro}')
