from collections import defaultdict
def countCompleteDayPairs(hours):
    remainder_hours = defaultdict(int)
    ans = 0
    for h in hours:
        r = h % 24
        if r == 0:
            ans += remainder_hours[0]
        else:
            ans += remainder_hours[24 - r]
        remainder_hours[r] += 1
    return ans


print(countCompleteDayPairs([12,12,30,24,24]))
