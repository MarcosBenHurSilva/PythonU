# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(repr=True)
class Pessoa:
    nome: str
    # idade: int
    sobrenome: str

    #     @property
    #     def nome_completo(self):
    #         return f"{self.nome} {self.sobrenome}"

    #     @nome_completo.setter
    #     def nome_completo(self, valor):
    #         nome, *sobrenome = valor.split()
    #         self.nome = nome
    #         self.sobrenome = " ".join(sobrenome)

    #     def __init__(self, nome, idade, sobrenome):
    #         self.nome = nome
    #         self.idade = idade
    #         self.sobrenome = " ".join(sobrenome)
    #         self.sobrenome = sobrenome
    #         self.nome_completo = f"{self.nome} {self.sobrenome}"

    #     def __post_init__(self):
    #         print("POST INIT")


if __name__ == "__main__":
    #     p1 = Pessoa("Marcos", 31, "Silva")
    #     p2 = Pessoa("Marcos", 31, "Silva")
    #     print(p1 == p2)
    #     p1 = Pessoa("Marcos", 31, "Silva")
    #     p1.nome_completo = "Benhur Dorneles"
    #     print(p1)
    #     print(p1.nome_completo)
    lista = [Pessoa("A", "Z"), Pessoa("B", "Y"), Pessoa("C", "X")]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
