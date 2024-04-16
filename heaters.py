def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()
    heater = 0
    ans = 0
    for house in houses:
        while heater + 1 < len(heaters) and abs(heaters[heater] - house) >= abs(heaters[heater + 1] - house):
            heater += 1
        ans = max(ans, abs(heaters[heater] - house))
    return ans

print(findRadius([1,1,1,1,1,1,999,999,999,999,999], [499,500,501]))