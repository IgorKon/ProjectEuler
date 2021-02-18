def CollatzCount(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    return count
max = 1
n_max = 1
for i in range(3, 1001):
    c = CollatzCount(i)
    if max < c:
        max = c
        n_max = i
print(n_max, max)
