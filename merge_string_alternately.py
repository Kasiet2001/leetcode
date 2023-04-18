def mergeAlternately(word1, word2):
    ans = []
    for i in range(max(len(word1), len(word2))):
        ans.append(word1[i] if i < len(word1) else '')
        ans.append(word2[i] if i < len(word2) else '')
    return ''.join(ans)
print(mergeAlternately("ab", "pqrs"))