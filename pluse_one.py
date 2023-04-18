def plusOne(digits):
    digits = [str(i) for i in digits]
    digits = ''.join(digits)
    digits = int(digits) + 1
    return [int(str(digits)[i]) for i in range(len(str(digits)))]
print(plusOne([1, 9]))