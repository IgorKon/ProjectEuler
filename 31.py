import datetime

""" def GetString(i_p1, i_p2 = 0, i_p5 = 0, i_p10 = 0, i_p20 = 0, i_p50 = 0, i_f1 = 0):
    s = ""
    if i_p1 > 0:
        s = "{}*1".format(i_p1)
    if i_p2 > 0:
        if s == "":
            s = "{}*2".format(i_p2)
        else:
            s += " {}*2".format(i_p2)
    if i_p5 > 0:
        if s == "":
            s = "{}*5".format(i_p5)
        else:
            s += " {}*5".format(i_p5)
    if i_p10 > 0:
        if s == "":
            s = "{}*10".format(i_p10)
        else:
            s += " {}*10".format(i_p10)
    if i_p20 > 0:
        if s == "":
            s = "{}*20".format(i_p20)
        else:
            s += " {}*20".format(i_p20)
    if i_p50 > 0:
        if s == "":
            s = "{}*50".format(i_p50)
        else:
            s += " {}*50".format(i_p50)
    if i_f1 > 0:
        if s == "":
            s = "{}*1£".format(i_f1)
        else:
            s += " {}*1£".format(i_f1)
    return s
 """
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