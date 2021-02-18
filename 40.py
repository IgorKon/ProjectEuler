import datetime

start_time = datetime.datetime.now()

s = '123456789101'
next10 = 1
i = 11
len_s = 12
iCount = 7
i = 1
while True:
    si = str(i)
    len_s += len(si)
    if len(len_s) >= next10:
        print(s[next10])
        next10 *= 10
        i += 1
        if i > iCount:
            break

stop_time = datetime.datetime.now()
print(stop_time - start_time)
