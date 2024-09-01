## 

n = 7
f = 2

try: val = int(n)
except: print('insira um número');exit()
N = int(n)
if N < 2: print('insira um número maior do que 1')

while True:
    while True:
        if n//f == n/f:print('f é fator trivial de n');break
        else:
            while True:
                f+=1
                if n//f == n/f:print('f é fator de n');break
                if f**2>=n: print('n é primo');break
            break
    print(n,f)
    break
