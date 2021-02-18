prev1 = 1
prev2 = 2
sum = 2
while True:
    (prev1, prev2) = (prev2, prev1 + prev2)
    if prev2 > 4000000:
        break
    if prev2 % 2 == 0:
        sum += prev2
print(sum)