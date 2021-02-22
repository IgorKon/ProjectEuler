import datetime
import Utilities
import re 

# Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, 
# is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.

start_time = datetime.datetime.now()

max_i = 999999
a = Utilities.Eratosthenes(max_i)
b = [i for i in a if (i >= (max_i + 1) // 10) and (len(re.findall(r'(\d).*\1.*\1', str(i))) > 0)]
d = {0, 1, 2, 3, 4, 5}
g3 = []
for i in b:
    si = str(i)
    e = re.findall(r'(\d).*\1.*\1', si)
    if len(e) == 1:
        s = e[0]
        pos = [j for j,s1 in enumerate(si) if s1 == s]
        if len(pos) > 3:
            continue
        f = list(d - set(pos))
        i1 = f[0]
        i2 = f[1]
        i3 = f[2]
        g1 = [k for k in b if str(k)[i1] == si[i1] and str(k)[i2] == si[i2] and str(k)[i3] == si[i3]]
        IsWrong = (len(g1) < 8)
        if not IsWrong:
            i1 = pos[0]
            i2 = pos[1]
            i3 = pos[2]
            iCount = 0
            g3.clear()
            for j in range(10):
                sj = str(j)
                g2 = [k for k in g1 if str(k)[i1] == sj and str(k)[i2] == sj and str(k)[i3] == sj]
                if len(g2) > 0:
                    iCount += 1
                    for gg in g2:
                        g3.append(gg)
            if iCount == 8:
                break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(g3)
print(min(g3))
