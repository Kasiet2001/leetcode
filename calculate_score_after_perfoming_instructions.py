def calculateScore(instructions, values):
    score = 0
    i = 0
    visited = set()
    n = len(instructions)
    while i not in visited and i < n:
        visited.add(i)
        if instructions[i] == 'add':
            score += values[i]
            i += 1
        else:
            i += values[i]
            i %= n
    return score
print(calculateScore(["jump","add","add","jump","add","jump"], [2,1,3,1,-2,-3]))
