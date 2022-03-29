#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:01:08 2022

@author: alejandro
"""

from keycode import KeyCode

Kc = 'ẍ\
abcdefghijklmnñopqrstuvwxyz\
ABCDEFGHIJKLMNÑOPQRSTUVWXYZ\
0123456789áéíóú (),.!?;:"\
|¿¡°#$%&/=+-*-_@~\
[]{}<>ẅ'

ran = len(Kc)

dict_in = {Kc[idx]:int(idx) for idx in range(ran)}
dict_out = {int(idx):Kc[idx] for idx in range(ran)}

# FUNCIONES

def open_text_in(text:str, ran:int, dict_in:dict) -> int :
    text = text.replace('\n','ẅ')
    l = len(text)
    num = 0
    for i in range(l):
        # try:
            num += dict_in[text[i]] * ran**(int(i))
        # except KeyError:
        #     num += dict_in['?'] * ran**(int(i))
    return num

def open_text_out(num:int, ran:int, dict_out:dict) -> str :
    text = ''
    r , div = 1 , 1
    while div != 0:
        div = num // ran
        r = num % ran
        num = div
        text += dict_out[r]
    text = text.replace('ẅ','\n')
    return text

def int_to_lis_int(num:int, max_len:int) -> list:
    dig = str(num)
    while len(dig) % max_len != 0:
        dig = '0' + dig
    rang = len(dig) // max_len
    dig_lis = [dig[max_len*idx:max_len*(idx + 1)] for idx in range(rang)]
    return [int(dig) for dig in dig_lis]

def lis_int_to_int(lis_int:list, max_len:int) -> int:
    pass
        
def power_tower(num:int, mod:int, max_power:int) -> list:
    pow_tow = [num % mod]
    for _ in range(1, max_power):
        power = pow_tow[0] ** 2 % mod
        pow_tow.insert(0, power)
    return pow_tow

def power_mod(num:int, exp:int, mod:int) -> int:
    
    bin_exp = bin(exp)
    bin_exp = bin_exp[2:]
    max_power = len(bin_exp)
    
    pow_tow = power_tower(num, mod, max_power)
    
    result = 1
    for idx in range(max_power):
        if bin_exp[idx] == '1':
            result *= pow_tow[idx]
            result %= mod
    return result

def exponential_cipher_lis(int_lis:list, exp:int, mod:int) -> list:
    return [power_mod(num, exp, mod) for num in int_lis]    



k1=2758777663931
k2=11479179514433
k3=2038615913437

# OPERACIONES

k1=2758777663931
k2=11479179514433
k3=2038615913437
max_len = len(str(k1)) 
text = '''
Este es un texto que tiene
saltos de línea y todo

xD
'''

text = text.replace('\n','ẅ')

num = open_text_in(text, ran, dict_in)

dig = str(num)

dig_2 = dig

while len(dig) % (-1 % len(str(k1))):
    dig = '0' + dig
    
int_lis = int_to_lis_int(num, max_len - 1)

int_lis_c = exponential_cipher_lis(int_lis, k2, k1)

int_lis_c = [str(num) for num in int_lis_c]

for idx in range(len(int_lis_c)):
    
    while len(int_lis_c[idx]) % max_len != 0:
        int_lis_c[idx] = '0' + int_lis_c[idx]

num_c = int(''.join(int_lis_c))

text_c = open_text_out(num_c, ran, dict_out)



exponential_cipher_lis(int_lis_c, k3, k1)
print(open_text_out(num, ran, dict_out))






