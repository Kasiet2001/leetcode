def maxArea(height):
    ans = 0
    left = 0
    right = len(height) - 1
    while left < right:
        ans = max(ans, (right - left) * min(height[left], height[right]))
        if height[left] <= height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
    return ans
print(maxArea([1,1]))