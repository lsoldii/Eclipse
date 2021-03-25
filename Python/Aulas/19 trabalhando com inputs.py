# -*- coding: UTF-8


escolhacor = input('Digite a cor desejada:')
cor = ['amarelo', 'azul', 'verde', 'vermelho']

if escolhacor.lower() in cor:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')