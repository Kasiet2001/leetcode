def reorderSpaces(text):
    w = text.split()
    sp = text.count(' ')
    if len(w) == 1:
        return w[0] + (' ' * sp)
    spaces = sp // (len(w) - 1)
    sp_at_the_end = sp % (len(w) - 1)
    return (' ' * spaces).join(w) + (' ' * sp_at_the_end)
print(reorderSpaces("  walks  udp package   into  bar a"))