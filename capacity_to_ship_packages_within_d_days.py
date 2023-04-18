def shipWithinDays(weights, days):
    l = max(weights)
    r = sum(weights)
    while l < r:
        mid = (r + l) // 2
        day_count = 1
        total_weight = 0
        for w in weights:
            total_weight += w
            if total_weight > mid:
                day_count += 1
                total_weight = w
        if day_count > days:
            l = mid + 1
        else:
            r = mid
    return l
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))