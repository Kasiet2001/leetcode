def numberOfBeams(bank):
    prev = bank[0].count('1')
    ans = 0
    for i in range(1, len(bank)):
        curr = bank[i].count('1')
        ans += prev * curr
        if curr > 0:
            prev = curr
    return ans
print(numberOfBeams(["000","111","000"]))