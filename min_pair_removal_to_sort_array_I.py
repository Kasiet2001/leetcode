def minimumPairRemoval(nums):
    ans = 0
    while nums != sorted(nums):
        min_sum = float('inf')
        min_idx = -1

        for i in range(len(nums) - 1):
            pair_sum = nums[i] + nums[i + 1]
            if pair_sum < min_sum:
                min_sum = pair_sum
                min_idx = i
        combined = nums[min_idx] + nums[min_idx + 1]
        nums = nums[:min_idx] + [combined] + nums[min_idx + 2:]
        ans += 1
    return ans
print(minimumPairRemoval([5,2,3,1]))