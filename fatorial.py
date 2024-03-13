def fat(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)


if __name__ == "__main__":
    n = 5
    res = fat(n)
    print(f"O fatorial de {n} é {res}")
