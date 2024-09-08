def convertDateToBinary(date):
    b = []
    for d in date.split('-'):
        b.append(str(bin(int(d)))[2:])
    return ('-').join(b)
print(convertDateToBinary("2080-02-29"))