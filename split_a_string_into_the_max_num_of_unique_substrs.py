def maxUniqueSplit(s):
    seen = set()
    return backtrack(s, 0, seen)

def backtrack(s, start, seen):
    if len(s) == start:
        return 0

    max_count = 0
    for end in range(start + 1, len(s) + 1):
        sub_string = s[start: end]
        if sub_string not in seen:
            seen.add(sub_string)
            max_count = max(max_count, 1 + backtrack(s, end, seen))
            seen.remove(sub_string)
    return max_count

print(maxUniqueSplit("ababccc"))