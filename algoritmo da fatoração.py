#algoritmo de euclides
#Introdução à Teoria dos Números (2003, Santos, José Plínio Oliveira de)

def alg_euclides(r0,r1):
    if r1==0:
        print("eof")
    else:
        print(f'{r0//r1}x{r1}+{r0-((r0//r1)*r1)}')
        print("eof")
alg_euclides(5,2)