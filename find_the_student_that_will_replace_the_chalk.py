def chalkReplacer(chalk, k):
    k %= sum(chalk)
    for i, s in enumerate(chalk):
        if k < s:
            return i
        k -= s
print(chalkReplacer([22,25,39,3,45,45,12,17,32,9], 835))