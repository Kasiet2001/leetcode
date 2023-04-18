def mostWordsFound(sentences):
    return max([i.count(' ') + 1 for i in sentences])

def mostWordsFound(sentences):
    return max([len(i.split()) for i in sentences])
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))