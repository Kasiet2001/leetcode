def countSubarrays(nums):
    res = 0
    for i in range(len(nums) - 2):
        array = nums[i: i + 3]
        if nums[i + 1] % 2 == 0:
            if array[0] + array[2] == array[1] // 2:
                res += 1
    return res
print(countSubarrays([1,1,1]))