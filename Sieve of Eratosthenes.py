n = int(input('Enter the number '))

def eratosthenes(n):
    sieve = list(range(n+ 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

print(eratosthenes(n))