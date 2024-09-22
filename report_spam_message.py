from collections import Counter
def reportSpam(message, bannedWords):
    freq = Counter(message)
    spam = 0
    for w in bannedWords:
        if w in freq:
            spam += min(freq[w], 2)
            freq -= 1
        if freq[w] == 0:
            del freq[w]
        if spam > 1:
            return True
    return False
print(reportSpam(["l","i","l","i","l"], ["d","a","i","v","a"]))