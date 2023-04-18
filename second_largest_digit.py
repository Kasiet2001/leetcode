def secondHighest(s):
    digits = sorted([int(i) for i in set(s) if i.isdigit()])
    return digits[-2] if len(digits) > 1 else -1
print(secondHighest("dfa12321afd"))