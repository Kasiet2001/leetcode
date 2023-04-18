def reverse(x):
    if x >= 0 and 0 <= int(str(x)[::-1]) < 2147483648 - 1:
        return int(str(x)[::-1])
    elif -2147483648 <= int('-' + str(x)[::-1].replace('-', '')) < 0:
        return int('-' + str(x)[::-1].replace('-', ''))
    return 0
print(reverse(-123))