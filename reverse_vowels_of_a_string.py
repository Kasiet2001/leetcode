def reverseVowels(self, s: str) -> str:
    vowels = [i for i in s if i in 'aAiIeEoOuU'][::-1]
    idx = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] in 'aAiIeEoOuU':
            s[i] = vowels[idx]
            idx += 1
    return ''.join(s)