def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for d, t in enumerate(temperatures):
        d_t = (d, t)
        while stack and d_t[1] > stack[0][1]:
            ans[stack[0][0]] = d_t[0] - stack[0][0]
            stack.pop(0)
        stack.insert(0, d_t)
    return ans
print(dailyTemperatures([73,74,75,71,69,72,76,73] ))