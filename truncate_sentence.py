def truncateSentence(s, k):
    return ' '.join(s.split()[:k])
print(truncateSentence("chopper is not a tanuki", 5))