n = 20#for example
def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n+ 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

print(eratosthenes(n))