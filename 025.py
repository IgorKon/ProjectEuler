# 1000-digit Fibonacci number

# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# https://projecteuler.net/problem=25

def F(n):
    if n == 1: return 1
    if n == 2: return 1
    return F(n - 1) + F(n - 2)
fn2 = 1
fn1 = 1
i = 2
limit = 10 ** (1000 - 1)
while fn1 < limit:
    fn1, fn2 = fn1 + fn2, fn1
    i += 1
print(fn1, i)