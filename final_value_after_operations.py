def finalValueAfterOperations(operations):
    final = 0
    for i in operations:
        if i == '++X' or i == 'X++':
            final += 1
        else:
            final -= 1
    return final
print(finalValueAfterOperations(["++X","++X","X++"]))