def numRabbits(answers):
    from math import ceil
    from collections import Counter
    ans = 0
    answers = Counter(answers)
    for k, v in answers.items():
        ans += (k + 1) * ceil(v/(k + 1))
    return ans
print(numRabbits([1,1,2]))