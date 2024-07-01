def threeConsecutiveOdds(arr):
    n = 0
    for num in arr:
        if num % 2:
            n += 1
            if n == 3:
                return True
        else:
            n = 0
    return False
print(threeConsecutiveOdds([1,3]))