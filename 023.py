import math
def DividersSum(n):
    m = math.sqrt(n)
    dividers = set()
    dividers.add(1)
    i = 2
    while i <= m:
        if n % i == 0:
            dividers.add(i)
            m = n // i
            dividers.add(m)
        i += 1
    a = list(dividers)
    return sum(a)
result = set(range(1, 28123))
izbytNumbers = []
for i in range(1, 28124):
    if i < DividersSum(i):
        izbytNumbers.append(i)
iCount = len(izbytNumbers)
print(iCount)        
for i in range(iCount):
    for j in range(iCount):
        sum2 = izbytNumbers[i] + izbytNumbers[j]
        if sum2 in result:
            result.remove(sum2)
print(len(result))
print("{0:,d}".format(sum(result)))
