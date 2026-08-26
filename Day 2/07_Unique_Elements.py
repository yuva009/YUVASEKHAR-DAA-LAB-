def unique_elements(arr):
    result = []
    seen = set()

    for value in arr:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


test_cases = [
    [3, 7, 3, 5, 2, 5, 9, 2],
    [-1, 2, -1, 3, 2, -2],
    [1000000, 999999, 1000000]
]

for arr in test_cases:
    print("Input:", arr)
    print("Unique:", unique_elements(arr))
