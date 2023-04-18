def minimumOperations(nums):
    t = 0
    while nums != [0] * len(nums):
        if min(sorted(set(nums))) == 0:
            nums = [i - sorted(set(nums))[1] if i > sorted(set(nums))[1] else 0 for i in nums]
            t += 1
        else:
            nums = [i - min(nums) if i > min(nums) else 0 for i in nums]
            t += 1
    return t
print(minimumOperations([0, 2]))