def maximumTime(time):
    h, m = time.split(':')
    h, m = list(h), list(m)
    if h[0] == '?':
        if h[1] in '?0123':
            h[0] = '2'
        else:
            h[0] = '1'
    if h[1] == '?':
        if h[0] == '2':
            h[1] = '3'
        else:
            h[1] = '9'
    if m[0] == '?':
        m[0] = '5'
    if m[1] == '?':
        m[1] = '9'
    return ''.join(h) + ':' + ''.join(m)
print(maximumTime("?4:03"))