def bagOfTokensScore(tokens, power):
    tokens.sort()
    ans = 0
    score = 0
    left, right = 0, len(tokens) - 1
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
        else:
            if score:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                return ans
        ans = max(ans, score)
    return ans
print(bagOfTokensScore([100], 50))