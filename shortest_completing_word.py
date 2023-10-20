from collections import Counter
def shortestCompletingWord(licensePlate, words):
    letters = Counter([i.lower() for i in licensePlate if i.isalpha()])
    return min((w for w in words if not letters - Counter(w)), key=len)
print(shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))