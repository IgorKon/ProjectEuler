N = 1001
i = 0
j = N
r = 0
d = 1
a = [[0] * N for i in range(N)]
max = N * N
while d < 2 * N - 1:
    d += r // (N * d - d * d // 4)
    di = d % 4 - 1
    if di < 0:
        i -= di % 2
    else:
        i += di % 2
    di = d % 4 - 2
    if di < 0:
        j -= di % 2
    else:
        j += di % 2
    a[i][j] = max - r
    r += 1
sum_d = 0
for i in range(N):
    sum_d += a[i][i]
    if i != N // 2:
        sum_d += a[N - 1 - i][i]
""" f = open('num28.txt', 'w')
for i in range(N):
    s = ""
    for j in range(N):
        s += "{0:d},".format(a[i][j])
    l = len(s)
    s = s[:l-1:] + "\n"
    f.write(s)
f.close()
 """#print(a)
print("{0:,d}".format(sum_d))


