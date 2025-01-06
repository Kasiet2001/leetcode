def minOperations(boxes):
    n = len(boxes)
    ans = [0] * n
    balls_to_left = 0
    moves_to_left = 0
    balls_to_right = 0
    moves_to_right = 0
    for i in range(n):
        ans[i] += moves_to_left
        balls_to_left += int(boxes[i])
        moves_to_left += balls_to_left

        j = n - i - 1
        ans[j] += moves_to_right
        balls_to_right += int(boxes[j])
        moves_to_right += balls_to_right
    return ans
print(minOperations("001011"))
