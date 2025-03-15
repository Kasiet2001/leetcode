def totalNumbers(digits):
    nums = set()
    n = len(digits)
    for i in range(n):
        num = ''
        if digits[i] != 0:
            for j in range(n):
                if i != j:
                    for k in range(n):
                        if k != j and k != i:
                            num = str(digits[i]) + str(digits[j]) + str(digits[k])
                            if int(num) % 2 == 0:
                                nums.add(num)
    return len(nums)
print(totalNumbers([1,3,5]))
