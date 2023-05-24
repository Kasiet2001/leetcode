import heapq
def maxScore(nums1, nums2, k):
    total = ans = 0
    h = []
    pairs = list(zip(nums1, nums2))
    pairs = sorted(pairs, key=lambda x: -x[1])
    for i in pairs:
        num1, num2 = i
        total += num1
        heapq.heappush(h, num1)
        if len(h) > k:
            total -= heapq.heappop(h)
        if len(h) == k:
            ans = max(ans, total * num2)
    return ans
print(maxScore([4,2,3,1,1],[7,5,10,9,6],1))