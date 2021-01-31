import sys
import numpy as np

# complimentary functions
def intChar(c):
    return (ord(c)-65)%32
def charInt(i):
    return chr(i%26+97)

#  classical ciphers
def caeser(plaintext,key):
    return ''.join([charInt(intChar(p)+key) for p in plaintext])

def playFair(plaintext,key):
    def getRowCol(n):
        return int(np.floor(n/5)),n%5
    def setRowCol(r,c):
        return r*5+c
    plaintext = plaintext.replace(' ','').replace('j','i')
    matrix = {k:i for i,k in enumerate(dict.fromkeys(key.replace(' ','').replace('j','i')))}
    inv_matrix = dict([(value, key) for key, value in matrix.items()]) 
    it = len(matrix)
    for i in range(26):
        if charInt(i) != 'j' and matrix.get(charInt(i)) == None:
            matrix.setdefault(charInt(i),it)
            inv_matrix.setdefault(it,charInt(i))
            it+=1
    output,i = '',0
    while i < len(plaintext):
        r1,c1 = getRowCol(matrix[plaintext[i]])
        if i == len(plaintext)-1 or plaintext[i] == plaintext[i+1]:
            r2,c2 = getRowCol(matrix['x'])
            i += 1
        else:
            r2,c2 = getRowCol(matrix[plaintext[i+1]])
            i += 2
        if r1 == r2:
            output += inv_matrix[setRowCol(r1,(c1+1)%5)] + inv_matrix[setRowCol(r2,(c2+1)%5)]
        elif c1 == c2:
            output += inv_matrix[setRowCol((r1+1)%5,c1)] + inv_matrix[setRowCol((r2+1)%5,c2)]
        else:
            output += inv_matrix[setRowCol(r1,c2)] + inv_matrix[setRowCol(r2,c1)]
    return output

def Hill(plaintext,key):
    if type(key) == list:
        key = np.array(key)
    plaintext += 'x'*(len(plaintext) % key.shape[0])
    plaintext = np.array([intChar(p) for p in plaintext]).reshape(-1,key.shape[1]).T
    return ''.join(np.vectorize(lambda x: charInt(x))(np.dot(key,plaintext).T.reshape(1,-1).flatten()).tolist())

def vigenere(plaintext,key,mode=True):
    # True: auto-mode, False: repeating-mode
    key += plaintext if mode else key * (len(plaintext)//len(key))
    return ''.join([charInt(intChar(p)+intChar(key[i])) for i,p in enumerate(plaintext)])

def vernam(plaintext,key):
    return ''.join([charInt(intChar(p)+intChar(key[i])) for i,p in enumerate(plaintext)])
