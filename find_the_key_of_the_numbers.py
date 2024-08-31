def generateKey(num1, num2, num3):
    num1 = '0' * (4 - len(str(num1))) + str(num1)
    num2 = '0' * (4 - len(str(num2))) + str(num2)
    num3 = '0' * (4 - len(str(num3))) + str(num3)
    ans = ''
    for i in range(len(num1)):
        ans += min(num1[i], num2[i], num3[i])
    return int(ans)
print(generateKey(1, 10, 1000))