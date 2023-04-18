def intToRoman(num):
    roman_num = ''
    roman_dict = {1000: 'M', 900: 'CM',
                  500: 'D', 400: 'CD',
                  100: 'C', 90: 'XC',
                  50: 'L', 40: 'XL',
                  10: 'X', 9: 'IX',
                  5: 'V', 4: 'IV',
                  3: 'III',  1: 'I'}
    for k, v in roman_dict.items():
        if num // k != 0:
            n = num // k
            roman_num += roman_dict[k] * n
            num -= k * n
    return roman_num
print(intToRoman(2))


