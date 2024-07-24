def sortJumbled(mapping, nums):
    store_pairs = []
    for i in range(len(nums)):
        number = str(nums[i])
        formed = ""
        for j in range(len(number)):
            formed = formed + str(mapping[int(number[j])])
        mapped_value = int(formed)
        store_pairs.append((mapped_value, i))
    store_pairs.sort()
    answer = []
    for pair in store_pairs:
        answer.append(nums[pair[1]])
    return answer
print(sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]))