def fast_power(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        half = fast_power(x, n // 2)
        return half * half

    return x * fast_power(x, n - 1)


x = 2
n = 10

print("Result:", fast_power(x, n))
