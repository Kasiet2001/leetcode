def removeDigit(number, digit):
    ans = []
    for i in range(len(number)):
        if number[i] == digit:
            ans.append(int(number[:i] + number[i + 1:]))
    return str(max(ans))
print(removeDigit("551", "5"))