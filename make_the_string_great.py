def makeGood(s):
    ans = []
    for i in s:
        if ans:
            if ans[-1].lower() == i.lower() and ans[-1] != i:
                ans.pop()
            else:
                ans.append(i)
        else:
            ans.append(i)
    return ''.join(ans)
print(makeGood("abBAcC"))