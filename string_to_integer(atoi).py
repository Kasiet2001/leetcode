def myAtoi(s):
    if s is None or len(s) < 1:
        return 0
    int_max = 2147483647
    int_min = -2147483648
    s = s.lstrip()
    i = 0
    isNegative = len(s) > 1 and s[0] == '-'
    isPositive = len(s) > 1 and s[0] == '+'
    if isNegative:
        i += 1
    elif isPositive:
        i += 1
    number = 0
    while i < len(s) and '0' <= s[i] <= '9':
        number = number * 10 + (ord(s[i]) - ord('0'))
        i += 1
    if isNegative:
        number = -number
    if number < int_min:
        return int_min
    if number > int_max:
        return int_max
    return number
print(myAtoi('-98765432126890'))

