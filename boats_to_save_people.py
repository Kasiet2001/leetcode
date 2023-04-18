def numRescueBoats(people, limit):
    ans = 0
    n = len(people)
    l, r = 0, n - 1
    people.sort()
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        ans += 1
    return ans
print(numRescueBoats([3,2,2,1], 3))