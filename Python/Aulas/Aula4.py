#Calculo de troco

valorprod =input('Qual o valor do produto?')
valor = input('Quanto de dinheiro o cliente lhe fornececeu?')
valorprod= float(valorprod)
valor= float(valor)

resultado = valor - valorprod
resultado = float(resultado)

# caso faltar preciso que mostre o valor faltante (Ainda n�o mostrado em aula) - se valor do resultado do print for negativo


#Aula 24

if resultado > 0:
    print('voc� precisa dar de troco o valor de ' +str(resultado) + ' reais')
elif resultado == 0:
    print('Voc� n�o precisa dar nenhum troco')
else:
   print('Valor faltante de ' + str(resultado) + ' reais')