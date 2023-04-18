def reverseWords(s):
    return ' '.join([i[::-1] for i in s.split()])
print(reverseWords("Let's take LeetCode contest"))