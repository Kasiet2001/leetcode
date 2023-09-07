from collections import defaultdict
def checkStrings(s1, s2):
    d1_even = defaultdict(int)
    d2_even = defaultdict(int)
    d1_odd = defaultdict(int)
    d2_odd = defaultdict(int)
    for i in range(len(s1)):
        if i % 2:
            d1_odd[s1[i]] += 1
            d2_odd[s2[i]] += 1
        else:
            d1_even[s1[i]] += 1
            d2_even[s2[i]] += 1
    if d1_even == d2_even and d1_odd == d2_odd:
        return True
    return False
print(checkStrings("abe", "bea"))