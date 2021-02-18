import math
import datetime

def IsSqr(n):
    x = math.ceil((math.sqrt(n)))
    return (x * x == n)

def GetCountDel(n):
    res = 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res += 1
    if IsSqr(n):
        res -= 1
    return res

start_time = datetime.datetime.now()
i = 1
Triangle = 1
while True:
    i += 1
    Triangle += i
    Count = GetCountDel(Triangle)
    if Count > 500:
        print(Triangle, Count)
        break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

