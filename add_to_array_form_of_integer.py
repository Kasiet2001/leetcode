def addToArrayForm(num, k):
    num = int(''.join([str(i) for i in num])) + k
    return [int(i) for i in str(num)]
print(addToArrayForm([1,2,0,0], 34))