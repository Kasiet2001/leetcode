def reverseWords(s):
    rev_s = str()
    for i in s.split():
        rev_s += i[::-1] + ' '
    return rev_s.rstrip()
print(reverseWords("Let's take LeetCode contest"))