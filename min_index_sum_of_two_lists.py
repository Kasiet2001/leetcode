def findRestaurant(list1, list2):
    dict = {}
    for i in list1:
        if i in list2:
            dict[i] = list1.index(i) + list2.index(i)
    w = []
    ind = min(dict.values())
    for k, v in dict.items():
        if v == ind:
            w.append(k)
    return w
print(findRestaurant(["happy","sad","good"],["sad","happy","good"]))
