import random

# Lista de palavras secretas
palavras_secretas = ["python", "programacao", "computador", "desenvolvimento", "openai", "inteligencia"]

# Escolha aleatoriamente uma palavra secreta da lista
palavra_secreta = random.choice(palavras_secretas)

# Inicialize a variável de controle para contar tentativas
tentativas = 0

# Inicialize uma lista para armazenar as letras adivinhadas corretamente
letras_adivinhadas = []

# Função para exibir o progresso
def exibir_progresso(palavra_secreta, letras_adivinhadas):
    progresso = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            progresso += letra
        else:
            progresso += "*"
    return progresso

print("Bem-vindo ao jogo de adivinhação de palavras!")
print(exibir_progresso(palavra_secreta, letras_adivinhadas))

while True:
    # Solicita ao usuário que digite uma letra
    letra = input("Digite uma letra: ").lower()

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        letras_adivinhadas.append(letra)
    else:
        print("Letra não encontrada na palavra secreta.")

    # Exibe o progresso atual
    progresso_atual = exibir_progresso(palavra_secreta, letras_adivinhadas)
    print(progresso_atual)

    # Verifica se o usuário adivinhou a palavra
    if progresso_atual == palavra_secreta:
        print(f"Parabéns! Você adivinhou a palavra '{palavra_secreta}' em {tentativas} tentativas.")
        break
