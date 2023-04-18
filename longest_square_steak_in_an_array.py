def longestSquareStreak(nums):
    ans = 1
    nums = set(nums)
    visited = set()
    for i in sorted(nums):
        if i in visited:
            continue
        visited.add(i)
        c = 1
        while i ** 2 in nums:
            visited.add(i ** 2)
            i *= i
            c += 1
        ans = max(c, ans)
    return ans if ans > 1 else -1
print(longestSquareStreak([2,3,5,6,7]))

