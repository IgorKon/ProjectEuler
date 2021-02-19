import math

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

def Mult(a):
    res = 1
    for j in a:
        res *= j
    return res

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def GetAllDividers(n):
    m = math.sqrt(n)
    dividers = set()
    dividers.add(1)
    i = 2
    while i <= m:
        if n % i == 0:
            dividers.add(i)
            m = n // i
            dividers.add(m)
        i += 1
    a = list(dividers)
    a.sort()
    return a

def IsPalindromeStr(s):
    return s == s[::-1]

def IsPanDigit(i):
    s = str(i)
    k = len(s)
    a = [int(s1) for s1 in s]
    a.sort()
    b = [i for i in range(1, k + 1)]
    return (a == b)