import math
import datetime

def is_perf_sq(n):
    x=math.ceil((math.sqrt(n)))
    if x*x==n:
        return True
    else:
        return False

def max_triangular(m):
    x=3
    n=2
    num = 3
    while n<=m:
        n = 2
        num += x
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                n += 1
        if is_perf_sq(num):
                n -= 1
        x += 1
    return num

start_time = datetime.datetime.now()
print(start_time)

print(max_triangular(500))

stop_time = datetime.datetime.now()
print(stop_time - start_time)
