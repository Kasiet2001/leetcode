from collections import defaultdict
def relocateMarbles(nums, moveFrom, moveTo):
    marbles = set(nums)
    for f, t in zip(moveFrom, moveTo):
        marbles.remove(f)
        marbles.add(t)
    return marbles
print(relocateMarbles([1,1,3,3], [1,3], [2,2]))