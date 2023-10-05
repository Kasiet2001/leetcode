def minimumPartition(s, k):
    ans = 1
    curr = ''
    for i in s:
        curr += i
        if int(curr) > k:
            curr = i
            if int(curr) > k:
                return -1
            ans += 1
    return ans
print(minimumPartition("165462", 60))

