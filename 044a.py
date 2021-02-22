import datetime
import Utilities

start_time = datetime.datetime.now()

i = 1
a = []
need_to_continue = True
while need_to_continue:
    i += 1
    n = ((i * (3 * i - 1)) // 2)
    for j in range (i - 1, 1, -1):
        m = ((j * (3 * j - 1)) // 2)
        if Utilities.IsPentagonalNum(n - m) and Utilities.IsPentagonalNum(n + m):
            a.append(n - m)
            need_to_continue = False
            break

print(a[0])

stop_time = datetime.datetime.now()
print(stop_time - start_time)
