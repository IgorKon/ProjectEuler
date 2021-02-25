# Maximum path sum I

# Problem 18
# https://projecteuler.net/problem=18

f = open('num18.txt') 
lines = f.readlines()
n = []
i = 0
for line in lines:
    n.append([])
    s_nums = line.split()
    for s in s_nums:
        n[i].append(int(s))
    print(n[i])
    i += 1
i = len(n) - 2
while i >= 0:
    CountInLine = len(n[i])
    for j in range(CountInLine):
        sum1 = n[i][j] + n[i+1][j]
        sum2 = n[i][j] + n[i+1][j+1]
        if sum1 > sum2:
            n[i][j] = sum1
        else:
            n[i][j] = sum2
    for a in n:
        print(a)
    i -= 1