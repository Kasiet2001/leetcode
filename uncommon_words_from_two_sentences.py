def uncommonFromSentences(s1, s2):
    uncommon_words = []
    lists = s1.split() + s2.split()
    for i in set(lists):
        if lists.count(i) == 1:
            uncommon_words.append(i)
    return uncommon_words
print(uncommonFromSentences("apple apple","banana"))
