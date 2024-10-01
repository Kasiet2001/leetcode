def canArrange(arr, k):
    rem = dict()
    for num in arr:
        rem[num % k] = rem.get(num % k, 0) + 1
    for n in arr:
        r = n % k
        if r == 0:
            if rem[r] % 2:
                return False
        elif rem[r] != rem.get(k - r, 0):
            return False
    return True
print(canArrange([1,2,3,4,5,6], 10))