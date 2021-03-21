# -*- coding: UTF-8
#Dicionários
    #utiliza indez no formato de Keys e Values


aluno = {'nome': 'Ana', 'idade': 20, 'nota_final': 72, 'aprovação': True}

#aluno.update({'nome':'Jose', 'nota_final': '80'})
#aluno.update({'endereço': 'Rua 6'})

print(aluno.get('endereço', 'Não existe'))

