def hIndex(citations) -> int:
    length = len(citations)
    citations.sort()
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0
print(hIndex([3,0,6,1,5]))