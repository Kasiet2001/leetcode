def detectCapitalUse(word):
    '''if word.capitalize() == word or word.upper() == word or word.lower() == word:
        return True
    return False'''
    return word.isupper() or word.islower() or word.istitle()
print(detectCapitalUse("FlaG"))