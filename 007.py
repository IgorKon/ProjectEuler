import Utilities
i = 6
n = 13
while True:
    n += 2
    if Utilities.IsPrime(n): i += 1
    if i == 10001: break
print(n)
print(104743)