def CollatzCount(n, count = 1):
    if(n == 1):
        return count
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    count += 1
    return CollatzCount(n, count)

max = 1
n_max = 1
for i in range(3, 1001):
    c = CollatzCount(i)
    if max < c:
        max = c
        i_max = i
print(i_max, max)
