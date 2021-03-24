# -*- coding: UTF-8
#Funções

'''
criar um programa que calcule a quantidade de tinta necessária para pintar uma parede.
O usuário deverá forneceer as seguintes informações: rendimento, altura e largura.
O programa deverá mostrar na tela a mensagem ' você necessita de x latas de tintas'
'''
altura_parede = int(input('Qual é a altura da parede?'))
largura_parede = int(input('Qual é a largura da parede?'))
rendimento = int(input('Qual é o rendimento da lata?'))


def rendimento_lata():
    total_parede = altura_parede * largura_parede
    resultado = total_parede / rendimento
    print(f' Você precisará de {resultado} latas de tinta') 




