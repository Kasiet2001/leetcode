def digitSum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def minElement(nums) -> int:
    result = []
    for num in nums:
        result.append(digitSum(num))
    return min(result)