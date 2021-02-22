import datetime
import Utilities
from itertools import permutations

start_time = datetime.datetime.now()

s = '1234567890'
a = [''.join(p) for p in permutations(s) if p[0] != '0' and (p[5] == '0' or p[5] == '5')]
#a = [''.join(p) for p in permutations(s) if p[0] != '0' and p[5] == '5']
print(len(a))
b=[]
for s1 in a:
    i = int(s1[1:4])
    if i % 2 != 0:
        continue
    i = int(s1[2:5])
    if i % 3 != 0:
        continue
    i = int(s1[3:6])
    if i % 5 != 0:
        continue
    i = int(s1[4:7])
    if i % 7 != 0:
        continue
    i = int(s1[5:8])
    if i % 11 != 0:
        continue
    i = int(s1[6:9])
    if i % 13 != 0:
        continue
    i = int(s1[7:10])
    if i % 17 != 0:
        continue
    b.append(int(s1))
print(b)
print(sum(b))
stop_time = datetime.datetime.now()
print(stop_time - start_time)
