nums = [1, 2, 1]
total = 0

for i in range(len(nums)):
    distinct = set()

    for j in range(i, len(nums)):
        distinct.add(nums[j])
        total += len(distinct) ** 2

print("Sum of squares of distinct counts:", total)
