from collections import defaultdict
def numEquivDominoPairs(dominoes):
    counter = defaultdict(int)
    total = 0
    for i in dominoes:
        small = min(i)
        big = max(i)
        sorted_dominoes = (small, big)
        if sorted_dominoes in counter:
            total += counter[sorted_dominoes]
        counter[sorted_dominoes] += 1
    return total
print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))