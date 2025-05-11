def minDeletion(s, k):
    char_freq = [0] * 26
    for char in s:
        char_freq[ord(char) - ord('a')] += 1
    total = [freq for freq in char_freq if freq > 0]
    total.sort()
    return sum(total[:-k])
print(minDeletion('yyyzz', 1))