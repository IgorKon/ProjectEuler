import time
def IsPolindromInt(k):
    a = str(k)
    l = int(a[::-1])
    return k == l

def IsPolindromStr(a):
    return a == a[::-1]

max = 0
t_start = time.time()
for i in range(100,1000):
    for j in range(100,1000):
        k = i * j
        if IsPolindromStr(str(k)) and max < k:
            max = k
print(max)
print(time.time() - t_start)