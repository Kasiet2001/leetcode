def findOcurrences(text, first, second):
    ans = []
    text = text.split()
    for i in range(2, len(text)):
        if text[i - 2] == first and text[i - 1] == second:
            ans.append(text[i])
    return ans
print(findOcurrences( "we will we will rock you", "we","will"))