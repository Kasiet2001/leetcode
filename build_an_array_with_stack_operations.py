def buildArray(target, n):
    ans = []
    for i in range(1, n + 1):
        if i > target[-1]:
            break
        elif i not in target:
            ans.extend(['Push', 'Pop'])
        else:
            ans.append('Push')
    return ans