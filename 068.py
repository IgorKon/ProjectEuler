# Magic 5-gon ring

# Problem 68
# https://projecteuler.net/problem=68

import datetime
import itertools
start_time = datetime.datetime.now()
# For 16-digit string we need '10' on the external node of the ring
# For maximum string we need all our digits from '6' to '10' on the external nodes of the ring
# So create the template with digits '6' - '10' at the first nodes and try to find all possible
# places for digits '1' - '5' at the internal nodes of the ring
maxs = 0
a_min_idx = 0
at = itertools.permutations([6, 7, 8, 9, 10])
a = []
a.append([0, 0, 0])
a.append([0, 0, 0])
a.append([0, 0, 0])
a.append([0, 0, 0])
a.append([0, 0, 0])
for aa in at:
    a[0][0] = aa[0]
    a[1][0] = aa[1]
    a[2][0] = aa[2]
    a[3][0] = aa[3]
    a[4][0] = aa[4]
    if aa[0] == 6:
        a_min_idx = 0
    elif aa[1] == 6:
        a_min_idx = 1
    elif aa[2] == 6:
        a_min_idx = 2
    elif aa[3] == 6:
        a_min_idx = 3
    elif aa[4] == 6:
        a_min_idx = 4
    c = itertools.permutations([1, 2, 3, 4, 5])
    for cc in c:
        b = a[:][:]
        b[0][1] = cc[0]
        b[0][2] = cc[1]
        b[1][1] = cc[1]
        b[1][2] = cc[2]
        b[2][1] = cc[2]
        b[2][2] = cc[3]
        b[3][1] = cc[3]
        b[3][2] = cc[4]
        b[4][1] = cc[4]
        b[4][2] = cc[0]
        # if cc[0] == 5 and cc[1] == 3 and cc[2] == 1 and cc[3] == 4:
        #     print(cc)
        s0 = sum(b[0])
        s1 = sum(b[1])
        s2 = sum(b[2])
        if s0 == s1 and s1 == s2:
            s3 = sum(b[3])
            if s2 == s3:
                if s3 == sum(b[4]):
                    ss = ''
                    iCount = 0
                    i = a_min_idx
                    while iCount < 5:
                        bb = b[i]
                        for sb in bb:
                            ss += str(sb)
                        i += 1
                        if i > 4:
                            i = 0
                        iCount += 1
                    m1 = int(''.join(s for s in ss))
                    if maxs < m1:
                        maxs = m1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(maxs)
