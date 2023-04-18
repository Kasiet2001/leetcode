def findGCD(nums):
    min_num = min(nums)
    max_num = max(nums)
    if max_num % min_num == 0:
        return min_num
    else:
        return max([i for i in range(1, min_num) if max_num % i == 0 and min_num % i == 0])
print(findGCD([3,3]))