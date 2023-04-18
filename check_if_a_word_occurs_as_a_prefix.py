def isPrefixOfWord(sentence, searchWord):
    sentence = sentence.split()
    for i in range(len(sentence)):
        if sentence[i][:len(searchWord)] == searchWord:
            return i + 1
    return -1
print(isPrefixOfWord("i am tired", "you"))