def maximumCandies(candies, k):
    def can_allocate(candies, k, middle):
        max_num_of_children = 0
        for n in candies:
            max_num_of_children += n // middle
        return max_num_of_children >= k
    left = 0
    right = max(candies)
    while left < right:
        middle = (left + right + 1) // 2
        if can_allocate(candies, k, middle):
            left = middle
        else:
            right = middle - 1
    return left
print(maximumCandies([5,8,6], 3))