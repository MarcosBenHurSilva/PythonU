import json
from password_generator import generate_password

# Gera os perfis
perfis_data = []
site = input("Para qual serviço deseja gerar a senha: ")
user = input("Qual o user ou email deste serviço: ")
senha = generate_password(12, any, any, any, any)

perfis_data.append(
    {"Site": site, "User": user, "Senha": senha})
    
json_filename = "login_data_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"Dados de login gerados e salvos em {json_filename}")