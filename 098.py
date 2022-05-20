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

start_time = datetime.datetime.now()
f = open('num98.txt') 
lines = f.readlines()
words = lines[0].replace('"', '').split(",")
iCount = len(words)
word_pairs = list()
letters = dict()
first_letters = dict()
for i in range(iCount):
    word1 = words[i]
    word11 = sorted(word1)
    length1 = len(word1)
    for j in range(i+1, iCount):
        word2 = words[j]
        if len(word2) == length1:
            word22 = sorted(word2)
            if word11 == word22:
                word_pairs.append((word1, word2))
                
                if not (word1[0] in first_letters):
                    first_letters[word1[0]] = 1
                if not (word2[0] in first_letters):
                    first_letters[word2[0]] = 1

                for s in word1:
                    if s in letters:
                        k = letters[s]
                        letters[s] = k + 1
                    else:
                        letters[s] = 1
                for s in word2:
                    if s in letters:
                        k = letters[s]
                        letters[s] = k + 1
                    else:
                        letters[s] = 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
