def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ''