def increasingTriplet(nums):
    f = s = float('inf')
    for n in nums:
        if n <= f:
            f = n
        elif n <= s:
            s = n
        else:
            return True
    return False
print(increasingTriplet([2,1,5,0,4,6]))