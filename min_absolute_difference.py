def minimumAbsDifference(arr):
    arr.sort()
    ans = []
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        curr_diff = abs(arr[i + 1] - arr[i])
        if curr_diff < min_diff:
            ans = [[arr[i], arr[i + 1]]]
            min_diff = curr_diff
        elif curr_diff == min_diff:
            ans.append([arr[i], arr[i + 1]])
    return ans
print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))