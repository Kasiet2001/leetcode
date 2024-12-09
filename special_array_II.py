import bisect
def isArraySpecial(nums, queries):
    start = []
    end = []
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i - 1] % 2:
            start.append(i - 1)
            end.append(i)

    ans = [False for _ in queries]
    for i in range(len(queries)):
        n = bisect.bisect_left(start, queries[i][0])
        m = bisect.bisect_right(end, queries[i][1])
        if (n == 0 and m == 0) or (n == len(start) and m == len(end)) or n == m:
            ans[i] = True
    return ans

print(isArraySpecial([9,5,9], [[0,2]]))