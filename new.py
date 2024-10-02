# Python program to demonstrate
# Feistel Cipher Algorithm

import binascii
from common import *

# Random bits key generation
def rand_key(p):
	
	import random
	key1 = ""
	p = int(p)
	
	for i in range(p):
		
		temp = random.randint(0,1)
		temp = str(temp)
		key1 = key1 + temp
		
	return(key1)

# Function to implement bit exor
def exor(a,b):
	
	temp = "" 
	
	for i in range(n): 
		
		if (a[i] == b[i]):
			temp += "0"
			
		else: 
			temp += "1"
			
	return temp 

# Defining BinarytoDecimal() function 
def BinaryToDecimal(binary): 
	
	# Using int function to convert to 
	# string 
	string = int(binary, 2) 
	
	return string

# Feistel Cipher
PT = readFile("message.txt")
print("Plain Text is:", PT)

# Converting the plain text to
# ASCII
PT_Ascii = [ord(x) for x in PT]

# Converting the ASCII to 
# 8-bit binary format
PT_Bin = [format(y,'08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)

n = int(len(PT_Bin)//2)
L1 = PT_Bin[0:n]
R1 = PT_Bin[n::]
m = len(R1)

# Feistel key
KT = readFile("key.txt")
print("Key Text is:", KT)

# Converting the plain text to
# ASCII
KT_Ascii = [ord(x) for x in KT]

# Converting the ASCII to 
# 8-bit binary format
KT_Bin = [format(y,'08b') for y in KT_Ascii]
KT_Bin = "".join(KT_Bin)

# Generate Key K1 for the 
# first round
K1= KT_Bin[0:n]

# Generate Key K2 for the
# second round
K2= KT_Bin[n::]

# first round of Feistel
f1 = exor(R1,K1)
R2 = exor(f1,L1)
L2 = R1

# Second round of Feistel
f2 = exor(R2,K2)
R3 = exor(f2,L2)
L3 = R2

# Cipher text
bin_data = L3 + R3
str_data =' '

for i in range(0, len(bin_data), 7): 
	
	# slicing the bin_data from index range [0, 6] 
	# and storing it in temp_data 
	temp_data = bin_data[i:i + 7] 
		
	# passing temp_data in BinarytoDecimal() function 
	# to get decimal value of corresponding temp_data 
	decimal_data = BinaryToDecimal(temp_data) 
		
	# Decoding the decimal value returned by 
	# BinarytoDecimal() function, using chr() 
	# function which return the string corresponding 
	# character for given ASCII value, and store it 
	# in str_data 
	str_data = str_data + chr(decimal_data) 
	
print("Cipher Text:", str_data)

# Decryption
L4 = L3
R4 = R3

f3 = exor(L4,K2)
L5 = exor(R4,f3)
R5 = L4

f4 = exor(L5,K1)
L6 = exor(R5,f4)
R6 = L5
PT1 = L6+R6


PT1 = int(PT1, 2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Retrieved Plain Text is: ", RPT)
