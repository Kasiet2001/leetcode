def sumOfSquares(nums):
    n = len(nums)
    ans = 0
    for i, num in enumerate(nums, 1):
        if n % i == 0:
            ans += num ** 2
    return ans
print(sumOfSquares([2,7,1,19,18,3]))