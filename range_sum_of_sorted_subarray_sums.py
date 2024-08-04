def rangeSum(nums, n, left, right):
    modulo = 10 ** 9 + 7
    subarray_sums = []
    for i in range(n):
        sums = [nums[i]]
        for j in range(i + 1, n):
            sums.append(nums[j] + sums[- 1])
        subarray_sums.extend(sums)
    subarray_sums.sort()
    ans = 0
    for i in range(left - 1, right):
        ans += subarray_sums[i]
    return ans % modulo
print(rangeSum([1,2,3,4], 4, 1, 5))