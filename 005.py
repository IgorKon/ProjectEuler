def GetDividers(n):
    m = n
    k = 2
    result = {}
    while True:
        if (m % k == 0):
            m /= k
            if k in result:
                result[k] += 1
            else:
                result[k] = 1
        else:
            k += 1
        if k > m: break
    return result


a = list(range(2, 21))
d = {}
for i in a:
    c = GetDividers(i)
    for j in c:
        if j in d:
            if d[j] < c[j]:
                d[j] = c[j]
        else:
            d[j] = c[j]
res = 1
for i in d:
    k = 1
    while True:
        res *= i
        k += 1
        if k > d[i]: break
print(d)
print(res)

