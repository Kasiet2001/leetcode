def smallestNumber(num):
    zeros = str(num).count('0')
    n = [i for i in str(num) if i != '0' and i != '-']
    if str(num)[0] == '-':
        dig = sorted(n, reverse=True)
        return int('-' + ''.join(dig) + '0' * zeros)
    dig = sorted(n)
    dig.insert(1, '0' * zeros)
    return int(''.join(dig))
print(smallestNumber(-7605))