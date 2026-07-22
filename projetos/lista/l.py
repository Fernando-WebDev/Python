'''
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
print(l[5:16]) #fatiar a lista da posição 5 à 16
print(l[2:18:3]) # l[inicio:fim:espaçamento]
print(l[3:18:7])
print(l[:17:2])
print(l[5::4])

print(l)
l.sort() # o .sort() ordena em ordem númerica ou afalbetica
print(l)
'''

n = []
acu = 0
qntdd = 0
media = 0
menor = 0
maior = 0
iguais = 0
cont = True

while cont == True:

    n_ou_sair = input('Digite uma nota ou "s" para sair: ').lower

    if 's' in n_ou_sair:
        cont = False
    else:
        cont = True
