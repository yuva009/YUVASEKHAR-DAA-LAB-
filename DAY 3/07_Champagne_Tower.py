def champagne_tower(poured, query_row, query_glass):
    tower = [[0.0] * 101 for _ in range(101)]
    tower[0][0] = poured

    for row in range(query_row):
        for glass in range(row + 1):
            excess = max(0.0, tower[row][glass] - 1.0)

            if excess > 0:
                tower[row + 1][glass] += excess / 2
                tower[row + 1][glass + 1] += excess / 2

    return min(1.0, tower[query_row][query_glass])


test_cases = [
    (1, 1, 1),
    (2, 1, 1)
]

for poured, row, glass in test_cases:
    print(f"{champagne_tower(poured, row, glass):.5f}")
