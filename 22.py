f = open('p022_names.txt') 
s = f.readline()
names = s.replace('"', '').split(",")
names.sort()
iCount = len(names)
iNum = 0
base = ord('A') - 1
for i in range(iCount):
    name = names[i]
    alfabet = 0
    for ch in name:
        alfabet += (ord(ch) - base)
    iNum += (i + 1) * alfabet

print("{0:,d}".format(iNum))