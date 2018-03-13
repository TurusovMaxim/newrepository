s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

for a in range(1, len(s)):
    unsorted = s[a]
    sorted = a - 1
    while sorted >= 0:
        if unsorted < s[sorted]:
            s[sorted], s[sorted + 1] = s[sorted + 1], s[sorted]
            sorted -= 1
        else:
            break

print(s)
input('Press "enter" for close program ')