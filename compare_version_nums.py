def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    maxx_len = max(len(version1), len(version2))
    version1 = version1 + [0] * (maxx_len - len(version1))
    version2 = version2 + [0] * (maxx_len - len(version2))
    for i in range(maxx_len):
        if int(version1[i]) < int(version2[i]):
            return -1
        elif int(version1[i]) > int(version2[i]):
            return 1
    return 0
print(compareVersion("1.01", "1.001"))