# Counting rectangles

# Problem 85
# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles.
# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

# https://projecteuler.net/problem=85

import datetime

target : int = 2000000
area : int = 0
x : int = 2000
y : int = 1
error : int = target
start_time = datetime.datetime.now()
x1 : int = x
y1 : int = y 

while x >= y:
    rects = (x * (x + 1) * y * (y + 1)) / 4
 
    if error > abs(rects - target):
        area = x * y
        error = abs(rects - target)
        x1 = x
        y1 = y
 
    if rects > target:
        x -= 1
    else:
        y += 1

stop_time = datetime.datetime.now()

print(stop_time - start_time)
print(area, x, y)
