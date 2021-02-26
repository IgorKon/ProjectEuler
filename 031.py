# Coin sums

# Problem 31
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
# https://projecteuler.net/problem=31

import datetime

start_time = datetime.datetime.now()
p1 = 1
p2 = 2
p5 = 5
p10 = 10
p20 = 20
p50 = 50
f1 = 100
count = 0
""" result = []
result.append("1*2£") """
for i_p1 in range(201):
    k = i_p1 * p1
    if k == 200:
        """ s = GetString(i_p1)
        result.append(s) """
        count += 1
        break
    for i_p2 in range(101):
        k = i_p1 * p1 + i_p2 * p2 
        if k == 200:
            """ s = GetString(i_p1, i_p2)
            result.append(s) """
            count += 1
            break
        if(k > 200): break
        for i_p5 in range(41):
            k = i_p1 * p1 + i_p2 * p2 + i_p5 * p5
            if k == 200:
                """ s = GetString(i_p1, i_p2, i_p5)
                result.append(s) """
                count += 1
                break
            if(k > 200): break
            for i_p10 in range(21):
                k = i_p1 * p1 + i_p2 * p2 + i_p5 * p5 + i_p10 * p10
                if k == 200:
                    """ s = GetString(i_p1, i_p2, i_p5, i_p10)
                    result.append(s) """
                    count += 1
                    break
                if(k > 200): break
                for i_p20 in range(11):
                    k = i_p1 * p1 + i_p2 * p2 + i_p5 * p5 + i_p10 * p10 + i_p20 * p20
                    if k == 200:
                        """ s = GetString(i_p1, i_p2, i_p5, i_p10, i_p20)
                        result.append(s) """
                        count += 1
                        break
                    if(k > 200): break
                    for i_p50 in range(5):
                        k = i_p1 * p1 + i_p2 * p2 + i_p5 * p5 + i_p10 * p10 + i_p20 * p20 + i_p50 * p50
                        if k == 200:
                            """ s = GetString(i_p1, i_p2, i_p5, i_p10, i_p20, i_p50)
                            result.append(s) """
                            count += 1
                            break
                        if(k > 200): break
                        for i_f1 in range(3):
                            k = i_p1 * p1 + i_p2 * p2 + i_p5 * p5 + i_p10 * p10 +\
                                i_p20 * p20 + i_p50 * p50 + i_f1 * f1
                            if(k == 200):
                                """ s = GetString(i_p1, i_p2, i_p5, i_p10, i_p20, i_p50, i_f1)
                                result.append(s) """
                                count += 1
                                break
                            if(k > 200): 
                                break

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print("{0:,d}".format(count))
#print("{0:,d}".format(len(result)))
#print(result)