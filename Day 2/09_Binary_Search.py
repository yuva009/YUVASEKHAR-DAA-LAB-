def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [-9, 3, 4, 6, 8, 9, 10, 30]

for key in [10, 100]:
    position = binary_search(arr, key)

    if position != -1:
        print(f"Element {key} is found at position {position}")
    else:
        print(f"Element {key} is not found")

print("Time Complexity: O(log n)")
