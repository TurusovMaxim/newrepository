s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

for i in range(len(s)):
    min = i
    for j in range(min + 1, len(s)):
        if s[j] < s[min]:
            min = j
        j += 1
    if s[min] != s[i]:
        s[i], s[min] = s[min], s[i]

print(s)
input('Press "enter" for close program ')