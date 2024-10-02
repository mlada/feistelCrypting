from common import *
from key_generator import *
from encrypt import *

initialKey = readFile("key.txt")
print(initialKey)
binaryKey = string_to_binary(initialKey)
print(binaryKey)
KeyGenerator1 = KeyGenerator(binaryKey)
print(KeyGenerator1.keys);
  
initialMessage = readFile('message.txt')
print(initialMessage)
binaryMessage = string_to_binary(initialMessage)
print(binaryMessage)
Crypt1 = Crypt(KeyGenerator1)
encrypted_msg = Crypt1.encrypt(binaryMessage)
print(encrypted_msg)
decrypted_msg = Crypt1.decrypt(encrypted_msg)
print(decrypted_msg)
print(binary_to_string(decrypted_msg))
