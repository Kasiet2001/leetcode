def findThePrefixCommonArray(A, B):
    a, b = set(), set()
    ans = []
    count = 0
    for i in range(len(A)):
        a.add(A[i])
        b.add(B[i])
        if A[i] == B[i]:
            count += 1
            ans.append(count)
            continue
        if A[i] in b:
            count += 1
        if B[i] in a:
            count += 1
        ans.append(count)
    return ans
print(findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))