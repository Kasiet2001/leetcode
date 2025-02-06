def tupleSameProduct(nums):
    res = 0
    freq = dict()
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            prod = nums[i] * nums[j]
            if prod in freq:
                freq[prod] += 1
                res += (freq[prod] - 1) * 8
            else:
                freq[prod] = 1
    return res
print(tupleSameProduct([1,2,4,5,10,20]))
