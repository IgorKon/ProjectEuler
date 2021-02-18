def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

m = factorial(100)
print(m)
s = str(m)
sum = sum([int(ch) for ch in s])
print(sum)
