def get_num_of_bouquets(bloomDay, mid, k):
    num_of_bouquets = 0
    count = 0
    for day in bloomDay:
        if day <= mid:
            count += 1
        else:
            count = 0
        if count == k:
            num_of_bouquets += 1
            count = 0
    return num_of_bouquets
def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    start = 0
    end = max(bloomDay)
    minDays = -1

    while start <= end:
        mid = (start + end) // 2

        if get_num_of_bouquets(bloomDay, mid, k) >= m:
            minDays = mid
            end = mid - 1
        else:
            start = mid + 1

    return minDays
print(minDays([5,37,55,92,22,52,31,62,99,64,92,53,34,84,93,50,28], 8, 2))