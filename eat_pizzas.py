from math import ceil
def maxWeight(pizzas):
    pizzas.sort()
    days = len(pizzas) // 4
    even = days // 2
    odd = days - even
    total_weight = 0
    while even or odd:
        if odd:
            total_weight += pizzas.pop()
            odd -= 1
        else:
            pizzas.pop()
            total_weight += pizzas.pop()
            even -= 1
    return total_weight
print(maxWeight([1,2,3,4,5,6,7,8]))