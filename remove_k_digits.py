def removeKdigits(num, k):
    st = []
    for n in num:
        while st and k and st[-1] > n:
            st.pop()
            k -= 1
        st.append(n)
    while k > 0:
        st.pop()
        k -= 1
    ans = ''.join(st).lstrip('0')
    return ans if ans else '0'
print(removeKdigits("1432219", 3))