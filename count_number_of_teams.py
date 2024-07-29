def numTeams(rating):
    ans = 0
    for i in range(1, len(rating) - 1):
        left_smaller = right_larger = 0
        for j in range(i):
            if rating[i] > rating[j]:
                left_smaller += 1
        for k in range(i + 1, len(rating)):
            if rating[i] < rating[k]:
                right_larger += 1
        ans += left_smaller * right_larger
        left_larger = i - left_smaller
        right_smaller = len(rating) - i - 1 - right_larger
        ans += left_larger * right_smaller
    return ans
print(numTeams([1,2,3,4]))
