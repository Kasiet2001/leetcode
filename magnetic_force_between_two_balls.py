def maxDistance(position, m):
    position.sort()
    l, r = 1, position[-1] - position[0]
    ans = -1
    while l <= r:
        mid = l + (r - l) // 2
        last_position, balls = position[0], 1
        for i in range(1, len(position)):
            if position[i] - last_position >= mid:
                last_position = position[i]
                balls += 1
        if balls >= m:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
print(maxDistance([5,4,3,2,1], 4))