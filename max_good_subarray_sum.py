def maximumSubarraySum(nums, k):
    prefix_sum = dict()
    mx = float('-inf')
    s = 0
    for i, num in enumerate(nums):
        if num not in prefix_sum or prefix_sum[num] > s:
            prefix_sum[num] = s
        s += num
        if num - k in prefix_sum:
            mx = max(mx, s - prefix_sum[num - k])
        if num + k in prefix_sum:
            mx = max(mx, s - prefix_sum[num + k])
    return 0 if mx == float('-inf') else mx
print(maximumSubarraySum([-1,3,2,4,5], 3))
