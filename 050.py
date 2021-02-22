import datetime
import Utilities
import itertools 

start_time = datetime.datetime.now()

max_i = 999999

a = Utilities.Eratosthenes(max_i)
a_len = len(a)
b = []
sum = 0
for i in range(1, a_len):
    sum += a[i - 1]
    b.append(sum)

b_len = len(b)
ds_max = 0
curr_number = 0
for i in range(curr_number, b_len):
    for j in range(i - curr_number + 1, 0, -1):
        ds = b[i] - b[j]
        if ds > max_i:
            break
        if ds in a:
            curr_number = i - j
            ds_max = ds

print(ds_max, curr_number)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
