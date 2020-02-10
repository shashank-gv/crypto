from Crypto.Cipher import AES
import os

fileNameTemp = raw_input("Enter name of file to be decrypted\t")
fileName = fileNameTemp + ".bin"

file_in = open(str(fileName), "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
key = raw_input("Enter your secret key\t")
keyBytes = bytes(key)
try:
    cipher = AES.new(keyBytes, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    opFileName = raw_input('Enter the name of the file you want the data to be saved in\t')
    opFileName = opFileName + '.txt'
    opFile = open(opFileName, 'wb')
    [opFile.write(x) for x in data]

except ValueError:
    print("Key or message is corrupt")
os.remove(str(fileName))
