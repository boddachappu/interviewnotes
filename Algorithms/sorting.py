# Sort a list
l = [12, 9, 5, 6, 2, 4]

for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[i] < l[j]:
            # tmp = l[i]
            # l[i] = l[j]
            # l[j] = tmp
            l[i], l[j] = l[j], l[i]

print(l)
# l = [1, 9, 5, 6, 2, 4]
# l.sort() # acending
# l.sort(reverse=True) #descending
# print(l)
# sortl = sorted(l)


# sorted(l, key=lambda x:x[1] )
# [(0, 1), (1, 2), (3, 5)]
# sorted(l, key=lambda x:x[1], reverse=True)
# [(3, 5), (1, 2), (0, 1)]
# d = {1:2, 3:4, 0:2}
# sorted(d.items(), key=lambda x:x[1], reverse=True)


"""
Insertion sort: The second element will be compared with first element if smaller then swap. Similarly 3rd element will
be checked with 2nd element if it is small then swap 3rd to 2nd and check 2nd with 1st and it continues.
"""
l = [1, 9, 5, 6, 2, 4]
for k in range(1, len(l)):
    for m in range(k - 1, 0, -1):
        if l[m] > l[m + 1]:
            l[m], l[m + 1] = l[m + 1], l[m]

print(f"insertion sort value {l}")

"""
Selection Sort: We consider first index as small value and iterate over list to find small value and it's index.
Once we find the min value we will swap the index values with min value at 0 index.
"""

l = [1, 7, 9, 5, 6, 2, 4]
for k in range(0, len(l) - 1):
    minindex = k
    for m in range(k + 1, len(l)):
        if l[m] < l[minindex]:
            minindex = m
    if minindex != k:
        l[minindex], l[k] = l[k], l[minindex]

print(f"Selection sort value {l}")

"""
Bubble Sort: We need to compare the consecutive two elements and swap if they are small. we need to reduce the second 
for loop range by ith index of first for loop because at first iteration we will get the max value.
"""
l = [1, 7, 9, 5, 0, 6, 2, 4]
for k in range(0, len(l)):
    for m in range(0,
                   len(l) - 1 - k):  # iteration will be reduced for every k iteration the leng of range will be reduced
        if l[m] > l[m + 1]:
            l[m], l[m + 1] = l[m + 1], l[m]

print(f"Bubble sort value {l}")

"""
Merge Sort: we need to split entire list into single list and start mergeing by them again while checking the value
"""

import sys


def merge(L, first, middle, last):
    left = L[first:middle + 1]
    right = L[middle + 1:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 0

    for k in range(first, last + 1):
        if left[i] <= right[j]:
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1


def merge_sort2(L, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(L, first, middle)
        merge_sort2(L, middle + 1, last)
        merge(L, first, middle, last)


def merge_sort(L):
    merge_sort2(L, 0, len(L) - 1)


l = [1, 7, 9, 5, 0, 6, 2, 4]
merge_sort(l)
print(f"Merge sort value {l}")


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


# Merge the sorted halves
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))
