# -*- coding: UTF-8
#looping em dicionários
from _ast import And


aluno = {'nome': 'Ana', 'idade': 20, 'nota_final': 72, 'aprovação': True}

for keys, values in aluno.items():
#for x in aluno.items():
    print(keys, values)