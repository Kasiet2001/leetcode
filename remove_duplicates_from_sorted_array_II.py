def removeDuplicates(nums):
    if len(nums) < 3:
        return len(nums)
    l = 0
    for i in sorted(set(nums)):
        if nums.count(i) >= 2:
            ind = 2
            while ind != 0:
                nums[l] = i
                ind -= 1
                l += 1
        elif nums.count(i) == 1:
            nums[l] = i
            l += 1
    return l
print(removeDuplicates([-1,0,0,0,0,3,3]))