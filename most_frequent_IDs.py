import heapq
from collections import defaultdict
def mostFrequentIDs(nums, freq):
    ans = []
    counter = dict()
    curr_max = 0
    for idx, num in enumerate(nums):
        flag = False
        if freq[idx] < 0 and counter[num] == curr_max:
            flag = True
        counter[num] = counter.get(num, 0) + freq[idx]
        if counter[num] > curr_max:
            curr_max = counter[num]
        if flag:
            curr_max = max(counter.values())
        ans.append(curr_max)
    return ans
print(mostFrequentIDs([2,3,2,1], [3,2,-3,1]))