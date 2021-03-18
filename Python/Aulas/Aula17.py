# -*- coding: UTF-8
#listas


cidades = [ ['Canoas', 'Porto Alegre'], ['Rio de Janeiro', 'São Paulo']]
#           0    0           1          1        0             1

print(cidades[1][0])


cidadex= cidades[1][1]


print(cidadex)



produto =['arroz', 'feijão', 'laranja', 'cebola', 5, 6, 7, 8]


item1, item2, *outros = produto

print(item1)
print(outros)