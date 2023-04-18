def topStudents(positive_feedback, negative_feedback, report, student_id, k):
    pos = set(positive_feedback)
    neg = set(negative_feedback)
    st = {}
    for i in range(len(report)):
        p = 0
        for j in report[i].split():
            if j in pos:
                p += 3
            elif j in neg:
                p -= 1
        st[student_id[i]] = p
    return sorted(student_id, key=lambda i: (-st[i], i))[:k]
print(topStudents(["smart","brilliant","studious"], ["not"],["this student is not studious","the student is smart"],[1,2],2))