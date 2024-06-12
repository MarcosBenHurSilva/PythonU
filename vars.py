a = 0b1010  # 10 em binário
b = 0b0011  # 3 em binário

print("Valores originais:")
print("a =", a)
print("b =", b)

a = a ^ b  # Primeiro XOR
b = a ^ b  # Segundo XOR
a = a ^ b  # Terceiro XOR

print("\nValores trocados:")
print("a =", a)
print("b =", b)
