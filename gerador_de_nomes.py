import random
import json

def generate_full_name():
    # Gera o número de nomes (1 ou 2) com base nas probabilidades
    num_names = random.choices([1, 2], weights=[75, 25])[0]

    # Gera o número de sobrenomes (1 a 4) com base nas probabilidades
    num_surnames = random.choices([1, 2, 3, 4], weights=[20, 60, 15, 5])[0]

    # Lista de nomes e sobrenomes fictícios
    names = [
    "João", "Maria", "Pedro", "Ana", "Carlos", "Luiza", "Miguel", "Isabela", "Rafael", "Larissa",
    "Antônio", "Camila", "Lucas", "Juliana", "Fernando", "Amanda", "Gustavo", "Bianca", "Felipe", "Vanessa",
    "José", "Renata", "Daniel", "Patrícia", "Bruno", "Aline", "André", "Monica", "Eduardo", "Jessica",
    "Marcelo", "Natália", "Thiago", "Leticia", "Ricardo", "Thais", "Guilherme", "Priscila", "Paulo", "Fernanda"
    ]

    surnames = [
    "Silva", "Santos", "Oliveira", "Pereira", "Ribeiro", "Gomes", "Almeida", "Ferreira", "Carvalho",
    "Rodrigues", "Martins", "Fernandes", "Nunes", "Monteiro", "Cavalcanti", "Vieira", "Lima", "Sousa", "Barbosa",
    "Lopes", "Costa", "Correia", "Mendes", "Dias", "Castro", "Freitas", "Pinto", "Borges", "Moraes",
    "Sousa", "Pereira", "Nascimento", "Alves", "Rocha", "Ramos", "Pires", "Machado", "Nogueira", "Cardoso"
    ]

    

    # Gera os nomes (1 ou 2) aleatoriamente
    generated_names = random.sample(names, num_names)

    # Gera os sobrenomes (1 a 4) aleatoriamente
    generated_surnames = random.sample(surnames, num_surnames)

    # Combina nomes e sobrenomes para criar o nome completo
    full_name = ' '.join(generated_names + generated_surnames)

    return full_name

# Gera um nome completo
# full_name = generate_full_name()
# print("Nome completo gerado:", full_name)

# Solicita ao usuário o número de nomes a serem gerados
num_names = int(input("Digite o número de nomess a serem gerados: "))

# Gera os nomes
name_data = []
for i in range(num_names):
    full_name = generate_full_name()
    name_data.append({"id": i + 1, "nome": full_name})

# Cria um arquivo JSON com os nomes gerados
json_filename = "names_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(name_data, json_file, ensure_ascii=False, indent=2)

print(f"{num_names} Nomes gerados e salvos em {json_filename}")