def frequencySort(nums):
    from collections import Counter
    dict = Counter(sorted(nums, reverse=True))
    n = sorted(dict, key=dict.get)
    freq = []
    for i in range(len(set(nums))):
        freq.extend([n[i]] * dict[n[i]])
    return freq
print(frequencySort([1,1,2,2,2,3]))
