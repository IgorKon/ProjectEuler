# Permuted multiples

# Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import datetime

def GetDigits(i):
    return sorted(list(str(i)))

i = 100
start_time = datetime.datetime.now()
while True:
    i += 1
    s2 = sorted(list(str((2 * i))))
    s3 = sorted(list(str((3 * i))))
    if s2 == s3:
        s4 = sorted(list(str((4 * i))))
        if s3 == s4:
            s5 = sorted(list(str((5 * i))))
            if s4 == s5:
                s6 = sorted(list(str((6 * i))))
                if s5 == s6:
                    break
stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(i)
