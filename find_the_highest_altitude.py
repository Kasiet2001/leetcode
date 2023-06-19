def largestAltitude(gain):
    ans = [0]
    for i in range(len(gain)):
        ans.append(gain[i] + ans[-1])
    return max(ans)
print(largestAltitude([-5,1,5,0,-7]))