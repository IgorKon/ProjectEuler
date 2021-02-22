import datetime
import Utilities

start_time = datetime.datetime.now()
res = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
sr = ["1", "3", "7", "9"]
for i in range(101, 1000000, 2):
    si = str(i)
    bContinue = False
    for s in si:
        if not (s in sr):
            bContinue = True
            break
    if bContinue:
        continue
    if not Utilities.IsPrime(i):
        continue
    j = len(si)
    s1 = si
    for k in range(1, j):
        s1 = s1[-1] + s1[0:j-1]
        l = int(s1)
        if not Utilities.IsPrime(l):
            bContinue = True
            break
    if bContinue:
        continue
    res.append(i)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(len(res))
print(res)
