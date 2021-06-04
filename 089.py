# Roman numerals

# Problem 89
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
# Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
# For example, it would appear that there are at least six ways of writing the number sixteen:
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, 
# as it uses the least number of numerals.
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, 
# Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
# Find the number of characters saved by writing each of these in their minimal form.
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
# https://projecteuler.net/problem=89

import datetime

RomanDigitsToArab = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
ToRomanD = [1000,900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1]
ToRomanS = ['M','CM','DCCC','DCC','DC','D','CD','CCC','CC','C','XC','LXXX','LXX','LX','L','XL','XXX','XX','X','IX','VIII','VII','VI','V','IV','III','II','I']

def FromRoman(sRoman : str) -> int:
    global RomanDigits
    summ : int = 0
    maxx : int = 1001
    i_prev : int = maxx
    for s in sRoman:
        try:
            i_next = RomanDigitsToArab[s]
            if i_next <= i_prev:
                summ += i_next
                i_prev = i_next
            else:
                summ += i_next - i_prev - i_prev
                i_prev = maxx
        except:
            return 0
    return summ

def ToRoman( num : int) -> str:
    global ToRomanD, ToRomanS
    s = ""
    rest = num
    count = len(ToRomanD)
    while rest > 0:
        for i in range(count):
            if rest >= ToRomanD[i]:
                rest -= ToRomanD[i]
                s += ToRomanS[i]
                break
    return s

start_time = datetime.datetime.now()
f = open('num89.txt') 
lines = f.readlines()
n = []
i = 0
l1 = 0
l2 = 0
for line in lines:
    sroman = line.replace('\n', '')
    l1 += len(sroman)
    k = FromRoman(sroman)
    s = ToRoman(k)
    l2 += len(s)
    i += 1
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(i, l1 - l2)
