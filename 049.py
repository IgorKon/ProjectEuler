import datetime
import Utilities
from itertools import permutations

start_time = datetime.datetime.now()

max_i = 9999

a = Utilities.Eratosthenes(max_i)
b = [i for i in a if i > 1000]
icount = 0
bFound = False
for i in b:
    c = set(int(k) for k in str(i))
    d = [j for j in b if j > i and (set((int(m) for m in str(j))) == c)]
    for j in d:
        for k in d:
            if k > j:
                if j - i == k - j:
                    print(i, j, k)
                    icount += 1
                    if icount == 2:
                        bFound = True
                        break
        if bFound:
            break
    if bFound:
        break
                
stop_time = datetime.datetime.now()
print(stop_time - start_time)
