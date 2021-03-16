# -*- coding: UTF-8
#Enviar um e-mail de confirma��o de compra no m�ximo de 3 vezes
from test.test_ntpath import tester

compra_confirmada= False
dados_compra= 'compra no valor de R$X e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        break
    else:
        print('falha na compra')
        