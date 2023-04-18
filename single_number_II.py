def singleNumber(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for k,v in d.items():
        if v == 1:
            return k
print(singleNumber([2,2,3,2]))