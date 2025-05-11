def minOperations(nums):
    ops = 0
    stack = []
    for num in nums:
        while stack and stack[-1] >= num:
            if stack[-1] > num:
                ops += 1
            stack.pop()
        if num != 0:
            stack.append(num)
    return ops + len(stack) if stack else ops
print(minOperations([1,2,2,2,1]))