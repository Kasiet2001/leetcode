def numberOfPairs(nums):
    left = 0
    total = 0
    num_pairs = {}
    for i in nums:
        num_pairs[i] = nums.count(i)
    for i in num_pairs.values():
        if i > 1:
            total += i // 2
            left += i % 2
        else:
            left += 1
    return [total, left]
print(numberOfPairs([0,0,1]))