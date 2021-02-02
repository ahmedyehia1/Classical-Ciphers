from classicalCipher import Hill

with open("../Input Files/Hill/hill_plain_3x3.txt",'r') as plainFile:
    with open("../Input Files/Hill/hill_cipher_3x3.txt",'w') as cipherFile:
        for dummy in range(4):
            plaintext = plainFile.readline()[:-1] # ignore the \n character
            cipherFile.write(Hill(plaintext,[[2,4,12],[9,1,6],[7,5,3]]).upper()+'\n')
