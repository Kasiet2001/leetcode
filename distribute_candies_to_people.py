def distributeCandies(candies, num_people):
    ans = [0] * num_people
    c = 1
    i = 0
    while candies > 0:
        if i == num_people:
            i = 0
        if candies >= c:
            ans[i] += c
            candies -= c
            c += 1
        else:
            ans[i] += candies
            break
        i += 1
    return ans
print(distributeCandies(10, 3))