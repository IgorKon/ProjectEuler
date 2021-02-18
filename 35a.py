import time
start_time = time.time()


foundprimes = []

def isPrime(n):
    """Determine if cand is a prime number"""
    if n in foundprimes:
        return True

    if n <= 3:
        return n > 1
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i=5
    while (i*i <= n):
        if n % i == 0:
            return False
        if n%(i+2) == 0:
            return False
        i+=6

    foundprimes.append(n)
    return True

def rotations(num):
    """Return all rotations of the given number"""

    if abs(num) < 10:
        return [num]

    numstr = str(num)
    strlen = len(numstr)
    returnarray = []
    for i in range(strlen):
        if i==0:
            pass
        else:
            start = numstr[i:]
            end = numstr[0:i]
            returnarray.append(int(start+end))


    return returnarray

def QCheck(num):
    """Do a quick check if there is an even number in the set...at some point it will be an even number in rotation"""
    numstr = str(num)
    for i in range(len(numstr)):
        if int(numstr[i]) % 2 == 0:
            return False
        if int(numstr[i]) % 5 == 0:
            return False

    return True


allrotations = [2,5]

for i in range(3,1000000,2):
    if QCheck(i):
        prime = isPrime(i)
        if prime:
            rotcheck = True
            for rot in rotations(i):
                if isPrime(rot) == False:
                    rotcheck = False

            if rotcheck:
                allrotations.append(i)

print(len(allrotations))
print("--- %s seconds ---" % (time.time() - start_time))
