def canAliceWin(nums):
    single = 0
    double = 0
    for i in nums:
        if i >= 10:
            double += i
        else:
            single += i
    return single != double
print(canAliceWin([1,2,3,4,5,14]))