import datetime

def IsRightTriangle(m):
    return ((m[0]*m[0] + m[1]*m[1]) == (m[2]*m[2]))

start_time = datetime.datetime.now()
TheBestRightTriangles = []
TheBestP = 12
for p in range(12, 1001):
    rightTriangles = []    
    for i in range(1, p):
        for j in range(i, p - i):
            tri = [i, j, p - i - j]
            if IsRightTriangle(tri):
                rightTriangles.append(tri[:])
    if len(TheBestRightTriangles) < len(rightTriangles):
        TheBestRightTriangles = rightTriangles[:]
        TheBestP = p
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(TheBestP)
print(len(TheBestRightTriangles))
print(TheBestRightTriangles)