def checkDistances(s, distance):
    dis = [i for i in distance]
    for i in range(len(s)):
        t = 0
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                dis[ord(s[i]) - 97] = j - i - 1
    return dis == distance
print(checkDistances("rryzglzgyl",
[1,9,22,36,3,20,2,42,47,5,35,3,11,37,14,37,44,0,15,9,19,44,16,32,5,2]))