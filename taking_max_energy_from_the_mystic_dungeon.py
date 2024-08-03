def maximumEnergy(energy, k):
    for i in range(k, len(energy)):
        energy[i] = max(energy[i], energy[i] + energy[i - k])
    lst = energy[len(energy) - k:]
    return max(lst)
print(maximumEnergy([-2,-3,-1], 2))