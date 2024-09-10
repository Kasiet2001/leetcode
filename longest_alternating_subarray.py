def alternatingSubarray(nums):
    prev, cnt, ans, fl = -1, 0, 0, 1
    for num in nums:
        if num - prev == fl:
            cnt += 1
            fl = -fl
            ans = max(cnt, ans)
        elif num - prev == 1:
            cnt = 1
        else:
            cnt = 0
            fl = 1
        prev = num
    return -1 if not ans else ans + 1
print(alternatingSubarray([2,3,4,3,4]))



