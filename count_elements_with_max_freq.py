def maxFrequencyElements(nums):
    freq = dict()
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    maxx = 0
    ans = 0
    for v in freq.values():
        if maxx == v:
            ans += v
        elif maxx < v:
            ans = v
            maxx = v
    return ans
print(maxFrequencyElements([1,2,2,3,1,4]))