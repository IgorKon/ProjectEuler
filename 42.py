import datetime

start_time = datetime.datetime.now()

def NumberByWord(s):
    a = bytearray('a', 'ascii')
    b = bytearray(s.lower(), 'ascii')
    return sum([i - a[0] + 1 for i in b])

def TriangularNumbers(max_i):
    a = set()
    i = 0
    j = 1
    while True:
        i += 1
        j = (i * (i + 1)) // 2
        if j > max_i:
            break
        a.add(j)
    return a

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
c = TriangularNumbers(j)
iCount = 0
for k in a:
    if k in c:
        iCount += 1
print(iCount)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
