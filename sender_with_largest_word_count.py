def largestWordCount(messages, senders):
    n = []
    d = {}
    for i in range(len(messages)):
        if senders[i] not in d:
            d[senders[i]] = messages[i].count(' ') + 1
        else:
            for k, v in d.items():
                if senders[i] == k:
                    d[k] = v + messages[i].count(' ') + 1
    l = max(d.values())
    for k, v in d.items():
        if v == l:
            n.append(k)
    return n[0] if len(n) == 1 else max(n)
print(largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"]))