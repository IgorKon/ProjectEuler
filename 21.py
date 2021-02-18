import Utilities

friends = set()
sum_a = 0
for i in range(3, 10000):
    if i not in friends:
        dividers = Utilities.GetAllDividers(i)
        sum_d = sum(dividers)
        if (i != sum_d) and (sum_d not in friends):
            dividers = Utilities.GetAllDividers(sum_d)
            sum_d1 = sum(dividers)
            if i == sum_d1: 
                print(i, sum_d)
                friends.add(i)
                friends.add(sum_d)
                sum_a += i
                sum_a += sum_d
print(sum_a)
