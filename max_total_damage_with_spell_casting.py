def maximumTotalDamage(power):
    from collections import Counter
    if not power:
        return 0
    damage_count = Counter(power)
    unique_damage = sorted(damage_count.keys())
    n = len(unique_damage)
    if n == 0:
        return 0
    if n == 1:
        return unique_damage[0] * damage_count[unique_damage[0]]
    dp = [0] * n
    dp[0] = unique_damage[0] * damage_count[unique_damage[0]]
    for i in range(1, n):
        include_current = unique_damage[i] * damage_count[unique_damage[i]]
        exclude_current = dp[i - 1]
        j = i - 1
        while j >= 0 and (unique_damage[i] - unique_damage[j] <= 2):
            j -= 1
        if j >= 0:
            include_current += dp[j]
        dp[i] = max(include_current, exclude_current)
    return max(dp)
print(maximumTotalDamage([7,1,6,6]))

