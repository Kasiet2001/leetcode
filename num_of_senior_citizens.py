def countSeniors(details):
    ans = 0
    for c in details:
        flag = False
        age = ''
        for i in range(len(c) - 2):
            if flag:
                age += c[i]
            if c[i].isalpha():
                flag = True
        if int(age) > 60:
            ans += 1
    return ans
print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))