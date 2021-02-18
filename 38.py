import datetime
import Utilities

def IsPanDigit(s):
    if len(s) == 9:
        if '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s:
            return True
    return False

def UnitedMult(i, a):
    s = ''
    for j in a:
        s += str(i * j)
    return int(s)

start_time = datetime.datetime.now()
i = 8
maxUM = 9
maxA = []
while True:
    i += 1
    a = [1, 2]
    um = UnitedMult(i, a)
    if um > 987654321:
        break
    j = 2
    while um <= 987654321:
        if IsPanDigit(str(um)):
            if maxUM < um:
                maxI = i
                maxUM = um
                maxA = a[:]
        j += 1
        a.append(j)
        um = UnitedMult(i, a)

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(maxI)
print(maxA)
print(maxUM)
