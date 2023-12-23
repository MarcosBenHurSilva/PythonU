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

    # Improved logic for combining allowed characters.
    for char_set, include in zip(
        [lowercase_chars, uppercase_chars, number_chars, symbol_chars],
        [include_lowercase, include_uppercase, include_numbers, include_symbols],
    ):
        if include:
            allowed_chars += char_set

    # Improved validation for password length.
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    if not allowed_chars:
        raise ValueError("At least one set of characters needs to be selected.")

    for _ in range(length):
        random_index = random.randint(0, len(allowed_chars) - 1)
        password += allowed_chars[random_index]

    return password


def save_to_mongodb(site, user, password):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Gerador_de_Senhas']
    collection = db['Senhas_geradas_interface_grafica']

    # Improved error handling with try-except block.
    try:
        result = collection.insert_one({"Site": site, "User": user, "Senha": password})
    except Exception as e:
        raise ValueError(f"Error saving to MongoDB: {e}")
    else:
        return result.inserted_id


def generate_and_save(site_entry, user_entry, result_label):
    try:
        site = site_entry.get()
        user = user_entry.get()
        password = generate_password(16, True, True, True, True)
        inserted_id = save_to_mongodb(site, user, password)
        result_label.config(text=f"Senha gerada: {password}. Salva no MongoDB com ID: {inserted_id}")
    except ValueError as e:
        result_label.config(text=f"Erro: {e}")


# Improved code for creating the interface
def create_interface():
    root = tk.Tk()
    root.title("Gerador de Senhas e Salvar no MongoDB")

    # Create widgets
    site_label = ttk.Label(root, text="Site:")
    site_entry = ttk.Entry(root)

    user_label = ttk.Label(root, text="User:")
    user_entry = ttk.Entry(root)

    #generate_button = ttk.Button(root, text="Gerar e Salvar", command=generate_and_save)
    generate_button = ttk.Button(root, text="Gerar e Salvar", command=lambda: generate_and_save(site_entry, user_entry, result_label))

    result_label = ttk.Label(root, text="")

    # Organize widgets in grid
    site_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    site_entry.grid(row=0, column=1, padx=5, pady=5)
    user_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    user_entry.grid(row=1, column=1, padx=5, pady=5)
    generate_button.grid(row=2, column=0, columnspan=2, pady=10)
    result_label.grid(row=3, column=0, columnspan=2)

    # Start the GUI
    root.mainloop()


# Call the function to create the interface
create_interface()
