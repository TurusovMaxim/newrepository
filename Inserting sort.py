s = [1, 4, 10, 2, 6, 49, 24, 64]

print(s)

for i in range(1, len(s)):
    unsorted = s[i]
    sorted = i - 1
    while sorted >= 0:
        if unsorted < s[sorted]:
            s[sorted], s[sorted + 1] = s[sorted + 1], s[sorted]
            sorted -= 1
        else:
            break

print(s)