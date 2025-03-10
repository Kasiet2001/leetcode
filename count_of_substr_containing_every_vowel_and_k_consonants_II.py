from collections import defaultdict
def countOfSubstrings(word, k):
    n = len(word)
    cons_count = 0
    ans = 0
    vowels = ("a", "e", "i", "o", "u")
    map = defaultdict(int)

    l_right = 0
    l_left = 0
    for r in range(n):

        if word[r] in vowels:
            map[word[r]] += 1
        else:
            cons_count += 1

        while cons_count > k and l_right < r:
            if word[l_right] in vowels:
                map[word[l_right]] -= 1
                if map[word[l_right]] == 0:
                    del map[word[l_right]]

            else:
                cons_count -= 1
            l_right += 1
            l_left = l_right
        while cons_count == k and l_right < r:
            if word[l_right] in vowels:
                if map[word[l_right]] - 1 > 0:
                    map[word[l_right]] -= 1
                    l_right += 1
                else:
                    break
            else:
                break

        if len(map) == 5 and cons_count == k:
            ans += (l_right - l_left + 1)

    return ans
print(countOfSubstrings("iqeaouqi", 2))