def robotSim(commands, obstacles):
    obstacles = set(map(tuple, obstacles))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction_index = 0
    ans = 0

    for command in commands:
        if command == -2:
            direction_index = (direction_index - 1) % 4
        elif command == -1:
            direction_index = (direction_index + 1) % 4
        else:
            for _ in range(command):
                next_x = x + directions[direction_index][0]
                next_y = y + directions[direction_index][1]
                if (next_x, next_y) in obstacles:
                    break
                x, y = next_x, next_y
                ans = max(ans, x * x + y * y)
    return ans
print(robotSim([4,-1,3], []))
