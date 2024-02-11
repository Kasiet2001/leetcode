def nextGreaterElement(nums1, nums2):
    numsMap = {i: -1 for i in nums1}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            numsMap[stack[-1]] = num
            stack.pop()
        if num in numsMap:
            stack.append(num)
    return list(numsMap.values())
print(nextGreaterElement([2,4], [1,2,3,4]))
