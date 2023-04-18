def maxRepeating(sequence, word):
    i = 0
    while word * (i + 1) in sequence:
        i += 1
    return i
print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))