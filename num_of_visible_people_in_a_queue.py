def canSeePersonsCount(heights):
    n = len(heights)
    ans = [0] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and heights[i] > st[-1]:
            st.pop()
            ans[i] += 1
        if st:
            ans[i] += 1
        st.append(heights[i])
    return ans
print(canSeePersonsCount([10,6,8,5,11,9]))