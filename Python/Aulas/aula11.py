# -*- coding: UTF-8
#Criar um retangulo de 3x3
 
linhas=3
colunas=3 
linhasx = 1
colunasx = 2
simbolo= '@'
simbolo1 = '|    |'
simbolo2= '|▔▔▔|'
simbolo3='|____|' 

'''for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
'''

for l in range(linhasx):
    print(simbolo2)
    for c in range(colunasx):
        print(simbolo1)
print(simbolo3)