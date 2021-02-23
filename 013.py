# Large sum

# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.(file num13.txt)

f = open('num13.txt') 
s = f.readlines()
l = str(sum([int(i) for i in s]))
print(l[0:10])