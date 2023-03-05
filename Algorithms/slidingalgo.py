def maxSumOfK(ar, k):
    if k > len(ar):
        return "Invalid"
    window_sum = sum(ar[:k])
    initial_sum = window_sum
    for i in range(len(ar) - k):
        window_sum = window_sum - ar[i] + ar[i + k]
        initial_sum = max(window_sum, initial_sum)
    return initial_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
ob = maxSumOfK(arr, 4)
print(ob)
