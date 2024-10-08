def minSwaps(s):
    opening = 0
    for i in s:
        if i == '[':
            opening += 1
        else:
            if opening:
                opening -= 1
    return (opening + 1) // 2
print(minSwaps("][][]["))