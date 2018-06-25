s = input('Enter a list of numbers without a comma: ').split()
for i in range(len(s)):
    s[i] = int(s[i])


def quick_sort(s):
    quickSortHelper(s, 0, len(s) - 1)


def quickSortHelper(s, first, last):
    if first<last:
        splitpoint = partition(s, first, last)
        quickSortHelper(s, first, splitpoint - 1)
        quickSortHelper(s, splitpoint + 1, last)


def partition(s, first, last):
    pivotvalue = s[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and \
                s[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while s[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = s[leftmark]
            s[leftmark] = s[rightmark]
            s[rightmark] = temp
    temp = s[first]
    s[first] = s[rightmark]
    s[rightmark] = temp
    return rightmark


quick_sort(s)
print(s)