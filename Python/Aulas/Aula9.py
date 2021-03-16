# -*- coding: UTF-8
#Enviar um e-mail de confirmação de compra no máximo de 3 vezes

compra_confirmada= False
dados_compra= 'compra no valor de R$X e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        break
    else:
        print('falha na compra')
        
    