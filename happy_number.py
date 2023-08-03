def isHappy(n):
    end_num = 0
    d = dict()
    while len(str(n ** 2)) != 1:
        for i in str(n):
            end_num += int(i)**2
        if end_num in d:
            return False
        else:
            d[end_num] = True
        end_num, n = 0, end_num
    return n == 1
print(isHappy(4))



