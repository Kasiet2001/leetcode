def mostCompetitive(nums, k):
    n = len(nums) - k
    ans = []
    for num in nums:
        while n and ans and num < ans[-1]:
            ans.pop()
            n -= 1
        ans.append(num)
    return ans[:k]
print(mostCompetitive([3,5,2,6], 2))