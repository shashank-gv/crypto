from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

fileName = raw_input("Enter name of the file (with extension) that needs to be encrypted\t")

try:
    f = open(str(fileName), "r")
    if f.mode == "r":
        data = f.read()
except (IOError):
    print('File does not exist')
    exit()

key = raw_input("Enter a key of length 16\t")
while(1):
    if(len(str(key)) == 16):
        break
    else:
        print("Key must be of length 16\n")
        key = input("Enter a key of length 16\t")
keyBytes = bytes(key)

cipher = AES.new(keyBytes, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
encryptedFileName = raw_input("Enter name of the file where you want to save the encrypted data\t")

eName = str(encryptedFileName) +".bin"
file_out = open(eName, "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
os.remove(str(fileName))
