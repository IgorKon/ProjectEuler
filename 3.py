import Utilities

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

n=600851475143
dividers = GetDividers(n)
print(dividers)
for i in dividers[::-1]:
    if Utilities.IsPrimeFactor(i):
        print(i)
        break
