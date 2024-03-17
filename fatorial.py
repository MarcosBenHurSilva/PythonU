def fat(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Não existe fatorial de número negativo!")
    else:
        return n * fat(n - 1)


if __name__ == "__main__":
    n = 2
    res = fat(n)
    if n >= 0:
        print(f"O fatorial de {n} é {res}")
