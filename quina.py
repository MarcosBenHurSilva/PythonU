import random


def gerar_jogo_quina():
    # Gera uma lista com 5 números únicos sorteados entre 1 e 80
    return sorted(random.sample(range(1, 81), 5))


def gerar_varios_jogos(quantidade):
    jogos = []
    for _ in range(quantidade):
        jogos.append(gerar_jogo_quina())
    return jogos


# Exemplo de uso
quantidade_de_jogos = int(input("Quantos jogos deseja gerar? "))
jogos = gerar_varios_jogos(quantidade_de_jogos)

print(f"\nGerando {quantidade_de_jogos} jogos da Quina:")
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")
