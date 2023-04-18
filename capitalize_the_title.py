def capitalizeTitle(title):
    return ' '.join([i.capitalize() if len(i) > 2 else i for i in title.lower().split()])
print(capitalizeTitle("First leTTeR of EACH Word"))
