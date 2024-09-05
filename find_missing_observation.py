def missingRolls(rolls, mean, n):
    sum_rolls = sum(rolls)
    remaining = mean * (n + len(rolls)) - sum_rolls
    if remaining > n * 6 or remaining < n:
        return []
    distribute_mean = remaining // n
    mod = remaining % n
    n_elements = [distribute_mean] * n
    for i in range(mod):
        n_elements[i] += 1
    return n_elements
print(missingRolls([1,5,6], 3, 4))