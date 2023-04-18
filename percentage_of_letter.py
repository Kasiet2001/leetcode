def percentageLetter(s, letter):
    return (s.count(letter) * 100) // len(s)
print(percentageLetter("foobar","o"))