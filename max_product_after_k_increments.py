import heapq
def maximumProduct(nums, k):
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
    while k:
        num = heapq.heappop(heap)
        heapq.heappush(heap, num + 1)
        k -= 1
    ans = 1
    for i in heap:
        ans = (ans * i) % (10 ** 9 + 7)
    return ans
print(maximumProduct([6,3,3,2], 2))