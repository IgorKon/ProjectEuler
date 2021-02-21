import datetime
import Utilities

start_time = datetime.datetime.now()
i = 9
iCount = 0
res = []
while iCount < 11:
    i += 2
    b = False
    ii = 0
    if Utilities.IsPrime(i):
        s = str(i)
        iLength = len(s)
        for j in range(1, iLength):
            k = int(s[j::])
            if Utilities.IsPrime(k):
                ii += 1
                k = int(s[:iLength - j])
                if Utilities.IsPrime(k):
                    ii += 1
                else:
                    break
            else:
                break
        if ii == 2*iLength - 2:
            iCount += 1
            res.append(i)
print(sum(res))
print(res)
stop_time = datetime.datetime.now()
print(stop_time - start_time)