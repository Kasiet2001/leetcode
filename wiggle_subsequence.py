def wiggleMaxLength(nums):
    if len(nums) == 0:
        return 0
    if len(set(nums)) == 1 or len(nums) < 2:
        return 1
    l = [nums[1] - nums[0]]
    for i in range(1, len(nums)):
        last_num = nums[i] - nums[i - 1]
        if l[0] == 0:
            l[0] = last_num
        if last_num == 0:
            continue
        elif (l[-1] < 0 and last_num < 0) or (l[-1] > 0 and last_num > 0):
            continue
        else:
            l.append(last_num)
    return len(l) + 1
print(wiggleMaxLength([1,7,4,9,2,5]))