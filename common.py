import math
import binascii

#encoding = 'cp1251'
encoding = 'utf8'

def readFile(filename): 
    f1 = open(filename, "r", encoding='utf-8')
    msg = f1.read()
    f1.close()
    return msg

def writeFile(file, line):
    file2 = open(file, 'w', encoding='utf-8')
    file2.write(line)
    file2.close
    
def string_to_binary(text, encoding=encoding, errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def binary_to_string(s, encoding=encoding, errors='surrogatepass'):
    byte_data = bytearray()
    for i in range(0, len(s), 8):
        byte_data.append(int(s[i:i+8], 2))
    try:
        return byte_data.decode(encoding, errors)
    except UnicodeDecodeError:
        return byte_data.decode('latin1')

def string_to_hex(text, encoding=encoding, errors='surrogatepass'):
    return text.encode(encoding, errors).hex()
 