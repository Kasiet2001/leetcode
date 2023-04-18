def countPairs(deliciousness):
    from collections import defaultdict
    res = 0
    freq = defaultdict(int)
    for i in deliciousness:
        for j in range(22):
            res += freq[2 ** j - i]
        freq[i] += 1
    return res % 1_000_000_007
print(countPairs([1,3,5,7,9]))