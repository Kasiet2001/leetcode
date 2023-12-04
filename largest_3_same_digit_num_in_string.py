def largestGoodInteger(num):
    max_nums = ""
    prev = ''
    count = 0
    for i in num:
        if prev == i:
            count += 1
            if count == 3:
                max_nums = max(max_nums, i)
        else:
            count = 1
        prev = i
    return max_nums * 3 if max_nums else ''
print(largestGoodInteger("014455"))