import math
def GetAllDividers(n):
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
    a.sort()
    return a

friends = set()
sum_a = 0
for i in range(3, 10000):
    if i not in friends:
        dividers = GetAllDividers(i)
        sum_d = sum(dividers)
        if (i != sum_d) and (sum_d not in friends):
            dividers = GetAllDividers(sum_d)
            sum_d1 = sum(dividers)
            if i == sum_d1: 
                print(i, sum_d)
                friends.add(i)
                friends.add(sum_d)
                sum_a += i
                sum_a += sum_d
print(sum_a)
