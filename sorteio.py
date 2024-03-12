import random
import json

grupo = [
    "Marcos",
    "Matheus",
    "Wellington",
    "Dayane",
    "Wilmar",
    "Everton",
    "Jair",
    "Fabio",
]

exercicios = list(range(1, 19))  # lista de 1 a 18

random.shuffle(exercicios)

tamanho_parte = len(exercicios) // len(grupo)
partes = [
    exercicios[i : i + tamanho_parte] for i in range(0, len(exercicios), tamanho_parte)
]

random.shuffle(partes)
distribuicao = dict(zip(grupo, partes))

resultado = {}
for integrante, exercicios in distribuicao.items():
    resultado[integrante] = exercicios

with open("resultado_sorteio.json", "w") as f:
    json.dump(resultado, f, indent=4)

print("JSON gerado com sucesso!")
