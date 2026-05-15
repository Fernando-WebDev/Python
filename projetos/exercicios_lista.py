'''
lista = [] #cria uma lista com '[]'
lista2 = [1, '2', 1.0, True] #Uma lista pode conter varios tipos de dados e valores
lista.append('Abacaxi') #.append adiciona no fim da lista o seu dado inserido
lista.insert(0, 'mamão') #.insert adiciona o seu dado na posição que você desejar
'''
#exercicios

lista0 = ['B', 'D', 'E']
lista0.insert(0, 'A')
lista0.insert(2, 'C')
lista0.append('F')
print(lista0)

lista1 = ['a', 'b', 'c']
print(lista1)
nota = lista1[1]
print(nota)
lista1[2] = 'sss' #substitui um elemento da lista
print(lista1)

cauda = lista1.pop() #.pop ele "rouba" o ultimo elemento da lista ou um elemento especifico, basta especificar. ex.: lista.pop(1)
print(cauda)

lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = []
x = lista2.pop(0)
x += lista2.pop(0)
x += lista2.pop(0)

y = []
y = lista2.pop(0)
y += lista2.pop(1)
y += lista2.pop(2)

print(x)
print(y)
del(lista2[1])
print(lista2)