def find_paths(m, n, N, i, j):
    memo = {}

    def dp(r, c, steps):
        if r < 0 or r >= m or c < 0 or c >= n:
            return 1
        if steps == 0:
            return 0

        key = (r, c, steps)
        if key in memo:
            return memo[key]

        result = (
            dp(r - 1, c, steps - 1)
            + dp(r + 1, c, steps - 1)
            + dp(r, c - 1, steps - 1)
            + dp(r, c + 1, steps - 1)
        )

        memo[key] = result
        return result

    return dp(i, j, N)


test_cases = [
    (2, 2, 2, 0, 0),
    (1, 3, 3, 0, 1)
]

for m, n, N, i, j in test_cases:
    print("Number of ways:", find_paths(m, n, N, i, j))
