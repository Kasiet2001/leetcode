def longestSubsequence(arr, difference):
    ans = {}
    for i in arr:
        if i - difference in ans:
            ans[i] = ans[i - difference] + 1
        else:
            ans[i] = 1
    return max(ans.values())
print(longestSubsequence([1,5,7,8,5,3,4,2,1], -2))