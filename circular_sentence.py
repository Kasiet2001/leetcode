def isCircularSentence(sentence):
    sentence = sentence.split()
    if sentence[0][0] == sentence[-1][-1]:
        t = all(sentence[i][-1] == sentence[i + 1][0] for i in range(len(sentence) - 1))
        return t
print(isCircularSentence("Leetcode is cool"))