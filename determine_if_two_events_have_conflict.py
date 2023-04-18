def haveConflict(event1, event2):
    event1 = [int(i[:2]) * 60 + int(i[3:]) for i in event1]
    event2 = [int(i[:2]) * 60 + int(i[3:]) for i in event2]
    if event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[1]:
        return True
    else:
        return False
print(haveConflict(["15:19","17:56"], ["14:11","20:02"]))