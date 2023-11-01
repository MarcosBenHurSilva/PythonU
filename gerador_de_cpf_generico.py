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

# Solicita ao usuário o número de CPFs a serem gerados
num_cpfs = int(input("Digite o número de CPFs a serem gerados: "))

# Gera e valida os CPFs
cpf_data = []
for i in range(num_cpfs):
    cpf = generate_cpf()
    is_valid = validate_cpf(cpf)
    cpf_data.append({"id": i + 1, "cpf": cpf, "valid": is_valid})

# Cria um arquivo JSON com os CPFs gerados
json_filename = "cpfs_generated.json"
with open(json_filename, "w") as json_file:
    json.dump(cpf_data, json_file, indent=2)

print(f"{num_cpfs} CPFs gerados e salvos em {json_filename}")
