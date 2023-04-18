def checkIfPangram(sentence):
    return len(set(sentence)) == 26
print(checkIfPangram("leetcode"))