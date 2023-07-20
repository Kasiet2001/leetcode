def asteroidCollision(asteroids):
    stack = []
    for i in asteroids:
        if not stack or i > 0:
            stack.append(i)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(i):
                stack.pop()
            if stack and stack[-1] == abs(i):
                stack.pop()
            else:
                if not stack or stack[-1] < 0:
                    stack.append(i)
    return stack
print(asteroidCollision([5,10,-5]))