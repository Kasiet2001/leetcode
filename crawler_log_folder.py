def minOperations(logs):
    ans = 0
    for f in logs:
        if f == '../' and ans > 0:
            ans -= 1
        elif f not in ['../', './']:
            ans += 1
    return ans
print(minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))