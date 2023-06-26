from collections import Counter
import heapq
def minimumOperations(nums):
    if len(nums) <= 1:
        return 0
    even = Counter(nums[::2]).most_common(2)
    odd = Counter(nums[1::2]).most_common(2)
    if even[0][0] != odd[0][0]:
        return len(nums) - even[0][1] - odd[0][1]
    cand1 = len(nums) - even[0][1] - (odd[1][1] if len(odd) > 1 else 0)
    cand2 = len(nums) - odd[0][1] - (even[1][1] if len(even) > 1 else 0)
    return min(cand1, cand2)
print(minimumOperations([1,2,2,2,2]))
