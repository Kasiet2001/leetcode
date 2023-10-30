def sortByBits(arr):
    arr.sort()
    return sorted(arr, key=lambda x: bin(x).count('1'))
print(sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))