def findComplement(num):
    b = bin(num)[2:]
    binary = ''
    for d in b:
        if d == '1':
            binary += '0'
        else:
            binary += '1'
    return int(binary, 2)
print(findComplement(5))