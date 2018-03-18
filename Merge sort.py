s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])

def merge_sort(s):
    if len(s) <= 1:
        return s
    else:
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

print(merge_sort(s))
input('Press "enter" for close program ')