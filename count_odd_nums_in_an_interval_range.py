def countOdds(low, high):
    ans = (high - low) // 2
    if low % 2 == 1 or high % 2 == 1:
        ans += 1
    return ans
print(countOdds(3, 7))