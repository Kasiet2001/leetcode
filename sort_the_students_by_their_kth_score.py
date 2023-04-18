def sortTheStudents(score, k):
    st = sorted(score, key=lambda x: x[k], reverse=True)
    return st
print(sortTheStudents([[3,4],[5,6]], 0))