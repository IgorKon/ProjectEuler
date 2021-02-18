import datetime

def IsPalindrome(s):
    return s == s[::-1]

def IntToBinary(i):
    s2 = ''
    i2 = 1
    while i2 <= i:
        if i & i2 > 0:
            s2 = '1' + s2
        else:
            s2 = '0' + s2
        i2 *= 2
    return s2

start_time = datetime.datetime.now()
res2 = []
res10 = []
for i in range(1000000):
    if IsPalindrome(str(i)):
        s2 = IntToBinary(i)
        if  IsPalindrome(s2):
            res10.append(i)
            res2.append(s2)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(sum(res10))

