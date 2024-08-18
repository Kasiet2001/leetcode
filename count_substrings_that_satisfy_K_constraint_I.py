def countKConstraintSubstrings(s, k):
    left = 0
    count_0 = 0
    count_1 = 0
    substrings = 0

    for right in range(len(s)):
        if s[right] == '0':
            count_0 += 1
        else:
            count_1 += 1

        while count_0 > k and count_1 > k:
            if s[left] == '0':
                count_0 -= 1
            else:
                count_1 -= 1
            left += 1

        substrings += (right - left + 1)

    return substrings
print(countKConstraintSubstrings("10101", 1))