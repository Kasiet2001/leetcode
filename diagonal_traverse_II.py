from collections import defaultdict
def findDiagonalOrder(nums):
    d = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            d[i + j].append(nums[i][j])
    ans = []
    for v in d.values():
        ans.extend(v[::-1])
    return ans
print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))