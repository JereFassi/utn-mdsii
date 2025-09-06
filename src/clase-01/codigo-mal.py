def f(d, t):
    r = 0
    for x in d:
        if t == "a":
            r += x * 0.21
        elif t == "b":
            r += x * 0.105
        else:
            r += x * 0.15
    return r

