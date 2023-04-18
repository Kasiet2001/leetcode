def discountPrices(sentence, discount):
    s = []
    m = discount / 100
    for i in sentence.split():
        if i[0] == '$' and i[1:].isnumeric():
            s.append('$' + ('%.2f' % (float(i[1:]) * (1-m))))
        else:
            s.append(i)
    return ' '.join(s)
print(discountPrices("there are $1 $2 and 5$ candies in the shop", 50))