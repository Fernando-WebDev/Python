x = 1
while x < 6:
    x += 2
    print(x)
print("...........")

x = 9
while x > 3:
    print(x)
    x -= 2
print("...........")

x = 9
while x != 3:
    print(x)
    x -= 2
print("...........")

x = 4
while x < 20:
    print(x)
    x += 3
print("...........")

x = 21
while x > 11:
    print(x)
    x -= 2
print("...........")

x = -3
while x < 12:
    print(x)
    x += 3
print("...........")

x = 2
while x > -16:
    print(x)
    x -= 3
print("...........")

pares = -200
while pares < -99:
    print(pares)
    pares += 2
print("...........")

mult_7 = -728
while mult_7 < 1352:
    print(mult_7)
    mult_7 += 7
print("...........")

y = -308
while y < 252:
    y += 14
    print(y)
print("...........")


senha = input("digite sua senha: ")
while not(senha.isnumeric()):
    senha = input("digite sua senha: ")
else:
    print("Acesso liberado!")
print("...........")

idade = ""
ctg = 0
while idade.isnumeric() and idade > 102:
    idade = input("Digite sua idade: ")