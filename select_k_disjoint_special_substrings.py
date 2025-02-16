from collections import Counter
def maxSubstringLength(s, k):
    freq = Counter(s)
    special_substrings = []
    current_substring = ""
    unique_chars = set()

    for char in s:
        if freq[char] == 1:
            current_substring += char
            unique_chars.add(char)
        else:
            if current_substring:
                special_substrings.append(current_substring)
            current_substring = ""
            unique_chars.clear()

    if current_substring:
        special_substrings.append(current_substring)

    return len(special_substrings) >= k
print(maxSubstringLength("fln", 2))
