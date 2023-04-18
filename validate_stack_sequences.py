def validateStackSequences(pushed, popped):
    s = []
    ind = 0
    for num in pushed:
        s.append(num)
        while s and s[len(s) - 1] == popped[ind]:
            s.pop()
            ind += 1
    return True if not s else False
print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))