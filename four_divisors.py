def sumFourDivisors(nums):
    ans = 0
    for num in nums:
        divisors = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.add(num // i)
                divisors.add(i)
            if len(divisors) > 4:
                break
        if len(divisors) == 4:
            ans += sum(divisors)
    return ans
print(sumFourDivisors([1,2,3,4,5]))