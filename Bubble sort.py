s = [1, 4, 10, 2, 6, 49, 24, 64]
print(s)

for i in range(len(s)):
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]

print(s)