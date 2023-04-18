def sumEvenAfterQueries(nums, queries):
    res = []
    even_num = sum(i for i in nums if i % 2 == 0)
    for val, ind in queries:
        if nums[ind] % 2 == 0:
            even_num -= nums[ind]
        nums[ind] += val
        if nums[ind] % 2 == 0:
            even_num += nums[ind]
        res.append(even_num)
    return res
print(sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))