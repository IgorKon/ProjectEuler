# Digit cancelling fractions

# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may 
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples. 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# https://projecteuler.net/problem=33

def GetDividers(n):
    m = n
    dividers = []
    i = 2
    while i <= m:
        if m % i == 0:
            dividers.append(i)
            m = m // i
        else:
            i += 1
    return dividers
def OneCommonDigit(si, sj):
    i = 1
    j = 1
    iCount = 0
    i1 = sj.find(si[0])
    if i1 != -1:
        iCount += 1
    i2 = sj.find(si[1])
    if i2 != -1:
        iCount += 1
    if iCount == 1:
        if i1 != -1:
            i = int(si[1])
            if i1 == 0:
                j = int(sj[1])
            else:
                j = int(sj[0])
        else:
            i = int(si[0])
            if i2 == 0:
                j = int(sj[1])
            else:
                j = int(sj[0])
    return ((iCount == 1), i, j)
iii = 1
jjj = 1
for i in range(11, 99):
    for j in range(i, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue
        si = str(i)
        sj = str(j)
        (bOne, ii, jj) = OneCommonDigit(si, sj)
        if not bOne:
            continue
        if i / j == ii / jj:
            print(i, j, ii, jj)
            iii *= ii
            jjj *= jj
#print(iii, jjj)
dividers_i = GetDividers(iii)
dividers_j = GetDividers(jjj)
i = 0
while i < len(dividers_i):
    d = dividers_i[i]
    if d in dividers_j:
        dividers_j.remove(d)
        dividers_i.pop(i)
    else:
        i += 1
#print(dividers_i)
#print(dividers_j)
z = 1
for j in dividers_j:
    z *= j
print(z)
