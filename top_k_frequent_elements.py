def topKFrequent(nums, k):
    elem = {}
    sorted_dict = {}
    for i in set(nums):
        elem[i] = nums.count(i)
    sorted_keys = sorted(elem, key=elem.get, reverse=True)
    return sorted_keys[:k]
print(topKFrequent([1,1,1,2,2,3], 2))