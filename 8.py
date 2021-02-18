def Mult(a):
    res = 1
    for j in a:
        res *= j
    return res



f = open('num1.txt') 
s = f.readline()
n = []
for ch in s:
    n.append(int(ch))
i_start = 0
i_count = 13
i_len = len(n)
max_mult = 0
max_a = []
while True:
    i_stop = i_start + i_count
    if i_stop > i_len: break
    a = n[i_start:i_stop]
    mult = Mult(a)
    if max_mult < mult: 
        max_mult = mult
        max_a = a
    i_start += 1

print(max_a, max_mult)
