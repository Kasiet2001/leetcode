def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    n = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
    return sum(n[:k])
print(kItemsWithMaximumSum(3, 2, 0, 4))