def getHappyString(n, k):
    def generate_happy_strings(n, curr_str, happy_strings):
        if len(curr_str) == n:
            happy_strings.append(curr_str)
            return
        for char in ['a', 'b', 'c']:
            if len(curr_str) > 0 and curr_str[-1] == char:
                continue

            generate_happy_strings(
                n, curr_str + char, happy_strings
            )

    curr_str = ''
    happy_strings = []
    generate_happy_strings(n, curr_str, happy_strings)
    if len(happy_strings) < k:
        return ''
    happy_strings.sort()
    return happy_strings[k - 1]
print(getHappyString(3, 9))