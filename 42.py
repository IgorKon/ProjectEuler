import datetime
import Utilities

start_time = datetime.datetime.now()

def NumberByWord(s):
    a = bytearray('a', 'ascii')
    b = bytearray(s.lower(), 'ascii')
    return sum([i - a[0] + 1 for i in b])

f = open('num42.txt') 
s = f.readlines()
f.close()
a = []
for s1 in s:
    b = s1.replace('"', '').split(",")
    for s2 in b:
        i = NumberByWord(s2)
        a.append(i)
j = max(a)
c = Utilities.TriangularNumbers(j)
iCount = 0
for k in a:
    if k in c:
        iCount += 1
print(iCount)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
