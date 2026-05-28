l = []
l1 = []
n = ''
acu = 0

quant = int(input('Quantos nomes pretende digiar? '))

rep = 0
while rep < quant:
    n = input('Digite um nome: ')
    l.append(n)
    rep += 1

for i in l:
    ints = ''
    for x in i:
        print(f'CARACTERS: ', x  , ', ASCII = ', ord(x))


print(l)
print(l1)
