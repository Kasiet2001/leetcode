def check(self, num1, num2):
    first = str(num1)
    second = str(num2)

    while len(first) < len(second):
        first = "0" + first
    while len(second) < len(first):
        second = "0" + second

    diff_count = 0
    first_mismatch = -1
    second_mismatch = -1

    for i in range(len(first)):
        if first[i] != second[i]:
            diff_count += 1
            if diff_count == 1:
                first_mismatch = i
            elif diff_count == 2:
                second_mismatch = i
            else:
                return False
    if diff_count == 2:
        first = list(first)
        first[first_mismatch], first[second_mismatch] = first[second_mismatch], first[first_mismatch]
        first = ''.join(first)

    return first == second

def countPairs(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] or check(nums[i], nums[j]):
                count += 1
    return count


print(countPairs([3,12,30,17,21]))
