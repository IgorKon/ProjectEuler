import datetime
import math

start_time = datetime.datetime.now()

def CalcPentagonalNum(i):
    return ((i * (3 * i - 1)) // 2)

def IsPentagonalNum(i):
    d1 = 24 * i + 1
    d2 = math.sqrt(d1)
    d3 = d2 + 1
    return (((int(d2) * int(d2)) == d1) and (d3 % 6 == 0))

i = 1
a = []
need_to_continue = True
while need_to_continue:
    i += 1
    n = ((i * (3 * i - 1)) // 2)
    for j in range (i - 1, 1, -1):
        m = ((j * (3 * j - 1)) // 2)
        if IsPentagonalNum(n - m) and IsPentagonalNum(n + m):
            a.append(n - m)
            need_to_continue = False
            break

print(a[0])

stop_time = datetime.datetime.now()
print(stop_time - start_time)
