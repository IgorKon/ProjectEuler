# Anagramic squares

# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36**2. 
# What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96**2. 
# We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, 
# neither may a different letter have the same digital value as another letter.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
# find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
# What is the largest square number formed by any member of such a pair?
# NOTE: All anagrams formed must be contained in the given text file.
# https://projecteuler.net/problem=98

import datetime
from http.client import LineTooLong
import math

def CreateDictOfSquares() -> dict:
    squares = dict()
    for i in range(4, 31622):
        sq = i * i
        s = str(sq)
        l = len(s)
        if not (l in squares):
            lst = list()
            lst.append(sq)
            squares[l] = lst
        else:
            lst = squares[l]
            lst.append(sq)
    return squares

def get_max_squares(word1 : str, word2 : str, squares : list) -> int:
    iResult = -1
    DigitsByLetters = dict()
    LettersByDigits = dict()
    length = len(word1)
    for sq in squares:
        DigitsByLetters.clear()
        LettersByDigits.clear()
        s_digit = str(sq)
        for i in range(length):
            DigitsByLetters[word1[i]] = s_digit[i]
            LettersByDigits[s_digit[i]] = word1[i]
        digital_str_by_letter = ''
        word_str_by_digit = ''
        for i in range(length):
            digital_str_by_letter += str(DigitsByLetters[word1[i]])
            word_str_by_digit += str(LettersByDigits[s_digit[i]])
        if (s_digit == digital_str_by_letter) and (word1 == word_str_by_digit):
            digital_str_by_letter = ''
            for i in range(length):
                digital_str_by_letter += str(DigitsByLetters[word2[i]])
            d = int(digital_str_by_letter)
            if d in squares:
                if iResult < sq:
                    iResult = sq
                if iResult < d:
                    iResult = d
    return iResult

start_time = datetime.datetime.now()
squares = CreateDictOfSquares()
f = open('num98.txt') 
lines = f.readlines()
words = lines[0].replace('"', '').split(",")
iCount = len(words)
letters = dict()
words_lst = list()
for i in range(iCount):
    word1 = words[i]
    word11 = sorted(word1)
    length1 = len(word1)
    for j in range(i+1, iCount):
        word2 = words[j]
        if len(word2) == length1:
            word22 = sorted(word2)
            if word11 == word22:
                words_lst.append((word1, word2))
max_square_num = 0
word1 = ""
word2 = ""
for words in words_lst:
    sq_num = get_max_squares(words[0], words[1], squares[len(words[0])])
    if max_square_num < sq_num:
        max_square_num = sq_num
        word1 = words[0]
        word2 = words[1]

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(max_square_num, word1, word2)
