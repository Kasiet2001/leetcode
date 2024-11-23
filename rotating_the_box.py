from collections import deque
def rotateTheBox(box):
    for row in box:
        q = deque([])
        for i in range(len(row) - 1, -1, -1):
            if row[i] == '.':
                q.append(i)
            elif row[i] == '*':
                q = deque([])
            else:
                if q:
                    idx = q.popleft()
                    row[idx] = '#'
                    row[i] = '.'
                    q.append(i)
    box.reverse()
    return list(zip(*box))
print(rotateTheBox([["#",".","*","."],
              ["#","#","*","."]]))

