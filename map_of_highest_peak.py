from collections import deque
def highestPeak(isWater):
    def _is_valid_cell(x, y, rows, columns):
        return 0 <= x < rows and 0 <= y < columns
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    rows = len(isWater)
    columns = len(isWater[0])

    cell_heights = [[-1 for _ in range(columns)] for _ in range(rows)]

    cell_queue = deque()

    for x in range(rows):
        for y in range(columns):
            if isWater[x][y] == 1:
                cell_queue.append((x, y))
                cell_heights[x][y] = 0

    height_of_next_layer = 1

    while cell_queue:
        layer_size = len(cell_queue)
        for _ in range(layer_size):
            current_cell = cell_queue.popleft()

            for d in range(4):
                neighbor_x = current_cell[0] + dx[d]
                neighbor_y = current_cell[1] + dy[d]

                if (
                        _is_valid_cell(
                            neighbor_x, neighbor_y, rows, columns
                        )
                        and cell_heights[neighbor_x][neighbor_y] == -1
                ):
                    cell_heights[neighbor_x][
                        neighbor_y
                    ] = height_of_next_layer
                    cell_queue.append((neighbor_x, neighbor_y))

        height_of_next_layer += 1

    return cell_heights


print(highestPeak([[0,0,1],[1,0,0],[0,0,0]]))


