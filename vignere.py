#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# author: Nikolaj Berntsen
# Derived from
# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)
# This text can be copy/pasted from http://invpy.com/vigenereCipher.py

import argparse
import re
import sys  
import collections

reload(sys)  
sys.setdefaultencoding('utf8')


LETTERS = u'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

def main():
    parser = argparse.ArgumentParser(description='Vignere Cipher with Danish Alphabet')
    parser.add_argument('--encrypt', action="store_true", help='use to encrypt a text')
    parser.add_argument('--decrypt', action="store_true", help='use to decrypt a text')
    parser.add_argument('--text',    help='text to encrypt or decript', type=str)
    parser.add_argument('--key',     help='key to encrypt with', type=str)
    parser.add_argument('--period',  help='take input text and split in "period" strings', type=int)
    args = parser.parse_args()

    myMessage = unicode(args.text, "utf-8")
    myKey = unicode(args.key, "utf-8")
    period = args.period



    if (args.decrypt): 
       myMode = 'decrypt' 
    else:  # default mode is encryption
       myMode = 'encrypt'
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('\n')
    print('%sed message:' % (myMode.title()))
    print(translated.encode('utf-8'))

    # printing 'period' substrings and letter frequencies to assist in guessing key if length is guessed correctly    
    substring=subStrings(translated, period)
    print("\n Translated text in " + str(period) + " substrings for frequency analysis")
    for i in range(0, period) :
        s = str(substring[i].upper())
        print(s)
        print collections.Counter(s)

 
def subStrings(text, period):                 
    substring = []
    for i in range(0, period) :
        substring.append(u"")
    counter = 0
    for symbol in text:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            substring[counter%period] +=  symbol 
            counter +=1
    
    return substring


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)

# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
