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