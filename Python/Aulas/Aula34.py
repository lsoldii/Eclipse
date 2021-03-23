# -*- coding: UTF-8

#construtores 



class Users:
    
    def __init__(self, nome, sobrenome, id):
        self.nome = nome
        self.sobrenome = sobrenome
        self.id = id
    

usuario1= Users('Luiz', 'Soldi', '6')
usuario2= Users('Lucas', 'Silva', '12')


print(usuario1.nome)
   