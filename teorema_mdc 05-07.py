# teorema do máximo divisor comum
#Introdução à Teoria dos Números (2003, Santos, José Plínio Oliveira de)

a = 5
b = 2

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(mdc(a, b))