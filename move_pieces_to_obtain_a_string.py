def canChange(start, target):
    length = len(start)
    start_idx, target_idx = 0, 0
    while start_idx < length or target_idx < length:
        while start_idx < length and start[start_idx] == '_':
            start_idx += 1
        while target_idx < length and target[target_idx] == '_':
            target_idx += 1
        if start_idx == length or target_idx == length:
            return start_idx == length and target_idx == length
        if (
            start[start_idx] != target[target_idx] or
                (start[start_idx] == 'L' and start_idx < target_idx) or
                (start[start_idx] == 'R' and start_idx > target_idx)
        ):
            return False

        start_idx += 1
        target_idx += 1
    return True
print(canChange("_L__R__R_", "L______RR"))




