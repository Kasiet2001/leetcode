def printVertically(s):
    s = s.split()
    l = max([len(i) for i in s])
    w = [i + ' ' * (l - len(i)) if len(i) < l else i for i in s]
    ans = []
    for j in zip(*w):
        ans.append(''.join(j).rstrip())
    return ans
print(printVertically("CONTEST IS COMING"))