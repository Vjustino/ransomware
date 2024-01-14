import os
import pyaes

file_name = "text.txt.ransomware"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = b'12345678abcdefgh'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file_name = "text.txt"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()