def minMoves2(nums):
        nums.sort()
        m = nums[len(nums) // 2]
        moves = 0
        for num in nums:
            moves += abs(num - m)
        return moves
print(minMoves2([1,10,2,9]))