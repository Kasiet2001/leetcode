def numDifferentIntegers(word):
    for i in range(len(word)):
        if word[i].isnumeric() != True:
            word = word.replace(word[i], ' ')
    num = [int(i) for i in word.split()]
    return len(set(num))
print(numDifferentIntegers("a123bc34d8ef34"))