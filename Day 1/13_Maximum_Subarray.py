def max_subarray_sum(arr):
    current_sum = arr[0]
    maximum_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print("Maximum Subarray Sum:", max_subarray_sum(arr))
