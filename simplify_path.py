def simplifyPath(path):
    ans = []
    path = path.split('/')
    for i in path:
        if i == '..':
            if ans:
                ans.pop()
        elif i not in ('.', ''):
            ans.append(i)
    return '/' + '/'.join(ans)
print(simplifyPath("/../.."))