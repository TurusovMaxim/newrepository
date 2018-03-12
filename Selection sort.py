s = [1, 4, 10, 2, 6, 49, 24, 64]

print(s)

for i in range(len(s)):
    min = i
    for j in range(min + 1, len(s)):
        if s[j] < s[min]:
            min = j
        j += 1
    if s[min] != s[i]:
        s[i], s[min] = s[min], s[i]

print(s)