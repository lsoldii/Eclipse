# -*- coding: UTF-8
from datetime import datetime
from http.cookiejar import EPOCH_YEAR

#construtores 



class Users:
    
    def __init__(self, nome, sobrenome, id, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.id = id
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_user(self):
        ano_atual = datetime.now().year
        self.idade_user = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        

usuario1= Users('Luiz', 'Soldi', '6', 1999)
usuario2= Users('Lucas', 'Silva', '12', 2003)


#print(usuario1.nome_completo())
#print(Users.nome_completo(usuario2))
print(Users.idade_user(usuario1))
   