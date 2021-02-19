import datetime
import Utilities

start_time = datetime.datetime.now()

i = 143

while True:
    i += 1
    res = i * (2 * i - 1)
    if Utilities.IsPentagonalNum(res):
        break

print(res)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
