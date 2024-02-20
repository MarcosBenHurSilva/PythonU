import base64

text = input("texto a ser criptografado: ")
text2 = "Texto a ser codificado (criptografado)."
xpto = base64.b64encode(text.encode("utf-8"))
xpto2 = base64.b64encode(text2.encode("utf-8"))

print(text)
print(xpto)
