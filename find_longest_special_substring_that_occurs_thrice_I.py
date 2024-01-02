from collections import defaultdict
def maximumLength(s):
    count = 0
    substr_map = defaultdict(int)
    for i in range(len(s)):
        count = 1
        substr_map[(s[i], count)] += 1
        for j in range(i, len(s)):
            if j + 1 < len(s) and s[j] == s[j + 1]:
                count += 1
                substr_map[(s[i], count)] += 1
            else:
                break

    ans1 = 0
    for key, value in substr_map.items():
        if value >= 3:
            ans1 = max(ans1, key[1])
    return ans1 if ans1 != 0 else -1

print(maximumLength("abcccccdddd"))