# -*- coding: UTF-8
#erros


try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)

except ValueError:
    print('Digitar apenas números inteiros')
else:
    print('Valor computado com sucesso')
    
    
    
