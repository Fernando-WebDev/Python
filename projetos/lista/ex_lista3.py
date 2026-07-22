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
        asc = ord(x)
        print(f'CARACTERS: ', x  , ', ASCII = ', asc)
    
        if asc < 100:
            ints += '0'
            ints += str(asc)
        else:
            ints += str(asc)
    l1.append(ints)

print(l)
print(l1)
