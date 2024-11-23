def canAliceWin(n):
    stones = 10
    alice = False
    while n >= stones:
        n -= stones
        stones -= 1
        if alice:
            alice = False
        else:
            alice = True
    return alice
print(canAliceWin(19))