from tkinter import *
from tkinter import messagebox
import json
import base64


# Função para criptografar a string
def criptografar(texto):
    return base64.b64encode(texto.encode("utf-8"))


# Função para gerar o arquivo JSON
def gerar_json(texto_original, texto_criptografado):
    dados = {
        "texto_original": texto_original,
        "texto_criptografado": texto_criptografado.decode("utf-8"),
    }
    with open("criptografia.json", "w") as f:
        json.dump(dados, f, indent=4)


# Função para a ação do botão
def on_click():
    texto = entrada_texto.get()
    if not texto:
        messagebox.showerror("Erro", "Digite uma string para criptografar!")
        return

    texto_criptografado = criptografar(texto)
    gerar_json(texto, texto_criptografado)

    messagebox.showinfo("Sucesso", "Arquivo JSON gerado com sucesso!")


# Criação da interface gráfica
janela = Tk()
janela.title("Criptografia de String")
janela.geometry("300x200")

# Criação dos widgets
label_texto = Label(text="Digite a string para criptografar:")
entrada_texto = Entry()
botao_criptografar = Button(text="Criptografar e Gerar JSON", command=on_click)

# Layout dos widgets
label_texto.pack()
entrada_texto.pack()
botao_criptografar.pack()

# Execução da interface gráfica
janela.mainloop()
