# Summation of primes

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# https://projecteuler.net/problem=10

a = list(range(2, 2000))
sum = 0
i = 0
while True:
    p = a[i]
    j = i + 1
    while True:
        if j >= len(a): break
        b = a[j]
        if b % p == 0:
            a.remove(b)
        else:
            j += 1
    i += 1
    if i >= len(a): break
print(a)
sum = 0
for k in a:
    sum += k
print(sum)
