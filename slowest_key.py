def slowestKey(releaseTimes, keysPressed):
    key = [keysPressed[0]]
    rel_time = releaseTimes[0]
    for i in range(1, len(releaseTimes) - 1):
        if releaseTimes[i] - releaseTimes[i - 1] == rel_time:
            key.append(keysPressed[i])
        if releaseTimes[i] - releaseTimes[i - 1] > rel_time:
            rel_time = releaseTimes[i] - releaseTimes[i - 1]
            key = [keysPressed[i]]
    return max(key)
print(slowestKey([9,29,49,50], "cbcd"))