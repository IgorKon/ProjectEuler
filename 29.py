N = 101
a = set()
for i in range(2, N):
    for j in range(2, N):
        a.add( i**j)
print("{0:,d}".format(len(a)))