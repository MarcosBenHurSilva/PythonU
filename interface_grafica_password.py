import json
import random
import string
from pymongo import MongoClient
from bson import ObjectId
import tkinter as tk
from tkinter import ttk

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_symbols):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = "!@#$%^&*()_+-="

    allowed_chars = ""
    password = ""

    allowed_chars += lowercase_chars if include_lowercase else ""
    allowed_chars += uppercase_chars if include_uppercase else ""
    allowed_chars += number_chars if include_numbers else ""
    allowed_chars += symbol_chars if include_symbols else ""

    if length <= 0:
        return "(password length must be at least 1)"
    if not allowed_chars:
        return "(At least 1 set of character needs to be selected)"

    for _ in range(length):
        random_index = random.randint(0, len(allowed_chars) - 1)
        password += allowed_chars[random_index]

    return password

def save_to_mongodb(site, user, password):
    client = MongoClient('mongodb://localhost:27017')
    db = client['nome_do_seu_banco']
    collection = db['nome_da_sua_colecao']

    result = collection.insert_one({"Site": site, "User": user, "Senha": password})
    return result.inserted_id

def generate_and_save():
    site = site_entry.get()
    user = user_entry.get()
    
    password = generate_password(16, True, True, True, True)
    
    inserted_id = save_to_mongodb(site, user, password)
    
    result_label.config(text=f"Senha gerada e salva no MongoDB com ID: {inserted_id}")

# Criar a interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas e Salvar no MongoDB")

# Criar widgets
site_label = ttk.Label(root, text="Site:")
site_entry = ttk.Entry(root)

user_label = ttk.Label(root, text="User:")
user_entry = ttk.Entry(root)

generate_button = ttk.Button(root, text="Gerar e Salvar", command=generate_and_save)
result_label = ttk.Label(root, text="")

# Organizar widgets na grade
site_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
site_entry.grid(row=0, column=1, padx=5, pady=5)
user_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
user_entry.grid(row=1, column=1, padx=5, pady=5)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, columnspan=2)

# Iniciar a interface gráfica
root.mainloop()
