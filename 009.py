# Special Pythagorean triplet

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# https://projecteuler.net/problem=9

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
