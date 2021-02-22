a = range(2, 11)
s1 = 1
s2 = 1
for i in a:
    s1 += (i * i)
    s2 += i
s2 *= s2
print(s1)
print(s2)
print(s1 - s2)