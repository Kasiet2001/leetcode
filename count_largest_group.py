from collections import defaultdict
def countLargestGroup(n: int) -> int:
    hashMap = dict()
    for num in range(1, n + 1):
        n = str(num)
        m = 0
        for i in n:
            m += int(i)
        hashMap[m] = hashMap.get(m, 0) + 1
    max_value = max(hashMap.values())
    return sum(1 for i in hashMap.values() if i == max_value)
print(countLargestGroup(13))