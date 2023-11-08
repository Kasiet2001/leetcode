def isReachableAtTime(sx, sy, fx, fy, t):
    if sx == fx and sy == fy:
        return t != 1
    return max(abs(fx - sx), abs(fy - sy)) <= t