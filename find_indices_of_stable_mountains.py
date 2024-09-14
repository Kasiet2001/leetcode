def stableMountains(height, threshold):
    return [i for i in range(1, len(height)) if threshold < height[i - 1]]
print(stableMountains([1,2,3,4,5], 2))