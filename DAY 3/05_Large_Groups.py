def large_groups(s):
    result = []
    start = 0

    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[start]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    return result


test_cases = ["abbxxxxzzy", "abc"]

for s in test_cases:
    print("Input:", s)
    print("Large groups:", large_groups(s))
