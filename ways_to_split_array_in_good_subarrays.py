def numberOfGoodSubarraySplits(nums):
    ones = [i for i, n in enumerate(nums) if n == 1]
    if not ones:
        return 0
    ans = 1
    for i in range(1, len(ones)):
        ans *= (ones[i] - ones[i - 1]) % (10 ** 9 + 7)
    return ans
print(numberOfGoodSubarraySplits([0,1,0,0,1]))