import datetime
import Utilities
from itertools import permutations

start_time = datetime.datetime.now()

a = [9, 8, 7, 6, 5, 4]
i_max = 0
need_to_break = False
for i in a:
    if need_to_break:
        break
    s = ''
    for j in range(1, i + 1):
        s = str(j) + s
    b = [int(''.join(p)) for p in permutations(s)]
    b.sort(reverse=True)
    for k in b:
        if Utilities.IsPrime(k):
            if i_max < k:
                i_max = k
                need_to_break = True
                break
print(i_max)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
