def minCapability(nums, k):
    max_reward, min_reward = max(nums), 1
    total_houses = len(nums)
    while min_reward < max_reward:
        mid_reward = (min_reward + max_reward) // 2
        possible_thefts = 0
        index = 0
        while index < total_houses:
            if nums[index] <= mid_reward:
                possible_thefts += 1
                index += 2
            else:
                index += 1
        if possible_thefts >= k:
            max_reward = mid_reward
        else:
            min_reward = mid_reward + 1
    return min_reward
print(minCapability([2,7,9,3,1], 2))