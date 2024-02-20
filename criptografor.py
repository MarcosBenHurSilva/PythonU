import json
import base64
import PySimpleGUI as sg


# Função para criptografar a string
def criptografar(texto):
    return base64.b64encode(texto.encode("utf-8")).decode("utf-8")


# Função para gerar o arquivo JSON
def gerar_json(texto_original, texto_criptografado):
    dados = {
        "texto_original": texto_original,
        "texto_criptografado": texto_criptografado,
    }
    with open("criptografia.json", "w") as f:
        json.dump(dados, f, indent=4)


# Layout da interface
layout = [
    [sg.Text("Digite a string para criptografar:", size=(30, 1))],
    [sg.InputText(key="texto_original")],
    [sg.Button("Criptografar e Gerar JSON")],
    [sg.Text("Resultado:", size=(30, 1))],
    [sg.Multiline(key="resultado", disabled=True)],
]

# Criação da janela
janela = sg.Window("Criptografia de String", layout)

# Loop da interface
while True:
    # Leitura dos eventos
    evento, valores = janela.read()

    # Se o botão for clicado
    if evento == "Criptografar e Gerar JSON":
        texto_original = valores["texto_original"]
        texto_criptografado = criptografar(texto_original)
        gerar_json(texto_original, texto_criptografado)

        # Atualização da interface com o resultado
        janela["resultado"].update(f"{texto_criptografado}")

    # Se o usuário fechar a janela
    if evento == sg.WIN_CLOSED:
        break

# Fechamento da janela
janela.close()
