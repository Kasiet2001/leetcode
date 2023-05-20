def nextGreaterElements(nums):
    st = []
    ans = [-1] * len(nums)
    for _ in range(2):
        for j in range(len(nums)):
            while st and nums[st[-1]] < nums[j]:
                ans[st.pop()] = nums[j]
            st.append(j)
    return ans
print(nextGreaterElements([1,2,3,4,3]))