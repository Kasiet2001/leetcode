def divisorSubstrings(num, k):
    beauty = 0
    n = 0
    while k <= len(str(num)):
        if int(str(num)[n:k]) != 0 and num % int(str(num)[n:k]) == 0:
            beauty += 1
        k += 1
        n += 1
    return beauty
print(divisorSubstrings(240, 2))