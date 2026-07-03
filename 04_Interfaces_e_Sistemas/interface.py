import tkinter as tk
from tkinter import messagebox
import requests
def buscar_dados():
    pokemon = entrada.get().lower()
    if not pokemon:
        messagebox.showwarning("Aviso", "Digite o nome de um alvo!")
        return
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados['name'].capitalize()
        tipo = dados['types'][0]['type']['name']
        resultado_label.config(text=f"Alvo: {nome}\nTipo: {tipo}", fg="green")
    else:
        messagebox.showerror("Erro", "Alvo não localizado!")
# === 2. LÓGICA DE LIMPEZA (A NOVIDADE) ===
def limpar_tela():
    entrada.delete(0, tk.END)  # Apaga tudo o que foi digitado na caixa, do início (0) ao fim (END)
    resultado_label.config(text="")  # Tira o texto da etiqueta de resultado
    entrada.focus()  # Coloca o cursor piscando de volta na caixa de texto automaticamente

# === 3. CONFIGURAÇÃO DA JANELA ===
janela = tk.Tk()
janela.title("Buscador de API")
janela.geometry("400x350") # Aumentei um pouco o tamanho para caber o botão novo

instrucao = tk.Label(janela, text="Digite o termo para busca:", font=("Arial", 12))
instrucao.pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)

# Botão de Busca
botao_buscar = tk.Button(janela, text="Buscar", command=buscar_dados, bg="blue", fg="white", font=("Arial", 10, "bold"))
botao_buscar.pack(pady=10)

# Botão de Limpeza
botao_limpar = tk.Button(janela, text="Limpar", command=limpar_tela, bg="gray", fg="white", font=("Arial", 10))
botao_limpar.pack(pady=5)

resultado_label = tk.Label(janela, text="", font=("Arial", 14, "bold"))
resultado_label.pack(pady=10)

janela.mainloop()