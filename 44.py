import datetime
from itertools import permutations

start_time = datetime.datetime.now()

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

def CalcPentagonalNum(i):
    return ((i * (3 * i - 1)) // 2)

j = 10000000
a = PentagonalNumbers(j)
b = [p for p in permutations(a, 2)]
max_a = max(a)
min_d = max_a
min_b1 = 0
min_b2 = 0
for b1, b2 in b:
    d = abs(b1 - b2)
    s = (b1 + b2)
    if s <= max_a:
        if (d in a) and (s in a):
            if min_d > d:
                min_d = d
                min_b1 = b1
                min_b2 = b2
print(min_d)
print(min_b1, min_b2)


stop_time = datetime.datetime.now()
print(stop_time - start_time)
