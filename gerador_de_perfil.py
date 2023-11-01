import random
import json
from openpyxl import Workbook


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
    cpf_str = ''.join(map(str, cpf[:3])) + '.' + ''.join(map(str, cpf[3:6])) + '.' + ''.join(
        map(str, cpf[6:9])) + '-' + ''.join(map(str, cpf[9:11]))

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


# Lista de nomes masculinos
male_names = [
    "João", "Pedro", "Carlos", "Miguel", "Rafael",
    "Antônio", "Lucas", "Fernando", "Gustavo", "Felipe",
    "José", "Daniel", "Bruno", "André", "Eduardo",
    "Marcelo", "Thiago", "Ricardo", "Guilherme", "Paulo",
    "Roberto", "Vinícius", "Fábio", "Sérgio", "Ronaldo",
    "Gilberto", "Samuel", "Leandro", "Márcio", "Carlos",
    "Vitor", "Diego", "Luciano", "Raul", "Wagner",
    "Felipe", "Alexandre", "Lucas", "César", "Ricardo",
    "Caio", "Leonardo", "Renato", "Giovanni", "Joaquim",
    "Luis", "Hugo", "Fernando", "Raul", "Antônio",
    "Alberto", "Isaac", "Elias", "Thiago", "Sebastião",
    "Geraldo", "Álvaro", "Armando", "Arnaldo", "Vicente",
    "Roberto", "Sergio", "Wagner", "Anderson"
]

# Lista de nomes femininos
female_names = [
    "Maria", "Ana", "Luiza", "Isabela", "Larissa",
    "Camila", "Juliana", "Amanda", "Bianca", "Vanessa",
    "Renata", "Patrícia", "Aline", "Mônica", "Jessica",
    "Natália", "Leticia", "Thais", "Priscila", "Fernanda",
    "Andréa", "Cristina", "Cecília", "Helena", "Larissa",
    "Simone", "Mariana", "Cátia", "Tatiana", "Flávia",
    "Andressa", "Eduarda", "Rafaela", "Elaine", "Laura",
    "Vanessa", "Sandra", "Mônica", "Regina", "Larissa",
    "Isabela", "Márcia", "Tatiane", "Lorena", "Carla",
    "Patrícia", "Jéssica", "Ana", "Sueli", "Thais",
    "Priscila", "Fernanda", "Larissa", "Roberta", "Carolina",
    "Brenda", "Nathalia", "Amanda", "Karla", "Simone",
    "Valéria", "Eduarda", "Mariana", "Rosana", "Tânia"
]

# Lista de sobrenomes
surnames = [
    "Silva", "Santos", "Oliveira", "Pereira", "Ribeiro", "Gomes", "Almeida", "Ferreira", "Carvalho",
    "Rodrigues", "Martins", "Fernandes", "Nunes", "Monteiro", "Cavalcanti", "Vieira", "Lima", "Sousa", "Barbosa",
    "Lopes", "Costa", "Correia", "Mendes", "Dias", "Castro", "Freitas", "Pinto", "Borges", "Moraes",
    "Sousa", "Pereira", "Nascimento", "Alves", "Rocha", "Ramos", "Pires", "Machado", "Nogueira", "Cardoso",
    "Andrade", "Ribeira", "Ferreira", "Mendes", "Correia", "Carvalho", "Lima", "Fernandes", "Barros", "Campos",
    "Moraes", "Nascimento", "Almeida", "Gonçalves", "Cavalcanti", "Vieira", "Dias", "Santana", "Pessoa", "Gomes",
    "Ramos", "Martins", "Rocha", "Nunes", "Lopes", "Dias", "Lima", "Carvalho", "Ribeira", "Andrade",
    "Ferreira", "Sousa", "Pereira", "Freitas", "Cardoso", "Pinto", "Santos", "Machado", "Nascimento", "Nogueira",
    "Borges", "Silveira", "Costa", "Alves", "Araújo", "Melo", "Gouveia", "Azevedo", "Campos", "Gonçalves"
]

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
    elif rand_num <= percentages["0-14 anos"] + percentages["15-24 anos"] + percentages["25-54 anos"] + percentages[
        "55-64 anos"]:
        return random.randint(55, 64)
    else:
        return random.randint(65, 100)


# Função para gerar gênero aleatório com base nas porcentagens
def generate_random_gender():
    gender = random.choices(["Masculino", "Feminino", "Não-Binário"], weights=[45, 48, 2])[0]
    return gender


def generate_name_by_gender(gender):
    num_names = random.choices([1, 2], weights=[75, 25])[0]
    num_surnames = random.choices([1, 2, 3, 4], weights=[20, 60, 15, 5])[0]

    if gender == "Masculino":
        first_name = random.choice(male_names)
    elif gender == "Feminino":
        first_name = random.choice(female_names)
    else:  # Gênero não-binário
        first_name = random.choice(random.choice([male_names, female_names]))

    last_names = random.sample(surnames, num_surnames)
    full_name = [first_name] + last_names[:num_names]

    return ' '.join(full_name)


# Solicita ao usuário o número de perfis a serem gerados
num_perfil = int(input("Digite o número de perfis a serem gerados: "))

# Gera os perfis
perfis_data = []
for i in range(num_perfil):
    gender = generate_random_gender()
    full_name = generate_name_by_gender(gender)
    cpf = generate_cpf()
    is_valid = validate_cpf(cpf)
    idade = generate_random_age()
    perfis_data.append(
        {"id": i + 1, "nome": full_name, "Idade": idade, "gender": gender, "cpf": cpf, "valid": is_valid})

# Cria um arquivo JSON com os perfis gerados
json_filename = "perfis_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"{num_perfil} Perfis gerados e salvos em {json_filename}")

# Crie um arquivo de planilha
wb = Workbook()
ws = wb.active

# Adicione cabeçalhos
ws.append(["ID", "Nome", "Idade", "Gênero", "CPF"])

# Adicione os perfis aos dados
for perfil in perfis_data:
    ws.append([perfil["id"], perfil["nome"], perfil["Idade"], perfil["gender"], perfil["cpf"]])

# Especifique o caminho do arquivo .xls
xls_filename = "perfis_generated_openpyxl.xlsx"

# Salve a planilha no arquivo
wb.save(xls_filename)

print(f"{num_perfil} Perfis gerados e salvos em {xls_filename}")