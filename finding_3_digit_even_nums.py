def findEvenNumbers(digits):
    nums = set()
    n = len(digits)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue
                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                if num >= 100 and num % 2 == 0:
                    nums.add(num)

    res = sorted(list(nums))
    return res
print(findEvenNumbers([0,2,0,0]))