def partitionLabels(s):
    n = len(s)
    last = {s[i]: i for i in range(n)}
    i = 0
    ans = []
    while i < n:
        end = last[s[i]]
        j = i + 1
        while j < end:
            if last[s[j]] > end:
                end = last[s[j]]
            j += 1
        ans.append(end - i + 1)
        i = end + 1
    return ans
print(partitionLabels("ababcbacadefegdehijhklij"))
