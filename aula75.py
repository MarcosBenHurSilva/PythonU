# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar


# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def numero(num):
    def multiplicar(multi):
        return num * multi

    return multiplicar

numero_digitado = float(input('Digite o número: '))
funcao_multiplicar = numero(numero_digitado)

multiplicador_digitado = float(input('Digite o multiplicador: '))
resultado = funcao_multiplicar(multiplicador_digitado)

print(f"Resultado da multiplicação: {resultado}")
