def maxDivScore(nums, divisors):
    ans = -1
    d = -1
    for i in divisors:
        n = sum(1 for j in nums if j % i == 0)
        if n > d or n == d and ans > i:
            ans = i
            d = n
    return ans
print(maxDivScore([69,3,92,14,67,90,31,40,54,63,99,88,28,100,5,72,89,60,90,71], [97,16,7,60,6,57,73,84,17,8,77,60,7,74,74,24,52,43,94,48,9,99]))