def findTheWinner(n, k):
    ans = 0
    for i in range(2, n + 1):
        ans = (ans + k) % i
    return ans + 1
print(findTheWinner(5, 2))