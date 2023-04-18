def convertTime(current, correct):
    oper_num = 0
    dif = (int(correct[:2]) * 60 + int(correct[3:])) - (int(current[:2]) * 60 + int(current[3:]))
    for i in [60, 15, 5, 1]:
        oper_num += dif // i
        dif %= i
    return oper_num
print(convertTime("11:00","11:01"))