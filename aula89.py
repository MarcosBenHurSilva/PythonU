# dir, hasattr e getattr em Python

string = "Marcos"
metodo = "strip"

if hasattr(string, metodo):
    print("Existe upper")
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)
