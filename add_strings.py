def addStrings(num1, num2):
    numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9}
    output = 0
    output2 = 0
    for i in num1:
        output = output * 10 + numDict[i]
    for j in num2:
        output2 = output2 * 10 + numDict[j]
    return str(output + output2)
print(addStrings('11', '123'))