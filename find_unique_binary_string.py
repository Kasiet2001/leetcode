def findDifferentBinaryString(nums):
    res = []
    for i in range(len(nums)):
        if nums[i][i] == '1':
            res.append('0')
        else:
            res.append('1')
    return "".join(res)
print(findDifferentBinaryString(["01","10"]))