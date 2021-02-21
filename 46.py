import datetime
import Utilities
import math

start_time = datetime.datetime.now()

max_i = 1000000

p_list = Utilities.Eratosthenes(max_i)
p_set = set(p_list)
print(max_i, len(p_list))
for i in range(9, max_i, 2):
    if not (i in p_set):
        j = 0
        NotFound = True
        while True:
            pp = p_list[j]
            if (i - pp) < 2:
                break
            d = i - pp
            if Utilities.IsSquare(d // 2):
                NotFound = False
                break
            j += 1
        if NotFound:
            print(i)
            break

stop_time = datetime.datetime.now()
print(stop_time - start_time)
