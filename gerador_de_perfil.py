import random
import json

def generate_cpf():
    # Gera os oito primeiros dígitos do CPF de forma aleatória
    cpf = [random.randint(0, 9) for _ in range(8)]

    # Define a região fiscal (nono dígito) - Vamos usar a 10.ª Região Fiscal
    cpf.append(0)

    # Calcula o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += cpf[i] * (10 - i)
    remainder = total % 11
    if remainder < 2:
        cpf.append(0)
    else:
        cpf.append(11 - remainder)

    # Calcula o segundo dígito verificador
    total = 0
    for i in range(10):
        total += cpf[i] * (11 - i)
    remainder = total % 11
    if remainder < 2:
        cpf.append(0)
    else:
        cpf.append(11 - remainder)

    # Formata o CPF no padrão XXX.XXX.XXX-XX
    cpf_str = ''.join(map(str, cpf[:3])) + '.' + ''.join(map(str, cpf[3:6])) + '.' + ''.join(map(str, cpf[6:9])) + '-' + ''.join(map(str, cpf[9:11]))

    return cpf_str

def validate_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    remainder = total % 11
    if remainder < 2:
        calculated_digit = 0
    else:
        calculated_digit = 11 - remainder

    # Verifica se o primeiro dígito verificador é igual ao dígito real
    if int(cpf[9]) != calculated_digit:
        return False

    # Calcula o segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    remainder = total % 11
    if remainder < 2:
        calculated_digit = 0
    else:
        calculated_digit = 11 - remainder

    # Verifica se o segundo dígito verificador é igual ao dígito real
    if int(cpf[10]) != calculated_digit:
        return False

    return True

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

# Porcentagens por faixa etária
percentages = {
    "0-14 anos": 28.2,
    "15-24 anos": 45.7,
    "25-54 anos": 50.6,
    "55-64 anos": 6.2,
    "65 anos ou mais": 9.5
}

# Função para gerar idade aleatória com base nas porcentagens
def generate_random_age():
    rand_num = random.uniform(0, 100)  # Gera um número aleatório entre 0 e 100

    if rand_num <= percentages["0-14 anos"]:
        return random.randint(0, 14)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"]:
        return random.randint(15, 24)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"] + percentages["25-54 anos"]:
        return random.randint(25, 54)
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"] + percentages["25-54 anos"] + percentages["55-64 anos"]:
        return random.randint(55, 64)
    else:
        return random.randint(65, 100)

# Solicita ao usuário o número de perfis a serem gerados
num_perfil = int(input("Digite o número de perfis a serem gerados: "))

# Gera os perfis
perfis_data = []
for i in range(num_perfil):
    full_name = generate_full_name()
    cpf = generate_cpf()
    is_valid = validate_cpf(cpf)
    idade = generate_random_age()
    perfis_data.append({"id": i + 1, "nome": full_name, "Idade": idade, "cpf": cpf, "valid": is_valid, })

# Cria um arquivo JSON com os nomes gerados
json_filename = "perfis_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"{num_perfil} Perfis gerados e salvos em {json_filename}")