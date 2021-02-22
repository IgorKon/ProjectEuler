f = open('num13.txt') 
s = f.readlines()
l = str(sum([int(i) for i in s]))
print(l[0:10])