import Utilities
f = {}
for i in range(10):
    f[i] = Utilities.factorial(i)
    print(i, f[i])
# Число содержит не более 7 знаков, так как 
# у 8-значного числа, даже состоящего только из 9-ток, сумма факториалов 8*9! = 2 903 040
# то есть это семизначное число
s = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        for o in range(10):
                            s1 = i * 1000000 + j * 100000 + k * 10000 + l * 1000 + m * 100 + n * 10 + o
                            if i==0:
                                if j == 0:
                                    if k == 0:
                                        if l==0:
                                            if m==0:
                                                if n==0:
                                                    if o==0:
                                                        continue
                                                    else:
                                                        s2 = f[o]
                                                else:
                                                    s2 = f[n] + f[o]
                                            else:
                                                s2 = f[m] + f[n] + f[o]
                                        else:
                                            s2 = f[l] + f[m] + f[n] + f[o]
                                    else:
                                        s2 = f[k] + f[l] + f[m] + f[n] + f[o]
                                else: # j > 0
                                    s2 = f[j] + f[k] + f[l] + f[m] + f[n] + f[o]
                            else: # i > 0
                                s2 = f[i] + f[j] + f[k] + f[l] + f[m] + f[n] + f[o]
                            if s1 > 2 and s1 == s2:
                                print(i, j, k, l, m, n, o)
                                s += s1
print(s)