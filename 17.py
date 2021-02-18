nums={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    }

def GenerateNumberString(n):
    if n in nums:
        return nums[n]
    s_n = str(n)
    if n < 20:
        return nums[int(s_n[1])] + 'teen'
    elif n < 100:
        ed = int(s_n[1])
        d = n - ed
        return nums[d] + nums[ed]
    elif n < 1000:
        h = int(s_n[0])
        if s_n[1:3]=='00':
            return nums[h]+'hundred'
        else:
            return nums[h]+'hundredand' + GenerateNumberString(int(s_n[1:3]))
    elif n == 1000:
        return 'onethousand'

summ = 0
for i in range(1, 1001):
    s = GenerateNumberString(i)
    summ += len(s)
print(summ)
