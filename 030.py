N = (9**5) * 6 + 1
b = []
for i in range(2, N):
    a = [int(s) for s in str(i)]
    k = 0
    for j in a:
        k += j ** 5
    if k == i:
        b.append(i)
print(b)
print("{0:,d}".format(sum(b)))