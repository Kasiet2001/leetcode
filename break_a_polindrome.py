def breakPalindrome(palindrome):
    if len(palindrome) == 1:
        return ''
    for i in range(len(palindrome)):
        if palindrome[i] != 'a':
            p = palindrome[:i] + 'a' + palindrome[i + 1:]
            if palindrome[:i] + 'a' + palindrome[i + 1:] != p[::-1]:
                return p
    return palindrome[:-1] + 'b'
print(breakPalindrome("a"))