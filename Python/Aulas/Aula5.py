#formated Strings


nome =input('Qual o seu nome?')
idade =input('Qual a sua idade?')
cidade =input('Onde voc� mora?')
comida =input('Qual sua comida favorita?')
gosto =input('O que voc� mais gosta de fazer?')
idade =str(idade)

texto1 = 'O ' + nome + ' tem ' + str(idade) + ' anos' + ' e mora em ' + cidade + ', sua comida preferida � '  + comida + ' e gosta muito de ' + gosto

texto2 = f' O {nome} tem {idade} anos e mora em {cidade}, sua comida preferida � {comida} e gosta muito de {gosto}'


print(texto2)