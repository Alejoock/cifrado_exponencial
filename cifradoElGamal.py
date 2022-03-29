import random

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class TwoWayNode(Node):
    def __init__(self,data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
                
Kc = 'ẍABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '

ran = len(Kc)

dict_in = {Kc[idx]:int(idx) for idx in range(ran)}

dict_out = {int(idx):Kc[idx] for idx in range(ran)}

def open_text_in(text:str) -> int :
    l = len(text)
    num = 0
    for i in range(l):
        num += dict_in[text[i]] * ran**(int(i))
    return num

def open_text_out(num:int) -> str :
    text = ''
    r , div = 1 , 1
    while div != 0:
        div = num // ran
        r = num % ran
        num = div
        text += dict_out[r]
    return text

text = 'AAAEstaEsUnaAContrasenaDe EsasBienPerrazassAAAAAs'

len(str((open_text_in(text))))
  
p = """7219606290 61904110756973047896 8205296506 4662691398 7914193058 0819468693 0032350563 15036137851472350837 4759852909 2067962512 6053388015 8168423496 4490805070 29457261849793365394 8906694134 0113614760 9565065986 2416376029 0701029109 70128990995504864728 0564362349 3673330906 2195718092 7936630003 1291883168 4212336353""".replace(' ','')

# p = '15555555555 5555555555 5558888888 8888888888 8888882222 2222222222 2222222221 '.replace(' ','')

# https://primes.utm.edu/curios/index.php?start=37&stop=78

len(p)

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



p = int(p)

a = random.randint(2,p)

g = random.randint(2,p)

b = random.randint(2,p)

# K = g**a % p

K = power_mod(g, a, p)

m = open_text_in(text)

y1 = power_mod(g, b, p)
y2 = power_mod(K, b, p)
y2 = (y2 * m) % p

(g, p, K)

(open_text_out(g), open_text_out(p), open_text_out(K))

(y1 , y2)

(open_text_out(y1) , open_text_out(y2))

d = p-1-a

res = power_mod(y1, d, p)
res = (res * y2) % p

xx = open_text_out(res)

print(xx)















