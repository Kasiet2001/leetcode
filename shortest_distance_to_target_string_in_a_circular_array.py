def closetTarget(words, target, startIndex):
    n = 0
    for i in range(len(words)):
        forward = (startIndex + i) % len(words)
        backward = startIndex - i
        if words[backward] == target or words[forward] == target:
            return n
        n += 1
    return -1
print(closetTarget(["i","eat","leetcode"], "ate", 0))
