def lemonadeChange(bills):
    if bills[0] != 5:
        return False
    else:
        five = 0
        ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
                continue
            else:
                change = bills[i] - 5
                if change == 5:
                    five -= 1
                    ten += 1
                else:
                    five -= 1
                    if ten != 0:
                        ten -= 1
                    else:
                        five -= 2
                if five < 0 or ten < 0:
                    return False
        return True
print(lemonadeChange([5,5,5,5,20,20,5,5,20,5]))
