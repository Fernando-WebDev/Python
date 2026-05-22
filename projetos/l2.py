l = []
n_ou_sair = 0

while n_ou_sair != 's':
    n_ou_sair = input('Difite uma nota ou "s" para sair: ')

    if n_ou_sair != 's':
        l.append(int(n_ou_sair))
        
        

qntdd = len(l)
acu = sum(l)
l.sort()
print()
print(l)
print('menor nota: ', l[0])
print('mediana: ', l[qntdd//2])
print('quantidade de notas: ', qntdd)
print('Acumulado: ', acu)
print('média: ', acu/qntdd)
print('maior nota: ', l[qntdd - 1])

for i in l:
    if i < acu/qntdd:
        a = i
print(a)

for j in l:
    if j > acu/qntdd:
        b = j
print(b)