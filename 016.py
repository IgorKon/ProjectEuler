n = 2 << 1000
s_n = str(n)
sum_n = sum([int(s) for s in s_n])
print("{0:,d}".format(n))
print("{0:,d}".format(sum_n))