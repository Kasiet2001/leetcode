def countStudents(students, sandwiches):
    while students and sandwiches[0] in students:
        student = students.pop(0)
        if student == sandwiches[0]:
            sandwiches.pop(0)
        else:
            students.append(student)
    return len(students)
print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))
