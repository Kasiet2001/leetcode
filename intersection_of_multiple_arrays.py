def intersection(nums):
    dict = {}
    for i in range(len(nums)):
        for j in nums[i]:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] += 1
    inter = []
    for k, v in dict.items():
        if v == len(nums):
            inter.append(k)
    return sorted(inter)
print(intersection([[1,2,3],[4,5,6]]))
