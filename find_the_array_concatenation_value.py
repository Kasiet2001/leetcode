def findTheArrayConcVal(nums):
    ans = 0
    while len(nums) > 0:
        if len(nums) > 1:
            ans += int(str(nums[0]) + str(nums[-1]))
            del nums[-1]
        else:
            ans += nums[0]
        del nums[0]
    return ans
print(findTheArrayConcVal([5,14,13,8,12]))