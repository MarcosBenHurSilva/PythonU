import base64

text = "Texto a ser codificado em base64. Aumentando o texto para ver a diferença. Continuar aumentando o texto."
text2 = "Texto a ser codificado (criptografado)."
xpto = base64.b64encode(text.encode("utf-8"))
xpto2 = base64.b64encode(text2.encode("utf-8"))

print(text2)
print(xpto2)
