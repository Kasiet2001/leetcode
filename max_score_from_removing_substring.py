def maximumGain(s, x, y):

    def remove_pairs(pair, score):
        nonlocal s
        res = 0
        stack = []
        for c in s:
            if stack and c == pair[1] and stack[-1] == pair[0]:
                stack.pop()
                res += score
            else:
                stack.append(c)
        s = ''.join(stack)
        return res

    res = 0
    pairs = 'ab' if x > y else 'ba'
    res += remove_pairs(pairs, max(x, y))
    res += remove_pairs(pairs[::-1], min(x, y))
    return res
print(maximumGain("aabbaaxybbaabb", 5, 4))