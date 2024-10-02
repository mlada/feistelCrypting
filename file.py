#include <iostream>
#include <string>
#include <Windows.h>
encoding = 'utf8'
 
def fo(subblock, key, round):
    return (int(subblock) * int(key[round])) % (pow(2, round)+1); #Образующая функция

 
def DeCode(func):
    n = 16
    block = readFile('message.txt'); #Исходное сообщение
    # Converting the plain text to
    # ASCII
    block_Ascii = [ord(x) for x in block]
    # Converting the ASCII to 
    # 8-bit binary format
    block_Bin = [format(y,'08b') for y in block_Ascii]
    mes = "".join(block_Bin)
    # print(block_Bin)
    ikey = readFile('key.txt')    #Ключ
    # Converting the plain text to
    # ASCII
    Key_Ascii = [ord(x) for x in key]
    # Converting the ASCII to 
    # 8-bit binary format
    Key_Bin = [format(y,'08b') for y in Key_Ascii]
    key = "".join(Key_Bin)

    temp = '0'
    l = '0'
    res = [];
    r = '0';
    for desc in range(0,len(mes),2): #рассматриваем блоки по 2 символа
        res.append([])
        res.append([])
        l = mes[desc];
        r = mes[desc + 1];
        for i in range(n-1,0,-1):  #n раундов        
            temp = int(l) ^ func(r, key, i);
            l = r;
            r = temp;
        res[desc].append(int(l));
        res[desc+1].append(int(r));
    return mes;

def readFile(filename): 
    f1 = open(filename, "r", encoding='utf-8')
    msg = f1.read()
    f1.close()
    return msg

def writeFile(file, line):
    file2 = open(file, 'w', encoding='utf-8')
    file2.write(line)
    file2.close();

def Code(variancy, v_func):
    n = 16
    block = readFile('message.txt'); #Исходное сообщение
    # Converting the plain text to
    # ASCII
    block_Ascii = [ord(x) for x in block]
    # Converting the ASCII to 
    # 8-bit binary format
    block_Bin = [format(y,'08b') for y in block_Ascii]
    mes = "".join(block_Bin)
    # print(block_Bin)
    ikey = readFile('key.txt')    #Ключ
    # Converting the plain text to
    # ASCII
    Key_Ascii = [ord(x) for x in ikey]
    # Converting the ASCII to 
    # 8-bit binary format
    Key_Bin = [format(y,'08b') for y in Key_Ascii]
    key = "".join(Key_Bin)
    if (v_func == '0'):
        func = fo
    else:
        func = fo


    if (variancy == '0'):      
        temp = '0'
        l = '0'
        r = '0';
        res = [];
        for desc in range(0, 32 ): #рассматриваем блоки по 2 символа (1 символ = 8 бит)
            res.append([])
            res.append([])
            l = mes[desc];
            r = mes[desc + 1];
            for i in range(0, n): # n раундов       
                temp = int(r) ^ func(l, key, i);
                r = l;
                l = temp;        
            res[desc].append(int(l))
            res[desc+1].append(int(r));
    else:
        temp = '0'
        l = '0'
        r = '0';
        res = [];
        for desc in range(0, len(mes),2 ): #рассматриваем блоки по 2 символа (1 символ = 8 бит)
            res.append([])
            res.append([])
            l = mes[desc];
            r = mes[desc + 1];
            for i in range(0, n): # n раундов       
                temp = int(r) ^ func(l, key, i);
                r = l;
                l = temp;        
            res[desc].append(int(l))
            res[desc+1].append(int(r));

    writeFile('ci_message.txt', mes + '\n\n'+ binary_to_string(mes)+ '\n\n')
    return mes;

def binary_to_string(s, encoding=encoding, errors='surrogatepass'):
    byte_data = bytearray()
    for i in range(0, len(s), 8):
        byte_data.append(int(s[i:i+8], 2))
    try:
        return byte_data.decode(encoding, errors)
    except UnicodeDecodeError:
        return byte_data.decode('latin1')
