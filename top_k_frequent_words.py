def topKFrequent(words, k):
    dict = {}
    for i in sorted(words):
        dict[i] = words.count(i)
    freq_w = sorted(dict, key=dict.get, reverse=True)
    return freq_w[:k]
print(topKFrequent(["i","love","leetcode","i","love","coding"], 3))