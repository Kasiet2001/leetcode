from collections import defaultdict
def calculateScore(s):
    n = len(s)
    score = 0
    pos = defaultdict(list)
    freq = defaultdict(int)

    for i in range(n):
        m = chr(219 - ord(s[i]))

        if m in pos and pos[m]:
            j = pos[m].pop()
            score += i - j

            freq[m] -= 1
            if freq[m] == 0:
                del pos[m]
                del freq[m]
        else:
            freq[s[i]] += 1
            pos[s[i]].append(i)

    return score
print(calculateScore("aczzx"))
