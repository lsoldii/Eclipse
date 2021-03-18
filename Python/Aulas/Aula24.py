# -*- coding: UTF-8
#Set (listas)
#não utiliza index e evita itens duplicados

lista=[10, 20, 30, 40]
lista1=[10, 20, 60, 70]


num1 = set(lista)
num2 = set(lista1)

print(num1 | num2) #union
print(num1 - num2) #difference
print(num1 ^ num2) #symmetric difference
print(num1 & num2) #and
print(len(num1))
