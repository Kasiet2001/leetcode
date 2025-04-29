def numberOfSubarrays(nums):
    stack = []
    ans = 0
    freq = dict()
    for num in nums:
        ans += 1
        freq[num] = freq.get(num, 0) + 1
        while stack and stack[-1] < num:
            n = stack.pop()
            freq[n] -= 1
        if freq[num] == 0:
            del freq[num]
        else:
            ans += freq[num] - 1
        stack.append(num)

    return ans
print(numberOfSubarrays([3,2,18]))
