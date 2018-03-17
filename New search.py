s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

def merge_sort(s):
    if len(s) <= 1:
        return s
    elif len(s) > 1:
        mid = len(s) // 2
        left = merge_sort(s[:mid])
        right = merge_sort(s[mid:])
        return sort(left, right)

def sort(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    elif len(right) > 0:
        result += right
    return result

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

result = []
x = int(input("Enter the number you want to find: "))

result = binary_search(s, x)

if result == -1:
    print("-1")
else:
    print("The element is in array at the index", result)