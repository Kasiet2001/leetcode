from collections import defaultdict
def maxFreqSum(s: str) -> int:
    vowels = defaultdict(int)
    cons = defaultdict(int)
    for char in s:
        if char in 'aeiou':
            vowels[char] += 1
        else:
            cons[char] += 1
    max_c = 0
    max_v = 0
    if vowels:
        max_v = max(vowels.values())
    if cons:
        max_c = max(cons.values())
    return max_c + max_v
print(maxFreqSum("successes"))