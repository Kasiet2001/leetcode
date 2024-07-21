def maxOperations(s):
    operations = 0
    ones_count = 0
    for i in range(len(s) - 1):
        if s[i] == '1':
            ones_count += 1
        if s[i] == '1' and s[i + 1] == '0':
            operations += ones_count

    return operations
print(maxOperations("110"))

