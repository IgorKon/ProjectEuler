def IsPrimeFactor(i):
    if i in {2, 3, 5, 7}:
        return True
    if i < 2 or i % 2 == 0:
        return False
    if i % 3 == 0 or i % 5 == 0:
        return False
    r = int(i ** 0.5)
    f = 5
    while f <= r:
        if i % f == 0 or i % (f+2) == 0:
            return False
        f += 6
    return True