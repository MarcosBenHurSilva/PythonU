import json
from password_generator import generate_password
from pymongo import MongoClient

# Gera os perfis
perfis_data = []
site = input("Para qual serviço deseja gerar a senha: ")
user = input("Qual o user ou email deste serviço: ")
senha = generate_password(16, any, any, any, any)

perfis_data.append(
    {"Site": site, "User": user, "Senha": senha})

json_filename = "login_data_generated.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(perfis_data, json_file, ensure_ascii=False, indent=2)

print(f"Dados de login gerados e salvos em {json_filename}")

# Conecta ao MongoDB (certifique-se de ter o servidor MongoDB em execução)
client = MongoClient('mongodb://localhost:27017')

# Escolhe ou cria um banco de dados e uma coleção
db = client['Gerador_de_Senhas']
collection = db['Senhas_geradas']

# Insere os perfis na coleção
result = collection.insert_many(perfis_data)

# Imprime os IDs dos documentos inseridos
print(f"IDs dos documentos inseridos: {result.inserted_ids}")
    