def guessNumber(n):
    high = n
    low = 1
    while low <= high:
        mid = (high + low) // 2
        guessed = guess(mid)
        if guessed == 0:
            return mid
        elif guessed == -1:
            high = mid - 1
        else:
            low = mid + 1
    return low
