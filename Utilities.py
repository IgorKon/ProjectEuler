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

def CalcTriangularNum(i):
    return ((i * (i + 1)) // 2)

def IsTriangularNum(i):
    d1 = 8 * i + 1
    d2 = math.sqrt(d1)
    d3 = d2 - 1
    return (((int(d2) * int(d2)) == d1) and (d3 % 2 == 0))

def TriangularNumbers(max_i):
    a = set()
    i = 0
    j = 1
    while True:
        i += 1
        j = (i * (i + 1)) // 2
        if j > max_i:
            break
        a.add(j)
    return a

def CalcPentagonalNum(i):
    return ((i * (3 * i - 1)) // 2)

def IsPentagonalNum(i):
    d1 = 24 * i + 1
    d2 = math.sqrt(d1)
    d3 = d2 + 1
    return (((int(d2) * int(d2)) == d1) and (d3 % 6 == 0))

def PentagonalNumbers(max_i):
    a = set()
    i = 0
    j = 1
    while True:
        i += 1
        j = (i * (3 * i - 1)) // 2
        if j > max_i:
            break
        a.add(j)
    return a

def CalcHexagonalNum(i):
    return (i * (2 * i - 1))

def IsHexagonalNum(i):
    d1 = 8 * i + 1
    d2 = math.sqrt(d1)
    d3 = d2 + 1
    return (((int(d2) * int(d2)) == d1) and (d3 % 4 == 0))

def HexagonalNumbers(max_i):
    a = set()
    i = 0
    j = 1
    while True:
        i += 1
        j = (i * (2 * i - 1))
        if j > max_i:
            break
        a.add(j)
    return a

def Eratosthenes1(n):
    a = [2]    
    for i in range(3, n + 1, 2):
        a.append(i)
    for i in range(1, n):
        j = len(a) - 1
        if i > j:
            break
        d = a[i]
        while j > i:
            k = a[j]
            if k % d == 0:
                del a[j]
            j -= 1
    return a

def Eratosthenes(n): 
    p = [True for i in range(n + 1)] 
    p[0] = False
    p[1] = False
    i = 2
    while (i * i <= n): 
        if (p[i]): 
            for j in range(i * 2, n + 1, i): 
                p[j] = False
        i += 1
    return [i for i in range(n + 1) if p[i]]