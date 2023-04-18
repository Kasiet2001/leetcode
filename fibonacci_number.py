def fib(n):
    fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[-1] + fib[-2])
    return fib[n]
print(fib(4))