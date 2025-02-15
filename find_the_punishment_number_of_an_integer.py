def punishmentNumber(n):
    def partition(num, target):
        if not num and target == 0:
            return True
        if target < 0:
            return False
        for index in range(len(num)):
            left = num[:index + 1]
            right = num[index + 1:]
            left_num = int(left)
            if partition(right, target - left_num):
                return True
        return False
    punishment_num = 0
    for i in range(1, n + 1):
        num = i * i
        if partition(str(num), i):
            punishment_num += num
    return punishment_num
print(punishmentNumber(37))