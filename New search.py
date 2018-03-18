s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

def merge_sort(s):
    if len(s) <= 1:
        return s
    else:
        middle = len(s) // 2
        left = merge_sort(s[:middle])
        right = merge_sort(s[middle:])
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

m = merge_sort(s)
print('Array sorted',m)

def binary_search(lst, x, lft=0, rght=0):
    if rght == 0:
        rght = len(lst) - 1
    if rght >= lft:
        mid = (lft + rght) // 2
        if x > lst[mid]:
            return binary_search(lst, x, mid + 1, rght)
        elif x < lst[mid]:
            return binary_search(lst, x, lft, mid - 1)
        elif x == lst[mid]:
            return mid
    else:
        return -1

lst = m
x = int(input("Enter the number you want to find: "))

rslt = binary_search(lst, x)

if rslt == -1:
    print("error")
else:
    print("The element is in array at the index", rslt)

input('Press "enter" for close program ')