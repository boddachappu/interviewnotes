"""
Linear Search: We need to check each and every value whether it is matching or not
"""


def linearSearch(data, x):
    i = 0
    while i < len(data):

        if data[i] == x:
            return i
        i += 1
    return "not present"


print(linearSearch([1, 2, 3, 4, 5, 6], 5))

"""
Binary Search: break the values to half and search in those half
"""


def binarySearch(data, x):
    maxval = len(data) - 1
    minval = 0

    while minval <= maxval:

        midval = minval + (maxval - minval) // 2

        if data[midval] < x:
            minval = midval + 1

        elif data[midval] > x:
            maxval = midval - 1

        elif x == data[midval]:
            return midval
    return "not present"


print(binarySearch([1, 2, 3, 4, 5], 5))

"""
Interpolation Search: Similar to Binary Search but the time complexity is less O(log(log(n)). Here we need to find pos.
The data should be sorted and it should be even length
"""


def interPolationSearch(data, x):
    maxval = len(data) - 1
    minval = 0

    while minval <= maxval and x <= data[maxval] and x >= data[minval]:

        pos = minval + ((maxval - minval) // (data[maxval - data[minval]])) * (x - data[minval])
        if data[pos] < x:
            minval = pos + 1

        elif data[pos] > x:
            maxval = pos - 1

        elif x == data[pos]:
            return pos
    return "not present"


print(interPolationSearch([1, 2, 3, 4, 5, 6], 2))




