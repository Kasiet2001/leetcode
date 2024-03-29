def minimumBoxes(apple, capacity):
    capacity.sort(reverse=True)
    ans = 0
    apple = sum(apple)
    for i in capacity:
        if apple > 0:
            apple -= i
            ans += 1
        else:
            return ans
    return ans
print(minimumBoxes([1,3,2],[4,3,1,5,2]))