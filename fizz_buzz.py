def fizzBuzz(n):
    m = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            m.append('FizzBuzz')
        elif i % 3 == 0:
            m.append('Fizz')
        elif i % 5 == 0:
            m.append('Buzz')
        else:
            m.append(str(i))
    return m
print(fizzBuzz(5))