def shiftDistance(s, t, nextCost, previousCost):
    n = len(s)
    total_cost = 0

    for i in range(n):
        current_pos = ord(s[i]) - ord('a')
        target_pos = ord(t[i]) - ord('a')

        forward_distance = (target_pos - current_pos + 26) % 26
        backward_distance = (current_pos - target_pos + 26) % 26

        forward_cost = sum(nextCost[(current_pos + j) % 26] for j in range(forward_distance))
        backward_cost = sum(previousCost[(current_pos - j + 26) % 26] for j in range(backward_distance))

        total_cost += min(forward_cost, backward_cost)

    return total_cost
print(shiftDistance("abab", "baba", [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))