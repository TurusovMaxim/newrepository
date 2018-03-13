def binary_search(s, x, left=0, right=0):
    if right == 0:
        right = len(s) - 1
    if right >= left:
        mid = (left + right) // 2
        if x > s[mid]:
            return binary_search(s, x, mid + 1, right)
        elif x < s[mid]:
            return binary_search(s, x, left, mid - 1)
        elif x == s[mid]:
            return mid
    else:
        return -1

s = [1, 12, 15, 21, 27, 36, 40, 53, 68, 72]
x = int(input())

result = binary_search(s, x)

if result == -1:
    print("-1")
else:
    print("The element is in array at the index", result)

print('Here is the array: 1, 12, 15, 21, 27, 36, 40, 53, 68, 72')
input('Press "enter" for close program ')