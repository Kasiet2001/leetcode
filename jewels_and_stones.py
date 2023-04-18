def numJewelsInStones(jewels, stones):
    return sum([stones.count(i) for i in jewels])
print(numJewelsInStones("aA", "aAAbbbb"))