def kthLargestNumber(nums, k):
    nums = sorted(map(int, nums))
    return str(nums[-k])

    '''nums = sorted([int(i) for i in nums])
         return str(nums[-k]) '''
print(kthLargestNumber(["2","21","12","1"],3))