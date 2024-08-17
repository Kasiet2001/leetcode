from collections import deque

def resultsArray(nums, k):
    results = [-1] * (len(nums) - k + 1)
    curr_sub = deque()

    for i in range(len(nums)):
        if curr_sub and curr_sub[-1] == nums[i] - 1:
            curr_sub.append(nums[i])
        else:
            curr_sub = deque([nums[i]])

        if len(curr_sub) == k:
            results[i - k + 1] = curr_sub[-1]
            curr_sub.popleft()

    return results
print(resultsArray([1], 1))
