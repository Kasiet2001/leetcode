def optimalDivision(self, nums: List[int]) -> str:
    if len(nums) == 1:
        return str(nums[0])
    ans = str(nums[0]) + '/' + '('
    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            ans += str(nums[i]) + ')'
        else:
            ans += str(nums[i]) + '/'
    return ans