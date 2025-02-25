def numOfSubarrays(arr):
    count = pref_sum = 0
    odd = 0
    even = 1
    for n in arr:
        pref_sum += n
        if pref_sum % 2 == 0:
            count += odd
            even += 1
        else:
            count += even
            odd += 1
    return count % (10 ** 9 + 7)
print(numOfSubarrays([1,3,5]))