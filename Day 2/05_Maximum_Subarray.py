def max_subarray_sum(arr):
    current = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maximum = max(maximum, current)

    return maximum


test_cases = [
    [1, 2, 3, 4, 5],
    [7, 7, 7, 7, 7],
    [-10, 2, 3, -4, 5]
]

for arr in test_cases:
    print("Input:", arr)
    print("Maximum subarray sum:", max_subarray_sum(arr))
