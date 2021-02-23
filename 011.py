# Largest product in a grid

# Problem 11
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.(file num11.txt)
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def DialonalMax(a):
    k = len(a)
    if k == 0: return 0
    m = len(a[1])
    diag1 = 1
    diag2 = 1
    for i in range(k):
        for j in range(m):
            if i == j: diag1 *= a[i][j]
            if (i + j) == (k - 1): diag2 *= a[i][j]
    if diag1 > diag2: return diag1
    return diag2

def GetSquare(a, i, j, count):
    frame = []
    for i1 in range(i + count):
        line = []
        frame.append(line)
        for j1 in range(j, j + count):
            line.append(a[i1][j1])
    return frame

def TwoDimMax(a, i, j, count):
    k = len(a)
    if k == 0: return 0
    m = len(a[1])
    m1 = 1
    m2 = 1
    if i <= k - count: 
        for i1 in range(i, i + count):
            m1 *= a[i1][j]
    if j <= m - count: 
        for j1 in range(j, j + count):
            m2 *= a[i][j1]
    if m1 > m2: return m1
    return m2

count = 4
f = open('num11.txt')
a = f.readlines()
b = []
i = 0
for s in a:
    b.append(s.split())
d1 = []
i = 0
for c in b:
    d1.append([])
    for s in c:
        n = int(s)
        d1[i].append(n)
    i += 1
rows = len(d1)
columns = len(d1[0])
max1 = 0
i_max1 = -1
j_max1 = -1
frame = []
for i in range(rows - count):
    for j in range(columns - count):
        frame = GetSquare(d1, i, j, count)
        m = DialonalMax(frame)
        if max1 < m: 
            max1 = m
            i_max1 = i
            j_max1 = j
print(max1, i_max1, j_max1)
max2 = 0
i_max2 = -1
j_max2 = -1
for i in range(rows):
    for j in range(columns):
        m = TwoDimMax(d1, i, j, count)
        if max2 < m: 
            max2 = m
            i_max2 = i
            j_max2 = j
print(max2, i_max2, j_max2)
