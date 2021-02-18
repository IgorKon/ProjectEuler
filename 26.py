from decimal import Decimal, getcontext
import re
def GetPeriodLength(s):
    result = max(re.findall(r'((\w+?)\2+)', s), key=lambda t: len(t[0]))
    if len(result) < 2:
        return ""
    return result[1]

getcontext().prec = 15000
b_max = ''
max_len = 0
i_max = 0
for i in range(3, 1000):
    s = '{0:.15000f}'.format(Decimal(1.0) / Decimal(i))
    b = GetPeriodLength(s[2::])
    b_len = len(b)
    if max_len < b_len:
        max_len = b_len
        b_max = b
        i_max = i
print(i_max, max_len, b_max)
print('{0:.15000f}'.format(Decimal(1.0) / Decimal(i_max)))
