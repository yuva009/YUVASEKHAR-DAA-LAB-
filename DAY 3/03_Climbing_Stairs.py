def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


for n in [4, 3]:
    print("Number of ways for", n, "steps:", climb_stairs(n))
