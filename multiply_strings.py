def multiply(num1, num2):
    dic = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    k = 1
    i = -1
    n1 = 0
    n2 = 0
    while str(n1) != num1:
        n1 += dic[num1[i]] * k
        i -= 1
        k *= 10
    i = -1
    k = 1
    while str(n2) != num2:
        n2 += dic[num2[i]] * k
        i -= 1
        k *= 10
    return str(n1 * n2)
print(multiply("2", "4"))
