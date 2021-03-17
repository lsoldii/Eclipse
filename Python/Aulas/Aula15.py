# -*- coding: UTF-8
#Criar uma função que soma vários números

def soma(*numeros):
    resultado= 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(5, 5, 10, 5)


print(x)    