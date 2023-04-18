def twoEditWords(queries, dictionary):
    w = []
    for i in queries:
        for j in dictionary:
            t = sum([1 for n in range(len(i)) if i[n] == j[n]])
            if len(i) == len(j) and t >= len(i) - 2:
                t = 0
                w.append(i)
                break
    return w
print(twoEditWords(["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"], ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]))