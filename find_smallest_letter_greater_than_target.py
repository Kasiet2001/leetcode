def nextGreatestLetter(letters, target):
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    letters.append(target)
    letters = sorted(set(letters))
    return letters[letters.index(target) + 1]
print(nextGreatestLetter(["c","f","j"],"d"))