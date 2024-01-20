from math import ceil
def maxDistToClosest(seats):
    ans = 0
    left = 0
    curr_dist = 1 if seats[left] == 0 else 0
    for right in range(1, len(seats)):
        if seats[right] == 0:
            curr_dist += 1
        if seats[right] == 1:
            if seats[left] == 1:
                ans = max(ans, ceil(curr_dist / 2))
            else:
                ans = max(ans, curr_dist)
            curr_dist = 0
            left = right
    return max(ans, curr_dist)
print(maxDistToClosest([0,1,0]))