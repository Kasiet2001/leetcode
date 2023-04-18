def checkRecord(s):
    return False if s.count('A') >= 2 or 'LLL' in s else True

print(checkRecord("AA"))