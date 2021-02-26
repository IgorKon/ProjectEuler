# XOR decryption

# Problem 59
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard 
# Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, 
# taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, 
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", 
# it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
# and the knowledge that the plain text must contain common English words, decrypt the message and find the sum 
# of the ASCII values in the original text.
# https://projecteuler.net/problem=59

# Brute force approach

import itertools
import datetime

base = 'abcdefghijklmnopqrstuvwxyz'

def TryToTextByXOR(a, key):
    b = [int(x) for x in a]
    d = []
    j = 0
    # check if message starts with upper case symbol
    first = b[0] ^ key[0]
    if first < 65 or first > 90:
        return False, d, ""
    for i in b:
        k = i ^ key[j]
        # check if message don't has non-printing symbol
        if k < 32 or k > 126:
            return False, d, ""
        d.append(k)
        j += 1
        if j > 2:
            j = 0
    s = ''.join(chr(i) for i in d)
    s_low = s.lower()
    if ' on ' in s_low and \
        ' it ' in s_low and \
        ' and ' in s_low and \
        ' at ' in s_low:
        return True, d, s
    return False, d, s

f = open('num59.txt') 
lines = f.readlines()
iCount = 0
foundKey = ''
message = lines[0].split(',')
base_for_key_int = bytearray(base, 'ascii')
start_time = datetime.datetime.now()

for key_int in itertools.product(base_for_key_int, repeat = 3):
    bRes, message_after_XOR, s = TryToTextByXOR(message, key_int)
    iCount += 1
    if bRes:
        foundKey = ''.join(chr(i) for i in key_int)
        break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print('The key is:',foundKey)
print('Text:')
print(s)
print(sum(message_after_XOR))
