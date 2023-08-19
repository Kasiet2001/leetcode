def maximumSwap(num):
    num = list(str(num))
    max_ind = len(num) - 1
    large = small = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] > num[max_ind]:
            max_ind = i
        elif num[i] < num[max_ind]:
            small = i
            large = max_ind
    num[small], num[large] = num[large], num[small]
    return int(''.join(num))
print(maximumSwap(98368))