def longestSquareStreak(nums):
    ans = -1
    squares = dict()
    nums = sorted(set(nums), reverse=True)
    for num in nums:
        n = num * num
        if n in squares and n != num:
            squares[num] = squares[n] + 1
            ans = max(ans, squares[num])
        else:
            squares[num] = 1
    return ans
print(longestSquareStreak([2,3,5,6,7]))

