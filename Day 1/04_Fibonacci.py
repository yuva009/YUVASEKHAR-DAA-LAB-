def fibonacci(n):
    a, b = 0, 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


n = 6

print(fibonacci(n))
