def gcdOfStrings(str1, str2):
    from math import gcd
    if str1 + str2 != str2 + str1:
        return ''
    return str1[:gcd(len(str1), len(str2))]
print(gcdOfStrings("ABABAB", "ABAB"))