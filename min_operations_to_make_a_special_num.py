def minimumOperations(num):
    endIdx = {}
    ans = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '7' or num[i] == '2':
            if '5' in endIdx:
                return ans - 1
        elif num[i] == '5' or num[i] == '0':
            if '0' in endIdx:
                return ans - 1
        if num[i] == '5' or num[i] == '0':
            endIdx[num[i]] = i
        ans += 1
    return len(num) - 1 if '0' in endIdx else len(num)
print(minimumOperations("10"))