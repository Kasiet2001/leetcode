from collections import Counter
def maxNumberOfBalloons(text):
    text = Counter(text)
    b = Counter('balloon')
    ans = []
    for k, v in b.items():
        if k in b:
            ans.append(text[k] // v)
    return min(ans) if len(ans) == len(b) else 0
print(maxNumberOfBalloons("nlaebolko"))