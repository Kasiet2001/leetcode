def canConstruct(ransomNote, magazine):
    t = 0
    for i in set(ransomNote):
        if ransomNote.count(i) <= magazine.count(i):
            t += 1
    return t == len(set(ransomNote))
print(canConstruct("a",'b'))

