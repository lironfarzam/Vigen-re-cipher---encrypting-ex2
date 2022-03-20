from ast import keyword
from ctypes import pointer
from itertools import count
from operator import index
from queue import Empty
from typing import Counter

# ------------------------------- const --------------------------------#
ordOfLeter = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
              "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21,
              "w": 22, "x": 23, "y": 24, "z": 25}

englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                     'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41,
                     'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15,
                     'X': 0.15, 'Q': 0.10, 'Z': 0.07}

EmptyLetterFreq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                   'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
                   'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

MAX_K = 10
SIZE_A_B = 26

ciphertext = '''
WBWMDOCGIJPHLQWUQUCHVCJVSRVBVWHSUVWFOOQGUHHBUNIVMNGZBXGGB
FVQRHLSFYVLGZKGWLWRFRGWUGRJUQBYIJVWQKGTRLRSTMLRXQFPELKCQGS
NZHHHNOLRLGLWMFVCXRAPHHPDKULFDGTRVEEOOPWFQLTZGFWIPVRHGJADW
MGPWVXZGFHZWTGHMFQHKIJYCUHKOCYMFITUSEVVHYFKBWIDNWJMTNSFMHJS
UXWZHEEUMHRTDCWQXWZHDGARVHVGTQBTZGFLWSROLVGHOOKGTWWLEUHK
ELEFHELGHKIWPQUCHVWRRSPRWLWTSYIJUWQKVGQUCHVWRRLJSGILCWOIVQD
HVSVWRRGHOFMHJSUMKECQXJQZOIVDCWLTAHKISNURVAVVPEFFWQISEVLRKV
OQGWDMDOWAHKICGMLWSUSFVWVWGISNZBOFQKQSFNMWSLJSFSEOIQMUCBW
WMUIDPDAOVLGTHVXJKBJSXEVDVSEHHVKYVLGZKGQIWFSGXGFSFVQRHWLWEW
SLWTHHBLHCUQSNZBEUTMSXGUMVXWOWVXZGCUHWTSGPAUHRJWNSPIFVGRJ
XKBLXWRCVWADZHTDCWQXWZHVJAPWWIHQGVMTNSFCHJSUXWZHVJAPWWIHQ
GVMTNSNIQUOQHLJSHRUTMSXAQBDRVFSFVQRHLSFCZJSJKHKQKYVLGZECUVW
UDRRVVCHEUJYHCCGMVEJGWPTGTHDRLDCWLXQFPEDNMDRVKBDGLWOOTJCQ
WMUGOVGARVHVKYWWLGWHYEJKOEPWMSBWUCBEILTWYMSNZBFJQYHROKHK
SFNMWLWMBRADGRJIGHHKIUKDKIJWGHHSPRDVWVVHVWHCUIMUSOIKUCUINGB
FSMPHHVHTCGYUVWYIXQFPSKVDXVHQGHW
'''

## test:
# ciphertext = "CCBCCCCABCABAABCAA"
# englishLetterFreq ={"A":0.2,"B":0.1,"C":0.7}
# EmptyLetterFreq = {'A': 0, 'B': 0, 'C': 0}
# SIZE_A_B = 3
# MAX_K = 30

# test2:
# ciphertext = "DCBC BDBC CBBD BCAC BABB"
# englishLetterFreq ={"A":0.1,"B":0.1,"C":0.3,"D":0.5}
# EmptyLetterFreq = {'A': 0, 'B': 0, 'C': 0 , "D":0}
# SIZE_A_B = 4
# MAX_K = 4


# ------------------------------- function --------------------------------#

# function to find K value
'''
By loop from 2 to MAX_K we check what the optimal k value
is by moving the text k values and comparing to the source
The comparison is until the source text stops.
return value is the optimal k
'''


def findK(ciphertext):
    index = 0
    maxLen = len(ciphertext)
    maxCounter = 0
    for i in range(1, MAX_K):
        counter = 0
        for j in range(0, maxLen):
            if (j + i < maxLen and ciphertext[j] == ciphertext[j + i]):
                counter += 1
        if counter > maxCounter:
            maxCounter = counter
            index = i
        print("if k =", i, "counter of match: ", counter)
    return index


# function get text ,k value,and index split the text in blocks of k and return STRING of all latter in the block
def getStringIndexBloke(ciphertext, k, index):
    str = ""
    i = 0
    pointer = i * k + index
    while (pointer < len(ciphertext)):
        str += ciphertext[pointer]
        i += 1
        pointer = i * k + index
    return str


# function to get the frequency of each letter in the text
def getLetterFreq(text):
    freq = EmptyLetterFreq.copy()
    for letter in text:
        freq[letter] += 1

    print("freq of all letter: \n\n", freq, "\n")

    for letter in freq:
        freq[letter] = freq[letter] / len(text)

    return freq


# function to finde the keyWord
"""
The function get the text and the k 
By dividing the blocks by the length of the keyword (K) 
we find all the words encrypted by the same letter.
By analyzing frequencies using a scalar product we find the
signal with the highest chance of being in the encryption word.
And finally we return the encryption word we found 
(it is not sure but it is probable it has the highest chance)
"""


def findKeyWord(ciphertext, k):
    keyword = ""
    for index in range(0, k):
        print("-" * 20)
        print(f"\nfor the index - {index} in the keyword:  \n")
        textFromBloke = getStringIndexBloke(ciphertext, k, index)
        # print(f"string of plase {index}: ", textFromBloke)
        # print(f"letter freq of string {index}: ", getLetterFreq(textFromBloke))
        difrent = findDifference(getLetterFreq(textFromBloke), englishLetterFreq)
        # print(f"----difference of {index}: ", difrent)
        keyword += chr(difrent + ord('a'))
        print("we found the letter:", keyword[index], "\n")
        # print(f"keyword: {keyword}")
    return keyword


# function to find the difference between the english letter frequency and the text frequency
def findDifference(textFreq, englishFreq):
    # for debug..
    # mostFreqInText = max(textFreq, key=textFreq.get)
    # mostFreqInEnglish = max(englishFreq, key=englishFreq.get)
    # print("mostFreqInText: ", mostFreqInText, "ord(mostFreqInText): ", ord(mostFreqInText)-ord('A'))
    # print("mostFreqInEnglish: ", mostFreqInEnglish ,"ord(mostFreqInEnglish): ", ord(mostFreqInEnglish)-ord('A'))
    # print("so the difference is: ", ((ord(mostFreqInEnglish) - ord(mostFreqInText))%SIZE_A_B))
    maxMul = 0
    diff = 0
    # can be optimized by using the lamda function...
    # maybe in the future...                      ***
    for i in range(0, SIZE_A_B):
        mul = dotProduct(textFreq, englishFreq, i)
        print(f"for A,{i} mul is: ", mul)
        if mul > maxMul:
            maxMul = mul
            diff = i
    return diff


# function to Dot product 2 vectors
"""
by using loop we find the dot product of 2 vectors 
and return the value 
By going through indexes and calculating its frequency in the candidate vector
"""


def dotProduct(vectorB, vectorA, index):
    dotProduct = 0
    for i in vectorB:
        dotProduct += (vectorA[i] * vectorB[chr(((((ord(i) - ord("A")) + index) % SIZE_A_B) + ord("A")))])
    return dotProduct


# function to edit ciphertext
"""
Reset the text by lowering spaces and the like
"""


def editCiphertext(ciphertext):
    ciphertext = ciphertext.replace("\n", "")
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.replace("   ", "")
    return ciphertext


# function to encrypt the text(ciphertext) with the key(keyword)
def encrypt(ciphertext, keyword):
    plaintext = ""
    for i in range(0, len(ciphertext)):
        a = ciphertext[i]
        b = ord(keyword[i % len(keyword)]) - ord('a')
        plaintext += chr(((((ord(a) - ord('A')) - b) % SIZE_A_B) + ord('a')))
    return plaintext


# -------------- main --------------#
ciphertext = editCiphertext(ciphertext)
k = findK(ciphertext)
print("\nK value is: ", k, "\n")
keyword = findKeyWord(ciphertext, k)
print("-=" * 20)
print("keyword is: ", keyword)
print("-=" * 20)
print("plaintext is:\n", encrypt(ciphertext, keyword))
print("-=" * 20)