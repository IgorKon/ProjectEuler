def IsPifagorTree(a, b, c):
    return ((a*a + b*b) == c*c)

r = range(1, 1000)
bBreak = False
for a in r:
    for b in r:
        for c in r:
            if (a + b + c) == 1000:
                if IsPifagorTree(a, b, c):
                    print(a, b, c)
                    bBreak = True
                    break
        if bBreak: break
    if bBreak: break
