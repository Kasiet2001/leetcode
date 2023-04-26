def addDigits(num):
    #while num > 9:
        #num = sum([int(i) for i in str(num)])
    #return num
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9
print(addDigits(38))