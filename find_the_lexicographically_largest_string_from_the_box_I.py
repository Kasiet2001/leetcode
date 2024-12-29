def answerString(word, numFriends):
    if numFriends == 1:
        return word
    largest_letter = max(word)
    n = len(word)
    res = largest_letter
    for i in range(n):
        if word[i] == largest_letter:
            if i < numFriends - 1:
                friends = numFriends - i - 1
                s = word[i: len(word) - friends]
            else:
                s = word[i:]
            res = max(res, s)
    return res
print(answerString("gggg", 4))
