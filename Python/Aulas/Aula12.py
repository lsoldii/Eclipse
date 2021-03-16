# -*- coding: UTF-8
#while loop

valor = float(100)
dia = 0

while valor > 75:
    dia += 1
    print(f'no dia {dia} o peso do paciente será de {valor}')
    valor -= float(0.5)
