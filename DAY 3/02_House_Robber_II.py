def rob_linear(nums):
    previous = 0
    current = 0

    for money in nums:
        previous, current = current, max(current, previous + money)

    return current


def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )


test_cases = [
    [2, 3, 2],
    [1, 2, 3, 1]
]

for nums in test_cases:
    print("Maximum money:", rob_circular(nums))
