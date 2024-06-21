def maximumPrimeDifference(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    max_idx = float('-inf')
    min_idx = float('inf')
    for idx, num in enumerate(nums):
        if is_prime(num):
            max_idx = max(max_idx, idx)
            min_idx = min(min_idx, idx)
    return max_idx - min_idx
print(maximumPrimeDifference([1,7]))
