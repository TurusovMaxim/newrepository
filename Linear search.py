def linear_search(s, x):
    for i in range(len(s)):
        if s[i] == x:
            return i
    return -1

s = [1, 12, 15, 21, 27, 36, 40, 53, 68, 72]
x = 37

result = linear_search(s, x)

if result == -1:
    print("-1")
else:
    print("The element is in array at the index", result)