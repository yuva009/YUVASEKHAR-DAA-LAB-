def find_maximum(arr):
    if not arr:
        return None

    arr = sorted(arr)
    return arr[-1]


test_cases = [
    [],
    [5],
    [3, 3, 3, 3, 3]
]

for arr in test_cases:
    result = find_maximum(arr)
    print("Input:", arr)
    print("Maximum:", result)
