def largestTimeFromDigits(arr):
    from itertools import permutations
    arr = list(permutations(sorted(arr, reverse=True)))
    for h1, h2, m1, m2 in arr:
        if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
            return f'{h1}{h2}:{m1}{m2}'
    return ''
print(largestTimeFromDigits([5,5,5,5]))
