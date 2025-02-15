def separateSquares(squares):
    events = []

    for x, y, l in squares:
        events.append((y, l))
        events.append((y + l, -l))

    events.sort()

    total_area = 0
    active_width = 0
    prev_y = 0
    area_below = 0

    for curr_y, width_change in events:
        if active_width > 0:
            total_area += active_width * (curr_y - prev_y)
        active_width += width_change
        prev_y = curr_y

    active_width = 0
    prev_y = 0

    for curr_y, width_change in events:
        if active_width > 0:
            new_area_below = area_below + active_width * (curr_y - prev_y)
            if new_area_below >= total_area / 2:
                remaining = (total_area / 2) - area_below
                return prev_y + remaining / active_width

            area_below = new_area_below

        active_width += width_change
        prev_y = curr_y

    return -1
print(separateSquares([[0,0,1],[2,2,1]]))