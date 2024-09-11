def minBitFlips(start, goal):
    start = str(bin(start))[2:]
    goal = str(bin(goal))[2:]
    ans = 0
    if len(start) < len(goal):
        start = '0' * (len(goal) - len(start)) + start
    else:
        goal = '0' * (len(start) - len(goal)) + goal
    for i in range(len(start)):
        if start[i] != goal[i]:
            ans += 1
    return ans
print(minBitFlips(10, 7))