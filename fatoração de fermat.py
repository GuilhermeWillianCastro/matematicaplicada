##algoritmo de fermat
#COUTINHO, S. C. Números Inteiros e Criptografia RSA. Rio de Janeiro: IMPA, 2000. cap. [número do capítulo], p. 40-41]

import math

n = 1342127; x = (math.trunc(math.sqrt(n)))

if x == n: print("n é composto, fim")

else: x+=1; y = math.sqrt(x**2-n)
while True:
    x+=1; y = math.sqrt(x**2-n)
    if (x == ((n+1)/2)):print('n é primo');break 
    if ((y - int(y)) == 0):print('n é composto',x+int(y),',', x-int(y));break
