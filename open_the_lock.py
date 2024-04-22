from collections import deque
def openLock(deadends, target):
    next_num = {"0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "0"}
    prev_num = {"0": "9", "1": "0", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8"}
    visited = set(deadends)
    q = deque()
    turns = 0
    if '0000' in visited:
        return -1
    visited.add('0000')
    q.append('0000')
    while q:
        curr_q_len = len(q)
        for _ in range(curr_q_len):
            curr_comb = q.popleft()
            if curr_comb == target:
                return turns
            for wheel in range(4):
                new_comb = list(curr_comb)
                new_comb[wheel] = next_num[new_comb[wheel]]
                new_comb_str = ''.join(new_comb)
                if new_comb_str not in visited:
                    visited.add(new_comb_str)
                    q.append(new_comb_str)

                new_comb = list(curr_comb)
                new_comb[wheel] = prev_num[new_comb[wheel]]
                new_comb_str = ''.join(new_comb)
                if new_comb_str not in visited:
                    visited.add(new_comb_str)
                    q.append(new_comb_str)
        turns += 1
    return -1
print(openLock(["8888"], "0009"))