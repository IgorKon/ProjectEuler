import Utilities

max_count = 0
a_max_count = 0
b_max_count = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        count = 0
        for n in range(1000):
            k = n * n + a * n + b
            if Utilities.IsPrimeFactor(k):
                count += 1
                if max_count < count:
                    max_count = count
                    a_max_count = a
                    b_max_count = b
            else:
                break
print(a_max_count, b_max_count, max_count, a_max_count * b_max_count)

