##algoritmo de fermat
#COUTINHO, S. C. Números Inteiros e Criptografia RSA. Rio de Janeiro: IMPA, 2000. cap. [número do capítulo], p. 40-41]

import math

n = 17; x = (math.trunc(math.sqrt(n)))

if x**2 == n: print("n é composto")

else: x+=1; y = math.sqrt(x**2-n)
while True:
    x+=1; y = math.sqrt(x**2-n)
    if (x == ((n+1)/2)):print('n é primo');break 
    if ((y - int(y)) == 0):print(x+int(y),',', x-int(y));break
