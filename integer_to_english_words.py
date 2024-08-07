def numberToWords(num):
    if num == 0:
        return 'Zero'
    onesString = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
                  18: "Eighteen", 19: "Nineteen"}
    tenString = {20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

    def helper(n):
        s = []
        hundreds = n // 100
        if hundreds:
            s.append(onesString[hundreds] + ' Hundred')
        last_2 = n % 100
        if last_2 >= 20:
            tens, ones = last_2 // 10, last_2 % 10
            s.append(tenString[tens * 10])
            if ones:
                s.append(onesString[ones])
        elif last_2:
            s.append(onesString[last_2])

        return ' '.join(s)

    postfix = ['', ' Thousand', ' Million', ' Billion']
    i = 0
    ans = []
    while num:
        digits = num % 1000
        res = helper(digits)
        if res:
            ans.append(res + postfix[i])
        num //= 1000
        i += 1
    ans.reverse()
    return ' '.join(ans)

print(numberToWords(12345))


