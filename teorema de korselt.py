##Teorema de Korselt
#COUTINHO, S. C. Números Inteiros e Criptografia RSA. Rio de Janeiro: IMPA, 2000. cap. 2, p. 109]
import time

def teorema_korselt(q):
    q0=q
    i = 2
    fatores_p = []
    while i**2 <= q:
        if q % i: i += 1
        else: q //= i; fatores_p.append(i)
    if q > 1: fatores_p.append(q)
    #print(fatores_p)
    cond1 = []
    cond2 = []
    if len(fatores_p)>1:
        for p in fatores_p:
            if (q0//(p**2) != q0/(p**2)): cond1.append(p)
            if (((q0-1)//(p-1))==((q0-1)/(p-1))): cond2.append(p)
        if ((len(cond1)-len(fatores_p)) == 0) and ((len(fatores_p)-len(cond2)) == 0): print(q0,'é um número de Carmichael')
        else:(print(q0,'não é um número de Carmichael'))
    #time.sleep(.001)

for q in range(2, 1110):  
  if teorema_korselt(q):
    print(q, "é um número de Carmichael")