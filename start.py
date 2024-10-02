from common import *
from key_generator import *
from crypt_module import *

#�������� ���������� ��������
#������������� ������� ����� � ASCII, � ����� � 8-������ �������� ������. 
initialKey = readFile("key.txt")
print(initialKey)

# Converting the plain text to
# ASCII
Key_Ascii = [ord(x) for x in initialKey]
print(Key_Ascii)

# Converting the ASCII to 
# 8-bit binary format
Key_Bin = [format(y,'08b') for y in Key_Ascii]
Key_Bin = "".join(Key_Bin)

#������������� ������� ����� � ASCII, � ����� � 8-������ �������� ������.   
initialMessage = readFile('message.txt')
print(initialMessage)
# Converting the plain text to
# ASCII
Message_Ascii = [ord(x) for x in initialMessage]
print(Message_Ascii)

# Converting the ASCII to 
# 8-bit binary format
Message_Bin = [format(y,'08b') for y in Message_Ascii]
Message_Bin = "".join(Message_Bin)

#sub_key = input("Write subkey variant: ")


KeyGenerator1 = KeyGenerator(Key_Bin)
print(KeyGenerator1.keys);

Crypt1 = Crypt(KeyGenerator1)
encrypted_msg = Crypt1.encrypt(Message_Bin)
print(encrypted_msg)
decrypted_msg = Crypt1.decrypt(encrypted_msg)
print(decrypted_msg)
print(binary_to_string(decrypted_msg))

 

 
#��������� �������� ������ �������� ������ �� ��� ��������: ����� �������� (L1) � ������ �������� (R1) 
 
#������������ ��������� �������� ����� (K1 � K2) ������, ������ �������� ����� ��������� ������ ��� ���� �������. 