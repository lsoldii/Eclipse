# -*- coding: UTF-8
#if else

'''
Criar um programa que dependedno da temperatura(em celsius) do steak ele retorna o ponto de cozimento em portugues.
o usuário deverá fornecer a temperatura.

48º - selada
54º - ao ponto para o mal
60º - Ao ponto
65º - Ao ponto para o bem
71º - bem passada
'''

temperatura = int(input('Qual a temperatura da carne?'))

if temperatura < 48:
    print('Deixe mais alguns minutos no fogo (Carne muito mal passada)')
elif temperatura in range(48, 53):
    print('Sua carne está selada!')
elif temperatura in range(54, 59):
    print('Sua carne está ao ponto para o mal!')
elif temperatura in range(60, 64):
    print('Sua carne está ao ponto!')
elif temperatura in range(65, 70):
    print('Sua carne está ao ponto para o bem!')
elif temperatura > 70:
    print('Sua Carne está bem passada!')

#else:
    #print('Sua Carne está bem passada!')
