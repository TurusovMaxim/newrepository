s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

for i in range(len(s)):
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]

print(s)
input('Press "enter" for close program ')